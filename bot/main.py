"""
Entrypoint for «ورتکس» (Vortex) Telegram Bot.
Initializes configuration, SQLite database, startup workspace cleanup,
background 10-minute TTL workspace reaper job, and async polling loop.
"""

from __future__ import annotations

import logging
import sys
from datetime import UTC, datetime, time, timedelta

from telegram import Update
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from bot import __version__
from bot.config import settings
from bot.database import Database
from bot.dollar import DollarService
from bot.file_handler import FileProcessor, WorkspaceManager
from bot.handlers import VortexBotHandlers, global_error_handler
from bot.llm_client import LLMClient
from bot.security import RateLimiter
from bot.updater import check_for_update, notify_after_restart
from bot.web_tools import WebToolkit

# Configure structured logging without exposing sensitive payloads
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    stream=sys.stdout,
)
# Silence overly verbose HTTP logs that might log URLs with tokens
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

logger = logging.getLogger("vortex_bot.main")


async def _ttl_workspace_cleanup_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Periodic job that enforces the max 10-minute TTL on any leftover temp directories."""
    workspace_mgr: WorkspaceManager = context.application.bot_data["workspace_mgr"]
    removed = workspace_mgr.cleanup_expired_workspaces()
    if removed > 0:
        logger.info("TTL Reaper cleaned up %d expired temporary workspace(s).", removed)


async def _token_health_check_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Periodic job: test every LLM token, keep only the working ones,
    and rotate the active token at random among them."""
    llm_client: LLMClient = context.application.bot_data["llm_client"]
    await llm_client.token_pool.health_check()


async def _dead_token_recovery_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Periodic job: re-test every quarantined key; a key that answers
    is moved back into the active pool."""
    llm_client: LLMClient = context.application.bot_data["llm_client"]
    await llm_client.token_pool.retry_dead()


async def _update_check_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Daily job: check GitHub for a newer release and, when one
    exists, offer the boss the update (see bot/updater.py)."""
    await check_for_update(
        context.bot,
        context.application.bot_data["db"],
        settings.update_repo,
        __version__,
        boss_id=settings.boss_id,
        enabled=settings.update_check_enabled,
    )


async def _post_init(application: Application) -> None:
    """Runs on bot startup: cleans leftover workspaces and registers periodic TTL reaper."""
    workspace_mgr: WorkspaceManager = application.bot_data["workspace_mgr"]
    workspace_mgr.cleanup_all_on_startup()
    # If the previous run updated itself and restarted, tell the boss
    # the bot is updated and back on.
    await notify_after_restart(
        application.bot,
        application.bot_data["db"],
        settings.boss_id,
    )
    if application.job_queue is None:
        # The job queue needs the `python-telegram-bot[job-queue]`
        # extra. Without it the health check, dead-token recovery and
        # workspace reaper silently never run — fail loudly in the log
        # instead of pretending the bot is healthy.
        logger.error(
            "JobQueue is None (python-telegram-bot[job-queue] not installed?): "
            "token health check, dead-token recovery and workspace TTL reaper are DISABLED."
        )
    else:
        application.job_queue.run_repeating(
            _ttl_workspace_cleanup_job,
            interval=120,
            first=60,
            name="workspace_ttl_reaper",
        )
        application.job_queue.run_repeating(
            _token_health_check_job,
            interval=settings.token_health_check_interval_seconds,
            first=60,
            name="token_health_check",
        )
        application.job_queue.run_repeating(
            _dead_token_recovery_job,
            interval=settings.token_dead_retry_interval_seconds,
            first=300,
            name="dead_token_recovery",
        )
        # Daily update check, first run ~5 minutes after startup, then
        # every 24h at that same time of day (UTC, the job queue's
        # default timezone). run_daily takes a time-of-day, so the
        # first run is scheduled by computing "now + 5 minutes".
        first_check = datetime.now(UTC) + timedelta(minutes=5)
        application.job_queue.run_daily(
            _update_check_job,
            time=time(
                hour=first_check.hour,
                minute=first_check.minute,
                second=first_check.second,
            ),
            name="update_check",
        )
    logger.info("Vortex Bot initialized and ready for group chats!")


def build_application() -> Application:
    settings.validate()

    db = Database(settings.database_path)
    # Locale + country providers (bot/locale.py, bot/countries.py): the
    # bot's language and country are read from bot_settings on every
    # call, so an /admin change applies immediately. Precedence: DB
    # setting if present, else the env/config default, else the
    # hardcoded default (see bot/config.py). The wake word is the bot's
    # name (BOT_NAME, default "Vortex").
    from bot.countries import set_country_provider
    from bot.locale import set_language_provider
    from bot.security import set_wake_word

    set_language_provider(
        lambda: db.get_language(settings.bot_language or "en")
    )
    set_country_provider(
        lambda: db.get_country(settings.bot_country or "United States")
    )
    set_wake_word(settings.bot_name or "Vortex")
    workspace_mgr = WorkspaceManager(
        root_dir=settings.temp_workspace_root,
        ttl_seconds=settings.workspace_ttl_seconds,
    )
    # Clean leftover temporary folders immediately on startup as well
    workspace_mgr.cleanup_all_on_startup()

    file_processor = FileProcessor(
        workspace_mgr=workspace_mgr,
        max_file_size_bytes=settings.max_file_size_bytes,
        max_pdf_pages=settings.max_pdf_pages,
        max_table_rows=settings.max_table_rows,
        max_extracted_chars=settings.max_extracted_chars,
        process_timeout_seconds=settings.file_process_timeout_seconds,
    )
    dollar_service = DollarService(
        primary_url=settings.dollar_primary_url,
        fallback_url=settings.dollar_fallback_url,
        second_fallback_url=settings.dollar_second_fallback_url,
        cache_ttl_seconds=settings.dollar_cache_ttl_seconds,
    )
    web_toolkit = WebToolkit(
        search_provider=settings.search_provider,
        search_api_key=settings.search_api_key,
        max_results=settings.search_max_results,
    )
    llm_client = LLMClient(
        settings=settings,
        db=db,
        web_toolkit=web_toolkit,
        workspace_root=settings.temp_workspace_root,
    )
    rate_limiter = RateLimiter(
        max_requests=settings.rate_limit_requests,
        window_seconds=settings.rate_limit_window_seconds,
        boss_id=settings.boss_id,
    )
    vortex_handlers = VortexBotHandlers(
        settings=settings,
        db=db,
        dollar_service=dollar_service,
        workspace_mgr=workspace_mgr,
        file_processor=file_processor,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
    )

    app = (
        ApplicationBuilder()
        .token(settings.bot_token)
        .post_init(_post_init)
        .build()
    )
    app.bot_data["workspace_mgr"] = workspace_mgr
    app.bot_data["llm_client"] = llm_client
    app.bot_data["db"] = db

    # Handle text messages, captions, documents, and photos across private & group chats.
    # UpdateType.MESSAGE restricts the handler to NEW messages only:
    # without it, editing a message containing "ورتکس" would re-trigger
    # the bot (and burn another daily quota), and channel posts would
    # arrive with no real sender.
    msg_filter = (
        filters.UpdateType.MESSAGE
        & (filters.TEXT | filters.CAPTION | filters.Document.ALL | filters.PHOTO
         | filters.VOICE | filters.VIDEO | filters.AUDIO)
        & (~filters.StatusUpdate.ALL)
    )
    app.add_handler(MessageHandler(msg_filter, vortex_handlers.handle_message))
    # Inline-button callbacks (hidden /admin panel)
    app.add_handler(CallbackQueryHandler(vortex_handlers.handle_callback_query))
    app.add_error_handler(global_error_handler)

    return app


def main() -> None:
    app = build_application()
    logger.info("Starting Vortex Bot polling...")
    # Only request the update types the bot actually handles. ALL_TYPES
    # also delivers edited_message / channel_post, which the handler
    # must never act on (see the UpdateType.MESSAGE filter above).
    app.run_polling(
        allowed_updates=[Update.MESSAGE, Update.CALLBACK_QUERY],
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()
