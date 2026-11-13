"""
Telegram update handlers for Vortex Bot (`python-telegram-bot` v21+ async).
Implements strict adherence to all functional and security rules:
1. Immediate check of `blocked_users` at the very start of the handler:
   banned users' messages, files, replies, and 'ورتکس دلار' are completely ignored.
2. Private Chat (PV): open to EVERYONE (not just the Boss).
   Anyone can chat with Vortex in PV, no wake word needed.
   There is no channel-membership requirement: the bot works
   with no channel at all. Boss is always exempt from limits.
3. Boss administrative commands (`بن` / `آنبن`):
   - Triggered ONLY when `sender.id == BOSS_ID` and message is a reply to another user.
   - Does NOT require the wake word 'ورتکس'.
   - Exact whole-message match after normalization (configurable command list).
   - Never bans Boss or the Bot itself.
   - Deterministic execution (never passes through LLM).
4. Activation rules in groups:
   - Message text or file caption contains standalone word 'ورتکس' (normalized)
   - OR user replies directly to a message sent by Vortex.
   - OR the message is a known slash command (/gold, /currency, /crypto,
     /time, /weather, /price, /dollar, /stats, /quota, /help, /id, /forget)
     — unknown slash commands (e.g. /start) never activate the bot.
5. Fast paths bypassing LLM:
   - 'ورتکس فراموشم کن' / /forget -> clears only `(chat_id, user_id)` context.
   - 'ورتکس دلار' / /dollar -> fetches cached/fallback USD rate and replies with timestamp.
   - 'ورتکس ارز' / /currency, 'ورتکس طلا' / /gold, 'ورتکس کریپتو' / /crypto
     -> live prices (TGJU + Frankfurter + Nobitex + CoinGecko, 5-min cache).
   - 'ورتکس ساعت' / /time -> Tehran time + Jalali date (pure code).
   - 'ورتکس هوا <شهر>' / /weather <شهر> -> Open-Meteo weather.
   - 'ورتکس قیمت <ارز>' / /price <ارز> -> single currency (Toman + USD).
   - 'ورتکس عکس ...' / 'ورتکس یک عکس بساز از ...' -> image generation
     (neutral caption; the GPT Image label appears ONLY in boss-only stats).
   - extras (fast paths, cost 1 quota): 'ورتکس فال حافظ' / 'اخبار' /
     'اوقات شرعی' / 'حساب کن' / 'تاس' / 'شیر یا خط' / 'جوک' (see bot/extras.py).
   - Meta commands (free, no daily-quota cost): 'ورتکس آمار' / /stats (boss-only stats:
     groups, members with numeric ids, current chat model, image generator),
     'ورتکس سهمیه' / /quota (own daily quota), 'ورتکس راهنما' / /help, 'ورتکس آیدی' / /id
     (own numeric Telegram id).
   - Boss-only chat history (free, no daily-quota cost): 'تا الان چه افرادی باهات
     چت کردن و چه چیز هایی گفتن' / 'با چند نفر چت کردی و چیا گفتن' / 'ورتکس چت‌ها'
     -> code-generated verbatim history from the DB (the LLM refuses this on
     privacy grounds, so it never goes through the LLM); non-boss users get
     the privacy line; in a group the boss is redirected to PV (never dumps
     other users' chats into a group).
6. Daily quota: 30 messages per user per day (boss exempt); meta commands
   above are free, everything else costs 1. Senders are tracked in
   `chat_users` (per chat) for the boss-only stats.
6. File processing pipeline:
   1) Download into isolated temporary workspace
   2) Validate type & size (<= 20MB)
   3) Read & extract content as passive data
   4) Analyze via LLM
   5) Reply to user's message
   6) Immediately delete temporary workspace in `finally` block + save short summary in user context.
"""

from __future__ import annotations

import asyncio
import html
import io
import logging
import random
import shutil
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Message, Update
from telegram.constants import ChatAction, ChatType
from telegram.error import RetryAfter
from telegram.ext import ContextTypes

from bot.config import (
    ProviderEntry,
    Settings,
    find_env_file,
    write_llm_manual_selection,
    write_llm_pinned_model,
    write_llm_providers,
)
from bot.countries import (
    LANGUAGES,
    UI_LANGUAGES,
    country_now,
    country_timezone,
    current_country,
    get_country,
    list_country_names,
)
from bot.database import GLOBAL_CHAT_ID, Database
from bot.dollar import DollarService
from bot.downloader import (
    DownloadError,
    download_error_text,
    download_media,
)
from bot.extras import (
    calc,
    fetch_faal,
    fetch_news,
    fetch_prayer_times,
    flip_coin,
    format_calc,
    format_coin,
    format_dice,
    format_faal,
    format_news,
    format_prayer_times,
    get_joke,
    roll_dice,
)
from bot.file_handler import FileProcessor, WorkspaceManager
from bot.llm_client import LLMClient, LLMResponseResult
from bot.locale import current_language, fmt_num, t, t_list
from bot.prices import (
    currency_label,
    fetch_crypto,
    fetch_fiat,
    fetch_gold,
    fetch_market_updated,
    fetch_oil,
    fetch_weather,
    format_crypto_text,
    format_fiat_text,
    format_gold_text,
    format_single_currency,
    format_weather_text,
    gregorian_to_jalali,
    lookup_currency,
    tehran_now_text,
)
from bot.security import (
    RateLimiter,
    extract_calc_expr,
    extract_download_url,
    extract_image_add_prompt,
    extract_image_prompt,
    extract_prayer_city,
    extract_price_currency,
    extract_weather_city,
    get_wake_word,
    has_vortex_wake_word,
    is_calc_query,
    is_chat_history_query,
    is_coin_query,
    is_crypto_query,
    is_currency_query,
    is_dice_query,
    is_dollar_query,
    is_faal_query,
    is_forget_me_query,
    is_gold_query,
    is_help_query,
    is_id_query,
    is_joke_query,
    is_news_query,
    is_prayer_query,
    is_quota_query,
    is_stats_query,
    is_time_query,
    match_exact_command,
    parse_slash_command,
    set_wake_word,
    strip_wake_word,
)
from bot.token_pool import TokenPool
from bot.transcribe import transcribe_audio
from bot.updater import handle_update_callback

logger = logging.getLogger(__name__)


def _bot_name() -> str:
    """The bot's wake word / name (BOT_NAME, default "Vortex")."""
    return get_wake_word()


# Live user-facing texts come from the locale system (bot/locale/) via
# t("...") at call time, so an /admin language change applies
# immediately. The constants below are import-time aliases (default
# language) kept for backward compatibility — _HELP_TEXT in particular
# is asserted on by tests/test_admin.py ("/admin" must not appear in
# it). New code must use t() directly, not these constants.
_HELP_TEXT = (
    t("help.text", bot="{bot}", currency="{currency}", city="{city}")
)
_START_TEXT = (
    t("start.text", bot="{bot}")
)
# Hidden admin panel (/admin): boss-only, PV-only, never listed in /help
# or in any command menu — it exists only when the boss types it.
# Callback data prefix is "admin:".
_ADMIN_CB = "admin"

# Models that are never chat models: never shown in the /admin "models of
# a key" browser (a listed model can still be dead or hang — the boss's
# pick is validated live with a minimal chat call before it activates).
_ADMIN_NON_CHAT_MODEL_HINTS = (
    "embed",
    "rerank",
    "image",
    "video",
    "audio",
    "tts",
    "whisper",
    "seedance",
    "music",
    "speech",
    "transcri",
    "moderation",
)
_ADMIN_MODELS_PER_PAGE = 10

# Admin-panel permissions for managers (boss-appointed users). The boss
# has all of them; a manager's set is stored in the DB (managers table)
# and chosen by the boss in the 🛡 مدیرها section. The managers section
# itself is boss-only (no permission opens it). Values are locale keys;
# resolve them with _perm_label() at call time so an /admin language
# change applies immediately.
_ADMIN_PERMS = {
    "tokens": "admin.perm.tokens",
    "users": "admin.perm.users",
    "stats": "admin.perm.stats",
    "chats": "admin.perm.chats",
    "image": "admin.perm.image",
    "locale": "admin.perm.locale",
    "power": "admin.perm.power",
}


def _perm_label(perm: str) -> str:
    """Localized button label for an admin permission."""
    return t(_ADMIN_PERMS.get(perm, perm))


def _admin_menu_text() -> str:
    """The /admin main-menu text (localized at call time)."""
    return t("admin.menu", bot=_bot_name())

# Which permission each admin callback route needs (None = anyone who
# can open the panel; "boss" = the boss only).
_ADMIN_ROUTE_PERMS = {
    "tokens": "tokens",
    "addkey": "tokens",
    "removekey": "tokens",
    "pickkey": "tokens",
    "setactive": "tokens",
    "models": "tokens",
    "model": "tokens",
    "modelforce": "tokens",
    "health": "tokens",
    "recover": "tokens",
    "users": "users",
    "ban": "users",
    "unban": "users",
    "allow": "users",
    "unallow": "users",
    "stats": "stats",
    "chats": "chats",
    "image": "image",
    "setimage": "image",
    "addimage": "image",
    "removeimage": "image",
    "power": "power",
    "locale": "locale",
    "setlang": "locale",
    "countries": "locale",
    "setcountry": "locale",
    "managers": "boss",
    "mgr": "boss",
    "mgrtoggle": "boss",
    "mgradd": "boss",
    "mgrremove": "boss",
    "mgrremoveconfirm": "boss",
    "menu": None,
    "close": None,
}

# Known providers for the /admin "add key" flow:
# slug -> (label, base URL, example model).
_ADMIN_PROVIDERS = {
    "nvidia": (
        "NVIDIA",
        "https://integrate.api.nvidia.com/v1",
        "nvidia/nemotron-3-ultra-550b-a55b",
    ),
    "tokenharbor": (
        "TokenHarbor",
        "https://tokenharbor.ai/v1",
        "deepseek-v4-flash:free",
    ),
    "hilinkup": (
        "HiLinkUp",
        "https://api.hilinkup.com/v1",
        "kimi-k3.1-pro",
    ),
}


def _num(value: int) -> str:
    """Render an integer for user-facing text (localized digits)."""
    return fmt_num(value)


def _local_stamp(iso: str) -> str:
    """Local time for a UTC ISO timestamp stored by the DB: 'HH:MM'
    (localized digits) when it is today, otherwise 'D/M/YYYY HH:MM'
    in the Gregorian calendar — or Jalali when the country is Iran.
    Returns '' when the timestamp cannot be parsed."""
    try:
        dt = datetime.fromisoformat(iso)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        country = current_country()
        local = dt.astimezone(country_timezone(country.name))
        hhmm = fmt_num(local.strftime("%H:%M"))
        today = country_now(country.name)
        if country.name == "Iran":
            jy, jm, jd = gregorian_to_jalali(local.year, local.month, local.day)
            ty, tm, td = gregorian_to_jalali(today.year, today.month, today.day)
            if (jy, jm, jd) == (ty, tm, td):
                return hhmm
            date_part = fmt_num(f"{jd}/{jm}/{jy}")
        else:
            if (local.year, local.month, local.day) == (
                today.year,
                today.month,
                today.day,
            ):
                return hhmm
            date_part = fmt_num(f"{local.day}/{local.month}/{local.year}")
        return f"{date_part} {hhmm}"
    except Exception:
        return ""


# Backward-compatible alias (the old name referenced Tehran because the
# bot was Iran-only; the stamp now follows the configured country).
_tehran_stamp = _local_stamp


# Long replies are sent as a Telegram collapsible blockquote so the group
# isn't flooded with a wall of text; users tap the arrow to expand/collapse.
# Short replies stay plain text (no change).
LONG_REPLY_COLLAPSE_CHARS = 500


def _is_service_message(m: Message) -> bool:
    """True for Telegram service messages (forum-topic events, member
    joins/leaves, title/photo changes, pins, ...). They carry no user
    text, so they must never count as a reply-to-bot activation or as
    the target of a boss ban/unban command."""
    return bool(
        m.forum_topic_created
        or m.forum_topic_edited
        or m.forum_topic_closed
        or m.forum_topic_reopened
        or m.new_chat_members
        or m.left_chat_member
        or m.new_chat_title
        or m.new_chat_photo
        or m.delete_chat_photo
        or m.group_chat_created
        or m.supergroup_chat_created
        or m.channel_chat_created
        or m.migrate_to_chat_id
        or m.migrate_from_chat_id
        or m.pinned_message
    )


async def _send_reply(msg: Message, text: str) -> None:
    """Send a reply; long texts go as a collapsible HTML blockquote.
    Telegram caps a message at 4096 chars, so texts longer than that are
    split into ~4000-char chunks on line boundaries. Empty text is never
    sent (Telegram rejects it) — a short fallback is used instead."""
    if not (text or "").strip():
        text = t("common.no_reply")
    if len(text) > LONG_REPLY_COLLAPSE_CHARS:
        # Split into chunks that fit Telegram's 4096-char cap (leave room
        # for the blockquote tags), preferring line boundaries.
        chunks: list[str] = []
        rest = text
        while len(rest) > 3900:
            cut = rest.rfind("\n", 0, 3900)
            if cut <= 0:
                cut = 3900
            chunks.append(rest[:cut])
            rest = rest[cut:].lstrip("\n")
        if rest:
            chunks.append(rest)
        for chunk in chunks:
            try:
                await msg.reply_text(
                    f"<blockquote expandable>{html.escape(chunk)}</blockquote>",
                    parse_mode="HTML",
                )
            except Exception:
                # HTML parsing failed (or the chunk is still too long):
                # fall back to plain text, split again if needed.
                for part in [
                    chunk[i : i + 4000] for i in range(0, len(chunk), 4000)
                ]:
                    await msg.reply_text(part)
        return
    await msg.reply_text(text)


class VortexBotHandlers:
    def __init__(
        self,
        settings: Settings,
        db: Database,
        dollar_service: DollarService,
        workspace_mgr: WorkspaceManager,
        file_processor: FileProcessor,
        llm_client: LLMClient,
        rate_limiter: RateLimiter,
    ) -> None:
        self.settings = settings
        self.db = db
        self.dollar_service = dollar_service
        self.workspace_mgr = workspace_mgr
        self.file_processor = file_processor
        self.llm_client = llm_client
        self.rate_limiter = rate_limiter
        # Wire the locale/country/wake-word providers to this bot's
        # settings + DB (DB values override the env defaults; see
        # bot/config.py). Language/country are read per call, so an
        # /admin change applies immediately. getattr() defaults keep
        # this working with settings objects that predate these fields.
        try:
            from bot.countries import set_country_provider
            from bot.locale import set_language_provider

            set_language_provider(
                lambda: self.db.get_language(
                    getattr(self.settings, "bot_language", "en") or "en"
                )
            )
            set_country_provider(
                lambda: self.db.get_country(
                    getattr(self.settings, "bot_country", "United States")
                    or "United States"
                )
            )
        except Exception:
            pass
        try:
            set_wake_word(getattr(self.settings, "bot_name", "Vortex") or "Vortex")
        except Exception:
            pass
        # Last image prompt per (chat, user), so a follow-up like
        # "انویدیا هم توی عکس بیار" can rebuild the full prompt
        # (previous prompt + the added element). Keyed by (chat, user) —
        # in a group one user's follow-up must never build on another
        # user's prompt — with a 10-minute TTL and a length cap, so a
        # stale prompt can't trigger false-positive images forever and
        # the stored prompt can't grow without bound. In-memory only:
        # a bot restart loses it and the follow-up falls back to
        # generating just the added element.
        self._last_image_prompt: dict[tuple[int, int], tuple[str, float]] = {}
        # Pending admin-panel input: boss user id -> {"action": "ban"|"unban"}
        # while the bot waits for a numeric user id after the boss tapped
        # "ban/unban by id" in /admin. In-memory only; a restart clears it.
        self._admin_pending: dict[int, dict] = {}
        # Admin "models of a key" browser state: boss user id -> {
        # "base_url", "key", "models" (filtered chat-model ids), "page",
        # "pending_model" (model picked but not yet activated)}.
        # In-memory only; a restart clears it.
        self._admin_models: dict[int, dict] = {}
        # Admin locale (🌐 Language & Country) country-browser state:
        # user id -> {"page": int}. In-memory only; a restart clears it.
        self._admin_locale: dict[int, dict] = {}

    def _get_last_image_prompt(self, chat_id: int, user_id: int) -> str | None:
        """The remembered image prompt for this (chat, user), or None
        when there is none or it is older than 10 minutes (stale
        entries are pruned)."""
        key = (chat_id, user_id)
        entry = self._last_image_prompt.get(key)
        if entry is None:
            return None
        prompt, when = entry
        if time.monotonic() - when > 600:
            self._last_image_prompt.pop(key, None)
            return None
        return prompt

    @staticmethod
    def _extract_attachment_info(msg: Message) -> tuple[str | None, str, int | None]:
        """
        Inspects a Telegram message for supported attachments (document or photo).
        Returns `(file_id, filename, file_size)`.
        """
        if msg.document:
            doc = msg.document
            fname = doc.file_name or "document.txt"
            return doc.file_id, fname, doc.file_size
        if msg.photo:
            # Pick highest resolution photo
            best_photo = msg.photo[-1]
            fname = f"photo_{best_photo.file_unique_id}.jpg"
            return best_photo.file_id, fname, best_photo.file_size
        if msg.voice:
            # Telegram voice note (.ogg Opus)
            return msg.voice.file_id, "voice.ogg", msg.voice.file_size
        if msg.audio:
            audio = msg.audio
            fname = audio.file_name or "audio.mp3"
            return audio.file_id, fname, audio.file_size
        if msg.video:
            video = msg.video
            fname = video.file_name or f"video_{video.file_unique_id}.mp4"
            return video.file_id, fname, video.file_size
        return None, "", None

    # ------------------------------------------------------------------
    # Hidden admin panel (/admin) — boss-only, PV-only.
    # ------------------------------------------------------------------

    def _admin_has_perm(self, user_id: int, perm: str) -> bool:
        """True when `user_id` may use an admin section: the boss always,
        a manager when the permission is in their stored set."""
        if user_id == self.settings.boss_id:
            return True
        return perm in self.db.get_manager_perms(user_id)

    async def _admin_require_perm(self, query, user_id: int, perm: str | None) -> bool:
        """Permission gate for one admin callback route. Returns True
        when allowed; when not, answers the refusal and returns False.
        perm None = anyone who can open the panel; 'boss' = boss only."""
        if perm is None:
            return True
        if perm == "boss":
            if user_id == self.settings.boss_id:
                return True
            await query.answer(t("common.not_boss"))
            return False
        if self._admin_has_perm(user_id, perm):
            return True
        await query.answer(t("common.no_access"))
        return False

    def _admin_menu_keyboard(self, user_id: int) -> InlineKeyboardMarkup:
        """The /admin main menu, filtered by the user's permissions.
        The boss sees everything (incl. managers + the power toggle);
        a manager sees only the sections their permissions open."""
        is_boss = user_id == self.settings.boss_id
        rows: list[list[InlineKeyboardButton]] = []
        for perm in ("tokens", "users", "stats", "chats", "image", "locale"):
            if self._admin_has_perm(user_id, perm):
                rows.append(
                    [InlineKeyboardButton(_perm_label(perm), callback_data=f"admin:{perm}")]
                )
        if is_boss:
            rows.append(
                [InlineKeyboardButton(t("admin.menu.managers"), callback_data="admin:managers")]
            )
        if self._admin_has_perm(user_id, "power"):
            state = (
                t("admin.menu.power_on")
                if self.db.is_bot_enabled()
                else t("admin.menu.power_off")
            )
            rows.append(
                [InlineKeyboardButton(state, callback_data="admin:power")]
            )
        if self._admin_has_perm(user_id, "tokens"):
            rows.append(
                [InlineKeyboardButton(t("admin.menu.health"), callback_data="admin:health")]
            )
        rows.append([InlineKeyboardButton(t("common.close"), callback_data="admin:close")])
        return InlineKeyboardMarkup(rows)

    @staticmethod
    def _admin_back_keyboard() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            [[InlineKeyboardButton(t("common.back"), callback_data="admin:menu")]]
        )

    @staticmethod
    def _admin_tokens_keyboard() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(t("admin.tokens.addkey"), callback_data="admin:addkey"),
                    InlineKeyboardButton(t("admin.tokens.removekey"), callback_data="admin:removekey"),
                ],
                [
                    InlineKeyboardButton(t("admin.tokens.pickkey"), callback_data="admin:pickkey"),
                    InlineKeyboardButton(t("admin.tokens.models"), callback_data="admin:models"),
                ],
                [
                    InlineKeyboardButton(t("admin.tokens.health"), callback_data="admin:health"),
                    InlineKeyboardButton(t("admin.tokens.recover"), callback_data="admin:recover"),
                ],
                [InlineKeyboardButton(t("common.back"), callback_data="admin:menu")],
            ]
        )

    def _admin_pick_keyboard(self) -> InlineKeyboardMarkup:
        """Buttons for picking the active entry: one per pool entry (⭐ on
        the active one), plus 'auto' (clear the manual selection, back to
        the pinned model / rotation), 'no model' (clear manual AND pinned:
        free rotation, no model selected at all) and back to the tokens
        view."""
        rows: list[list[InlineKeyboardButton]] = []
        active = self.llm_client.token_pool.active_entry
        for idx, e in enumerate(self.llm_client.token_pool.entries):
            host = urlparse(e.base_url).netloc or e.base_url
            mark = "⭐ " if active is not None and e == active else ""
            rows.append(
                [
                    InlineKeyboardButton(
                        f"{mark}{host} — {e.model}",
                        callback_data=f"admin:setactive:{idx}",
                    )
                ]
            )
        rows.append(
            [
                InlineKeyboardButton(
                    t("admin.pickkey.auto"), callback_data="admin:setactive:auto"
                )
            ]
        )
        rows.append(
            [
                InlineKeyboardButton(
                    t("admin.pickkey.none"), callback_data="admin:setactive:none"
                )
            ]
        )
        rows.append(
            [InlineKeyboardButton(t("admin.pickkey.back"), callback_data="admin:tokens")]
        )
        return InlineKeyboardMarkup(rows)

    def _admin_model_keys_keyboard(self) -> InlineKeyboardMarkup:
        """Buttons for the 'models of a key' browser: one per DISTINCT key
        in the pool (a key can serve several models, so entries are
        deduped by key)."""
        rows: list[list[InlineKeyboardButton]] = []
        for idx, (base_url, key) in enumerate(self._distinct_admin_keys()):
            host = urlparse(base_url).netloc or base_url
            fp = (key[:9] + "\u2026" + key[-4:]) if len(key) > 13 else key
            rows.append(
                [
                    InlineKeyboardButton(
                        f"{host} \u2014 {fp}",
                        callback_data=f"admin:models:{idx}",
                    )
                ]
            )
        rows.append(
            [InlineKeyboardButton(t("admin.pickkey.back"), callback_data="admin:tokens")]
        )
        return InlineKeyboardMarkup(rows)

    def _distinct_admin_keys(self) -> list[tuple[str, str]]:
        """Distinct (base_url, key) pairs in the pool, in pool order."""
        seen: set[tuple[str, str]] = set()
        out: list[tuple[str, str]] = []
        for e in self.llm_client.token_pool.entries:
            ident = (e.base_url, e.key)
            if ident not in seen:
                seen.add(ident)
                out.append(ident)
        return out

    def _admin_models_keyboard(self, user_id: int) -> InlineKeyboardMarkup:
        """One page of the models browser: up to 10 model buttons (\u2b50 on
        the active model of this key, \u2713 on models already in the pool),
        a prev/next row, and back to the keys list."""
        state = self._admin_models.get(user_id, {})
        models: list[str] = state.get("models", [])
        page: int = state.get("page", 0)
        base_url: str = state.get("base_url", "")
        key: str = state.get("key", "")
        pool = self.llm_client.token_pool
        active = pool.active_entry
        pool_models = {
            e.model for e in pool.entries if e.base_url == base_url and e.key == key
        }
        start = page * _ADMIN_MODELS_PER_PAGE
        rows: list[list[InlineKeyboardButton]] = []
        for i, model in enumerate(models[start:start + _ADMIN_MODELS_PER_PAGE]):
            if active is not None and active.base_url == base_url and active.model == model:
                mark = "\u2b50 "
            elif model in pool_models:
                mark = "\u2713 "
            else:
                mark = ""
            label = model if len(model) <= 45 else model[:44] + "\u2026"
            rows.append(
                [
                    InlineKeyboardButton(
                        mark + label,
                        callback_data=f"admin:model:{start + i}",
                    )
                ]
            )
        nav: list[InlineKeyboardButton] = []
        if page > 0:
            nav.append(InlineKeyboardButton(t("admin.models.prev"), callback_data="admin:models:prev"))
        total_pages = max(1, (len(models) + _ADMIN_MODELS_PER_PAGE - 1) // _ADMIN_MODELS_PER_PAGE)
        if page < total_pages - 1:
            nav.append(InlineKeyboardButton(t("admin.models.next"), callback_data="admin:models:next"))
        if nav:
            rows.append(nav)
        rows.append(
            [InlineKeyboardButton(t("admin.models.keys_back"), callback_data="admin:models")]
        )
        return InlineKeyboardMarkup(rows)

    def _persist_manual(self, base_url: str, model: str) -> tuple[bool, str]:
        """Write the boss's manual (base_url, model) selection to .env
        (LLM_MANUAL_SELECTION); empty values clear it. Returns
        (True, '') on success, (False, reason) on failure."""
        env_path = find_env_file()
        if env_path is None:
            return False, t("admin.env_missing")
        try:
            write_llm_manual_selection(env_path, base_url, model)
            return True, ""
        except Exception as exc:
            logger.warning("persist manual selection to .env failed: %s", type(exc).__name__)
            return False, type(exc).__name__

    def _persist_pinned(self, model: str) -> tuple[bool, str]:
        """Write the pinned model to .env (LLM_PINNED_MODEL); empty
        clears it. Returns (True, '') on success, (False, reason) on
        failure."""
        env_path = find_env_file()
        if env_path is None:
            return False, t("admin.env_missing")
        try:
            write_llm_pinned_model(env_path, model)
            return True, ""
        except Exception as exc:
            logger.warning("persist pinned model to .env failed: %s", type(exc).__name__)
            return False, type(exc).__name__

    def _build_admin_image_text(self) -> str:
        """Image-model section: the current choice is either the owner's
        own provider (base URL + API key + model, added in /admin) or
        off. There is no built-in image provider."""
        current = self.db.get_image_model()
        if current == "custom":
            provider = self.db.get_image_provider()
            if provider is not None:
                base_url, key, model = provider
                host = urlparse(base_url).netloc or base_url
                fp = (key[:9] + "\u2026" + key[-4:]) if len(key) > 13 else key
                current_line = t(
                    "admin.image.custom", host=host, model=model, fp=fp
                )
            else:
                current_line = t("admin.image.custom_unset")
        elif current == "none":
            current_line = t("admin.image.none")
        else:
            # Legacy stored value (e.g. a removed built-in provider):
            # treated as off.
            current_line = t("admin.image.none")
        return (
            t("admin.image.title")
            + "\n\n"
            + t("admin.image.current", current=current_line)
            + t("admin.image.pick")
        )

    def _admin_image_keyboard(self) -> InlineKeyboardMarkup:
        """Image section keyboard: add a custom service, set it, turn
        images off, or remove the custom service."""
        provider = self.db.get_image_provider()
        rows: list[list[InlineKeyboardButton]] = [
            [InlineKeyboardButton(t("admin.image.add_btn"), callback_data="admin:addimage")]
        ]
        if provider is not None:
            rows.append(
                [
                    InlineKeyboardButton(
                        t("admin.image.custom_btn"),
                        callback_data="admin:setimage:custom",
                    )
                ]
            )
            rows.append(
                [
                    InlineKeyboardButton(
                        t("admin.image.remove_btn"), callback_data="admin:removeimage"
                    )
                ]
            )
        else:
            rows.append(
                [
                    InlineKeyboardButton(
                        t("admin.image.custom_unset"), callback_data="admin:addimage"
                    )
                ]
            )
        rows.append(
            [InlineKeyboardButton(t("admin.image.off_btn"), callback_data="admin:setimage:none")]
        )
        rows.append(
            [InlineKeyboardButton(t("common.back"), callback_data="admin:menu")]
        )
        return InlineKeyboardMarkup(rows)

    def _build_admin_managers_text(self) -> str:
        """Managers list for the boss-only \U0001f6e1 Managers section."""
        managers = self.db.list_managers(limit=20)
        lines = [t("admin.managers.title")]
        if not managers:
            lines.append(t("admin.managers.empty"))
        for m in managers:
            perms = {p.strip() for p in (m.get("permissions") or "").split(",") if p.strip()}
            labels = ", ".join(_perm_label(p) for p in sorted(perms) if p in _ADMIN_PERMS) or t("admin.mgr.no_access")
            lines.append(f"\u2022 {m['user_id']} \u2014 {labels}")
        lines.append(t("admin.managers.hint"))
        return "\n".join(lines)

    def _admin_managers_keyboard(self) -> InlineKeyboardMarkup:
        rows: list[list[InlineKeyboardButton]] = []
        for m in self.db.list_managers(limit=20):
            rows.append(
                [
                    InlineKeyboardButton(
                        f"\U0001f6e1 {m['user_id']}",
                        callback_data=f"admin:mgr:{m['user_id']}",
                    )
                ]
            )
        rows.append(
            [InlineKeyboardButton(t("admin.managers.add"), callback_data="admin:mgradd")]
        )
        rows.append(
            [InlineKeyboardButton(t("common.back"), callback_data="admin:menu")]
        )
        return InlineKeyboardMarkup(rows)

    def _build_admin_manager_detail_text(self, target: int) -> str:
        """One manager's permissions (boss-only detail view)."""
        perms = self.db.get_manager_perms(target)
        lines = [t("admin.mgr.detail_title", id=target)]
        for perm in _ADMIN_PERMS:
            lines.append(f"{'\u2705' if perm in perms else '\u274c'} {_perm_label(perm)}")
        lines.append(t("admin.mgr.detail_hint"))
        return "\n".join(lines)

    def _admin_manager_detail_keyboard(self, target: int) -> InlineKeyboardMarkup:
        perms = self.db.get_manager_perms(target)
        rows: list[list[InlineKeyboardButton]] = []
        for perm in _ADMIN_PERMS:
            mark = "\u2705 " if perm in perms else "\u274c "
            rows.append(
                [
                    InlineKeyboardButton(
                        mark + _perm_label(perm),
                        callback_data=f"admin:mgrtoggle:{target}:{perm}",
                    )
                ]
            )
        rows.append(
            [
                InlineKeyboardButton(
                    t("admin.mgr.remove"), callback_data=f"admin:mgrremove:{target}"
                )
            ]
        )
        rows.append(
            [InlineKeyboardButton(t("admin.mgr.back"), callback_data="admin:managers")]
        )
        return InlineKeyboardMarkup(rows)

    async def _render_admin_models(self, query, user_id: int) -> None:
        """Re-render the models browser message for the current page."""
        state = self._admin_models.get(user_id, {})
        models: list[str] = state.get("models", [])
        page: int = state.get("page", 0)
        total_pages = max(1, (len(models) + _ADMIN_MODELS_PER_PAGE - 1) // _ADMIN_MODELS_PER_PAGE)
        page = max(0, min(page, total_pages - 1))
        state["page"] = page
        host = urlparse(state.get("base_url", "")).netloc or state.get("base_url", "")
        await query.edit_message_text(
            t(
                "admin.models.title",
                host=host,
                count=len(models),
                page=page + 1,
                pages=total_pages,
            ),
            reply_markup=self._admin_models_keyboard(user_id),
        )

    async def _activate_admin_model(self, query, user_id: int, model: str) -> None:
        """Activate `model` on the key the boss is browsing: add a pool
        entry when needed (persisted to .env), set the manual selection
        (persisted), and show the tokens view."""
        state = self._admin_models.get(user_id, {})
        base_url: str = state.get("base_url", "")
        key: str = state.get("key", "")
        pool = self.llm_client.token_pool
        if not base_url or not key or not model:
            await query.answer(t("common.incomplete"))
            return
        exists = any(
            e.base_url == base_url and e.key == key and e.model == model
            for e in pool.entries
        )
        if not exists:
            added = await pool.add_entry(
                ProviderEntry(base_url=base_url, key=key, model=model)
            )
            if not added:
                await query.answer(t("admin.model.add_failed"))
                return
            self._persist_pool()
        active = await pool.set_manual_selection(base_url, model)
        persisted, err = self._persist_manual(base_url, model)
        if active is not None and active.base_url == base_url and active.model == model:
            toast = t("admin.model.activated", model=model)
        else:
            toast = t("admin.model.unhealthy", model=model)
        await query.answer(toast)
        await query.edit_message_text(
            self._build_admin_tokens_text()
            + (t("admin.model.save_warn") if not persisted else ""),
            reply_markup=self._admin_tokens_keyboard(),
        )
        self._admin_models.pop(user_id, None)

    @staticmethod
    def _admin_addkey_keyboard() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("NVIDIA", callback_data="admin:addkey:nvidia")],
                [InlineKeyboardButton("TokenHarbor", callback_data="admin:addkey:tokenharbor")],
                [InlineKeyboardButton("HiLinkUp", callback_data="admin:addkey:hilinkup")],
                [
                    InlineKeyboardButton(
                        t("admin.addkey.custom"),
                        callback_data="admin:addkey:custom",
                    )
                ],
                [InlineKeyboardButton(t("common.back"), callback_data="admin:menu")],
            ]
        )

    def _admin_remove_keyboard(self) -> InlineKeyboardMarkup:
        rows: list[list[InlineKeyboardButton]] = []
        for idx, e in enumerate(self.llm_client.token_pool.describe_entries()):
            host = urlparse(e["base_url"]).netloc or e["base_url"]
            rows.append(
                [
                    InlineKeyboardButton(
                        f"{host} \u2014 {e['model']} \u2014 {e['key_fp']}",
                        callback_data=f"admin:rm:{idx}",
                    )
                ]
            )
        rows.append(
            [InlineKeyboardButton(t("common.back"), callback_data="admin:menu")]
        )
        return InlineKeyboardMarkup(rows)

    @staticmethod
    def _admin_users_keyboard() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(t("admin.users.ban"), callback_data="admin:ban"),
                    InlineKeyboardButton(t("admin.users.unban"), callback_data="admin:unban"),
                ],
                [
                    InlineKeyboardButton(t("admin.users.allow"), callback_data="admin:allow"),
                    InlineKeyboardButton(t("admin.users.unallow"), callback_data="admin:unallow"),
                ],
                [InlineKeyboardButton(t("common.back"), callback_data="admin:menu")],
            ]
        )

    def _persist_pool(self) -> tuple[bool, str]:
        """Write the live token pool back to .env (LLM_PROVIDERS) so an
        add/remove survives a restart. Returns (True, '') on success,
        (False, reason) on failure — in that case the in-memory change
        still applies, but a restart would revert it."""
        env_path = find_env_file()
        if env_path is None:
            return False, t("admin.env_missing")
        try:
            write_llm_providers(
                env_path, list(self.llm_client.token_pool.entries)
            )
            return True, ""
        except Exception as exc:
            logger.warning("persist pool to .env failed: %s", type(exc).__name__)
            return False, type(exc).__name__

    def _build_admin_tokens_text(self) -> str:
        """Boss-only token pool status: per entry the provider host,
        model, status and the active marker. Keys appear only as a
        masked fingerprint (first 9 + last 4 chars), never in full."""
        pool = self.llm_client.token_pool
        lines: list[str] = [t("admin.tokens.title"), ""]
        lines.append(t("admin.tokens.active", label=self.llm_client.describe_active_model()))
        manual = pool.manual_selection
        if manual is not None:
            lines.append(t("admin.tokens.mode_manual", model=manual[1]))
        elif getattr(pool, "_pinned_model", ""):
            lines.append(t("admin.tokens.mode_pinned", model=pool._pinned_model))
        else:
            lines.append(t("admin.tokens.mode_none"))
        lines.append(
            t(
                "admin.tokens.healthy_count",
                n=_num(len(pool.healthy_entries)),
                total=_num(len(pool.entries)),
            )
        )
        lines.append("")
        status_keys = {
            "healthy": "admin.tokens.status_healthy",
            "cooldown": "admin.tokens.status_cooldown",
            "quarantined": "admin.tokens.status_quarantined",
        }
        for e in pool.describe_entries():
            host = urlparse(e["base_url"]).netloc or e["base_url"]
            active = t("admin.tokens.active_mark") if e["active"] else ""
            lines.append(f"• {host} — {e['model']}{active}")
            status = (
                t(status_keys[e["status"]])
                if e["status"] in status_keys
                else e["status"]
            )
            lines.append(t("admin.tokens.entry", status=status, fp=e["key_fp"]))
        return "\n".join(lines)

    def _build_admin_users_text(self) -> str:
        """Boss-only user overview: total members, groups, banned users
        (most recent first), the private-mode allowlist, and a hint that
        ban/unban/allowlist by id lives on the buttons below."""
        lines: list[str] = [t("admin.users.title"), ""]
        lines.append(
            t(
                "admin.users.bot_state",
                state=(
                    t("admin.users.bot_on") if self.db.is_bot_enabled() else t("admin.users.bot_off")
                ),
            )
        )
        lines.append(t("admin.users.members", n=_num(self.db.count_all_members())))
        lines.append(t("admin.users.groups", n=_num(len(self.db.list_known_groups()))))
        banned = self.db.list_banned_users(limit=20)
        lines.append(t("admin.users.banned_count", n=_num(len(banned))))
        for b in banned:
            scope = (
                t("admin.users.scope_global")
                if b["chat_id"] == GLOBAL_CHAT_ID
                else t("admin.users.scope_chat", id=b["chat_id"])
            )
            when = _local_stamp(b["banned_at"]) if b.get("banned_at") else ""
            lines.append(t("admin.users.banned_row", id=b["user_id"], scope=scope, when=when))
        allowed = self.db.list_allowlist(limit=20)
        lines.append(t("admin.users.allowed_count", n=_num(len(allowed))))
        for a in allowed:
            lines.append(t("admin.users.allowed_row", id=a["user_id"]))
        lines.append("")
        lines.append(t("admin.users.foot"))
        return "\n".join(lines)

    async def _admin_show_text(
        self,
        query,
        text: str,
        reply_markup: InlineKeyboardMarkup,
    ) -> None:
        """Show a panel section by editing the menu message. Long texts
        (stats / chat history) can exceed Telegram's 4096-char edit cap,
        so those are sent as a new message instead and the menu stays."""
        if len(text) <= 3900:
            try:
                await query.edit_message_text(text, reply_markup=reply_markup)
                return
            except Exception:
                pass
        # Too long to edit (or the edit failed): send as a new message.
        if query.message is not None:
            await _send_reply(query.message, text)
            try:
                await query.answer()
            except Exception:
                pass

    def _build_admin_locale_text(self) -> str:
        """🌐 Language & Country section: the current country and
        language, plus what the country drives (timezone, currency,
        prayer-time city). Language buttons and the country browser live
        on the keyboard below."""
        country = current_country()
        lang = current_language()
        return t(
            "admin.locale.text",
            country=country.name,
            language=LANGUAGES.get(lang, lang),
            timezone=country.timezone,
            currency=country.currency,
            capital=country.capital,
        )

    def _admin_locale_keyboard(self) -> InlineKeyboardMarkup:
        """Language buttons (the 40 UI languages, 2 per row, ✓ on the
        current one) plus a button that opens the country browser."""
        lang = current_language()
        rows: list[list[InlineKeyboardButton]] = []
        codes = list(UI_LANGUAGES)
        for i in range(0, len(codes), 2):
            row = []
            for code in codes[i : i + 2]:
                mark = "✓ " if code == lang else ""
                row.append(
                    InlineKeyboardButton(
                        mark + LANGUAGES[code],
                        callback_data=f"admin:setlang:{code}",
                    )
                )
            rows.append(row)
        rows.append(
            [
                InlineKeyboardButton(
                    t("admin.locale.countries_btn"), callback_data="admin:countries"
                )
            ]
        )
        rows.append(
            [InlineKeyboardButton(t("common.back"), callback_data="admin:menu")]
        )
        return InlineKeyboardMarkup(rows)

    def _admin_countries_text(self, user_id: int) -> str:
        """Title of the country browser with the current page number."""
        names = list_country_names()
        total_pages = max(1, (len(names) + 9) // 10)
        state = self._admin_locale.setdefault(user_id, {"page": 0})
        page = max(0, min(total_pages - 1, state.get("page", 0)))
        return t("admin.locale.countries_title", page=page + 1, pages=total_pages)

    def _admin_countries_keyboard(self, user_id: int) -> InlineKeyboardMarkup:
        """Country browser: 10 countries per page (like the models
        browser), ✓ on the current country, prev/next navigation."""
        names = list_country_names()
        state = self._admin_locale.setdefault(user_id, {"page": 0})
        total_pages = max(1, (len(names) + 9) // 10)
        page = max(0, min(total_pages - 1, state.get("page", 0)))
        state["page"] = page
        current = current_country().name
        rows: list[list[InlineKeyboardButton]] = []
        for name in names[page * 10 : (page + 1) * 10]:
            mark = "✓ " if name == current else ""
            rows.append(
                [
                    InlineKeyboardButton(
                        mark + name, callback_data=f"admin:setcountry:{name}"
                    )
                ]
            )
        nav: list[InlineKeyboardButton] = []
        if page > 0:
            nav.append(
                InlineKeyboardButton(
                    t("admin.models.prev"), callback_data="admin:countries:prev"
                )
            )
        if page < total_pages - 1:
            nav.append(
                InlineKeyboardButton(
                    t("admin.models.next"), callback_data="admin:countries:next"
                )
            )
        if nav:
            rows.append(nav)
        rows.append(
            [
                InlineKeyboardButton(
                    t("admin.locale.back"), callback_data="admin:locale"
                )
            ]
        )
        return InlineKeyboardMarkup(rows)

    async def _handle_admin_callback(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Routes every 'admin:*' inline-button press. The boss may do
        everything; a manager may use only the sections their stored
        permissions open (each route checks its permission from
        _ADMIN_ROUTE_PERMS). Any other user pressing an admin button gets
        a refusal. The menu edits itself in place; 'back' returns to the
        main panel and clears any pending input."""
        query = update.callback_query
        if not query or not query.data:
            return
        user = query.from_user
        if not user or user.is_bot:
            return
        is_boss = user.id == self.settings.boss_id
        if not is_boss and not self.db.is_manager(user.id):
            await query.answer(t("common.not_boss"))
            return
        if query.message is None:
            await query.answer(t("admin.panel_not_found"))
            return
        data = query.data
        # Route key = the part after "admin:" up to the next ":" (e.g.
        # "setactive" for "admin:setactive:2"); each route needs its
        # permission from _ADMIN_ROUTE_PERMS.
        route = data[len("admin:"):].split(":", 1)[0]
        if not await self._admin_require_perm(
            query, user.id, _ADMIN_ROUTE_PERMS.get(route)
        ):
            return
        try:
            if data == "admin:menu":
                self._admin_pending.pop(user.id, None)
                await query.edit_message_text(
                    _admin_menu_text(), reply_markup=self._admin_menu_keyboard(user.id)
                )
            elif data == "admin:tokens":
                await query.edit_message_text(
                    self._build_admin_tokens_text(),
                    reply_markup=self._admin_tokens_keyboard(),
                )
            elif data == "admin:users":
                await query.edit_message_text(
                    self._build_admin_users_text(),
                    reply_markup=self._admin_users_keyboard(),
                )
            elif data == "admin:stats":
                await self._admin_show_text(
                    query,
                    await self._build_stats_text(context),
                    self._admin_back_keyboard(),
                )
            elif data == "admin:chats":
                await self._admin_show_text(
                    query,
                    self._build_chat_history_text(),
                    self._admin_back_keyboard(),
                )
            elif data == "admin:health":
                await query.answer(t("admin.health.checking"))
                await self.llm_client.token_pool.health_check()
                await query.edit_message_text(
                    self._build_admin_tokens_text(),
                    reply_markup=self._admin_tokens_keyboard(),
                )
            elif data == "admin:recover":
                await query.answer(t("admin.tokens.recovering"))
                await self.llm_client.token_pool.retry_dead()
                await query.edit_message_text(
                    self._build_admin_tokens_text(),
                    reply_markup=self._admin_tokens_keyboard(),
                )
            elif data == "admin:addkey":
                await query.edit_message_text(
                    t("admin.addkey.which"),
                    reply_markup=self._admin_addkey_keyboard(),
                )
            elif data.startswith("admin:addkey:"):
                provider = data.split(":", 2)[2]
                if provider == "custom":
                    self._admin_pending[user.id] = {
                        "action": "addkey",
                        "step": "base_url",
                    }
                    await query.edit_message_text(
                        t("admin.addkey.base_url"),
                        reply_markup=self._admin_back_keyboard(),
                    )
                elif provider in _ADMIN_PROVIDERS:
                    label, base_url, example_model = _ADMIN_PROVIDERS[provider]
                    self._admin_pending[user.id] = {
                        "action": "addkey",
                        "step": "model",
                        "base_url": base_url,
                    }
                    await query.edit_message_text(
                        t("admin.addkey.model", label=label, example=example_model),
                        reply_markup=self._admin_back_keyboard(),
                    )
                else:
                    await query.answer(t("admin.addkey.invalid_service"))
            elif data == "admin:removekey":
                if len(self.llm_client.token_pool.entries) <= 1:
                    await query.answer(
                        t("admin.removekey.last"),
                        show_alert=True,
                    )
                else:
                    await query.edit_message_text(
                        t("admin.removekey.which"),
                        reply_markup=self._admin_remove_keyboard(),
                    )
            elif data.startswith("admin:rm:"):
                try:
                    idx = int(data.split(":", 2)[2])
                except ValueError:
                    await query.answer(t("common.invalid_button"))
                    return
                entries = self.llm_client.token_pool.describe_entries()
                if idx < 0 or idx >= len(entries):
                    await query.answer(t("admin.key_gone"))
                    return
                e = entries[idx]
                host = urlparse(e["base_url"]).netloc or e["base_url"]
                await query.edit_message_text(
                    t(
                        "admin.removekey.confirm",
                        host=host,
                        model=e['model'],
                        fp=e['key_fp'],
                        status=e['status'],
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    t("common.confirm_yes"),
                                    callback_data=f"admin:rmconfirm:{idx}",
                                ),
                                InlineKeyboardButton(
                                    t("common.confirm_no"), callback_data="admin:tokens"
                                ),
                            ]
                        ]
                    ),
                )
            elif data.startswith("admin:rmconfirm:"):
                try:
                    idx = int(data.split(":", 2)[2])
                except ValueError:
                    await query.answer(t("common.invalid_button"))
                    return
                entries = self.llm_client.token_pool.entries
                if idx < 0 or idx >= len(entries):
                    await query.answer(t("admin.key_gone"))
                    return
                if len(entries) <= 1:
                    await query.answer(
                        t("admin.removekey.last"),
                        show_alert=True,
                    )
                    return
                entry = entries[idx]
                removed = await self.llm_client.token_pool.remove_entry(entry.key)
                if not removed:
                    await query.answer(t("admin.key_not_found"))
                    return
                persisted, err = self._persist_pool()
                await query.answer(
                    t("admin.key_removed")
                    if persisted
                    else t("admin.key_removed_nosave", err=err)
                )
                await query.edit_message_text(
                    self._build_admin_tokens_text(),
                    reply_markup=self._admin_tokens_keyboard(),
                )
            elif data == "admin:pickkey":
                await query.edit_message_text(
                    t("admin.pickkey.which"),
                    reply_markup=self._admin_pick_keyboard(),
                )
            elif data.startswith("admin:setactive:"):
                which = data.split(":", 2)[2]
                if which == "auto":
                    active = await self.llm_client.token_pool.clear_manual_selection()
                    persisted, err = self._persist_manual("", "")
                    await query.answer(
                        t("admin.pickkey.auto_done")
                        if persisted
                        else t("admin.pickkey.auto_nosave", err=err)
                    )
                    await query.edit_message_text(
                        self._build_admin_tokens_text(),
                        reply_markup=self._admin_tokens_keyboard(),
                    )
                    return
                if which == "none":
                    # No model selected at all: clear the manual selection
                    # AND the pinned model -> free rotation among healthy
                    # entries. Both are persisted to .env.
                    await self.llm_client.token_pool.clear_manual_selection()
                    await self.llm_client.token_pool.set_pinned_model("")
                    ok1, err1 = self._persist_manual("", "")
                    ok2, err2 = self._persist_pinned("")
                    await query.answer(
                        t("admin.pickkey.none_done")
                        if ok1 and ok2
                        else t("admin.pickkey.none_nosave", err=err1 or err2)
                    )
                    await query.edit_message_text(
                        self._build_admin_tokens_text(),
                        reply_markup=self._admin_tokens_keyboard(),
                    )
                    return
                try:
                    idx = int(which)
                except ValueError:
                    await query.answer(t("common.invalid_button"))
                    return
                entries = self.llm_client.token_pool.entries
                if idx < 0 or idx >= len(entries):
                    await query.answer(t("admin.key_gone"))
                    return
                entry = entries[idx]
                active = await self.llm_client.token_pool.set_manual_selection(
                    entry.base_url, entry.model
                )
                persisted, err = self._persist_manual(entry.base_url, entry.model)
                if active is not None and active == entry:
                    toast = t("admin.pickkey.activated", model=entry.model)
                else:
                    toast = t("admin.pickkey.unhealthy")
                await query.answer(
                    toast if persisted else toast + t("admin.pickkey.nosave", err=err)
                )
                await query.edit_message_text(
                    self._build_admin_tokens_text(),
                    reply_markup=self._admin_tokens_keyboard(),
                )
            elif data == "admin:models":
                await query.edit_message_text(
                    t("admin.models.which_key"),
                    reply_markup=self._admin_model_keys_keyboard(),
                )
            elif data.startswith("admin:models:"):
                which = data.split(":", 2)[2]
                if which in ("prev", "next"):
                    state = self._admin_models.get(user.id)
                    if not state:
                        await query.answer(t("common.start_over"))
                        return
                    total_pages = max(
                        1,
                        (len(state.get("models", [])) + _ADMIN_MODELS_PER_PAGE - 1)
                        // _ADMIN_MODELS_PER_PAGE,
                    )
                    if which == "prev":
                        state["page"] = max(0, state.get("page", 0) - 1)
                    else:
                        state["page"] = min(total_pages - 1, state.get("page", 0) + 1)
                    await self._render_admin_models(query, user.id)
                    return
                try:
                    idx = int(which)
                except ValueError:
                    await query.answer(t("common.invalid_button"))
                    return
                keys = self._distinct_admin_keys()
                if idx < 0 or idx >= len(keys):
                    await query.answer(t("admin.key_gone"))
                    return
                base_url, key = keys[idx]
                await query.answer(t("admin.models.fetching"))
                raw = await TokenPool.list_models(base_url, key)
                models = [
                    m
                    for m in raw
                    if not any(h in m.lower() for h in _ADMIN_NON_CHAT_MODEL_HINTS)
                ]
                if not models:
                    await query.edit_message_text(
                        t("admin.models.none"),
                        reply_markup=self._admin_model_keys_keyboard(),
                    )
                    return
                self._admin_models[user.id] = {
                    "base_url": base_url,
                    "key": key,
                    "models": models,
                    "page": 0,
                }
                await self._render_admin_models(query, user.id)
            elif data.startswith("admin:model:"):
                state = self._admin_models.get(user.id)
                if not state:
                    await query.answer(t("common.start_over"))
                    return
                try:
                    idx = int(data.split(":", 2)[2])
                except ValueError:
                    await query.answer(t("common.invalid_button"))
                    return
                models: list[str] = state.get("models", [])
                if idx < 0 or idx >= len(models):
                    await query.answer(t("admin.model_gone"))
                    return
                model = models[idx]
                await query.answer(t("admin.model.probing"))
                ok = await TokenPool.probe_model(
                    state["base_url"], state["key"], model
                )
                if ok:
                    await self._activate_admin_model(query, user.id, model)
                else:
                    state["pending_model"] = model
                    await query.edit_message_text(
                        t("admin.model.no_reply", model=model),
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        t("admin.model.force_yes"),
                                        callback_data="admin:modelforce",
                                    ),
                                    InlineKeyboardButton(
                                        t("common.no"), callback_data="admin:models"
                                    ),
                                ]
                            ]
                        ),
                    )
            elif data == "admin:modelforce":
                state = self._admin_models.get(user.id)
                model = (state or {}).get("pending_model", "")
                if not model:
                    await query.answer(t("common.start_over"))
                    return
                await self._activate_admin_model(query, user.id, model)
            elif data == "admin:ban":
                self._admin_pending[user.id] = {"action": "ban"}
                await query.edit_message_text(
                    t("admin.ban.prompt"),
                    reply_markup=self._admin_back_keyboard(),
                )
            elif data == "admin:unban":
                self._admin_pending[user.id] = {"action": "unban"}
                await query.edit_message_text(
                    t("admin.unban.prompt"),
                    reply_markup=self._admin_back_keyboard(),
                )
            elif data == "admin:power":
                enabled = not self.db.is_bot_enabled()
                self.db.set_bot_enabled(enabled)
                await query.answer(
                    t("admin.power.on") if enabled else t("admin.power.off")
                )
                await query.edit_message_text(
                    _admin_menu_text(), reply_markup=self._admin_menu_keyboard(user.id)
                )
            elif data == "admin:image":
                await query.edit_message_text(
                    self._build_admin_image_text(),
                    reply_markup=self._admin_image_keyboard(),
                )
            elif data.startswith("admin:setimage:"):
                which = data.split(":", 2)[2]
                if which == "none":
                    self.db.set_image_model("none")
                    await query.answer(t("admin.image.set_off"))
                    await query.edit_message_text(
                        self._build_admin_image_text(),
                        reply_markup=self._admin_image_keyboard(),
                    )
                elif which == "custom":
                    if self.db.get_image_provider() is None:
                        await query.answer(t("admin.image.custom_unset_alert"), show_alert=True)
                        return
                    self.db.set_image_model("custom")
                    await query.answer(t("admin.image.set_custom"))
                    await query.edit_message_text(
                        self._build_admin_image_text(),
                        reply_markup=self._admin_image_keyboard(),
                    )
                else:
                    await query.answer(t("common.invalid_button"))
            elif data == "admin:addimage":
                self._admin_pending[user.id] = {
                    "action": "addimage",
                    "step": "base_url",
                }
                await query.edit_message_text(
                    t("admin.addimage.base_url"),
                    reply_markup=self._admin_back_keyboard(),
                )
            elif data == "admin:removeimage":
                if self.db.get_image_provider() is None:
                    await query.answer(t("admin.image.custom_unset_alert"))
                    return
                self.db.clear_image_provider()
                if self.db.get_image_model() == "custom":
                    self.db.set_image_model("none")
                await query.answer(t("admin.image.removed"))
                await query.edit_message_text(
                    self._build_admin_image_text(),
                    reply_markup=self._admin_image_keyboard(),
                )
            elif data == "admin:managers":
                await query.edit_message_text(
                    self._build_admin_managers_text(),
                    reply_markup=self._admin_managers_keyboard(),
                )
            elif data == "admin:mgradd":
                self._admin_pending[user.id] = {"action": "mgradd"}
                await query.edit_message_text(
                    t("admin.mgr.add_prompt"),
                    reply_markup=self._admin_back_keyboard(),
                )
            elif data.startswith("admin:mgr:"):
                try:
                    target = int(data.split(":", 2)[2])
                except ValueError:
                    await query.answer(t("common.invalid_button"))
                    return
                if not self.db.is_manager(target):
                    await query.answer(t("admin.mgr.gone"))
                    return
                await query.edit_message_text(
                    self._build_admin_manager_detail_text(target),
                    reply_markup=self._admin_manager_detail_keyboard(target),
                )
            elif data.startswith("admin:mgrtoggle:"):
                parts = data.split(":", 3)
                if len(parts) != 4:
                    await query.answer(t("common.invalid_button"))
                    return
                try:
                    target = int(parts[2])
                except ValueError:
                    await query.answer(t("common.invalid_button"))
                    return
                perm = parts[3]
                if perm not in _ADMIN_PERMS:
                    await query.answer(t("admin.mgr.invalid_perm"))
                    return
                if not self.db.is_manager(target):
                    await query.answer(t("admin.mgr.gone"))
                    return
                perms = self.db.get_manager_perms(target)
                if perm in perms:
                    perms.discard(perm)
                else:
                    perms.add(perm)
                self.db.set_manager_perms(target, perms)
                await query.answer(
                    t(
                        "admin.mgr.perm_toggled",
                        label=_perm_label(perm),
                        state=(
                            t("admin.mgr.perm_on") if perm in perms else t("admin.mgr.perm_off")
                        ),
                    )
                )
                await query.edit_message_text(
                    self._build_admin_manager_detail_text(target),
                    reply_markup=self._admin_manager_detail_keyboard(target),
                )
            elif data.startswith("admin:mgrremove:"):
                try:
                    target = int(data.split(":", 2)[2])
                except ValueError:
                    await query.answer(t("common.invalid_button"))
                    return
                if not self.db.is_manager(target):
                    await query.answer(t("admin.mgr.gone"))
                    return
                await query.edit_message_text(
                    t("admin.mgr.remove_confirm", id=target),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    t("common.confirm_yes"),
                                    callback_data=f"admin:mgrremoveconfirm:{target}",
                                ),
                                InlineKeyboardButton(
                                    t("common.confirm_no"), callback_data=f"admin:mgr:{target}"
                                ),
                            ]
                        ]
                    ),
                )
            elif data.startswith("admin:mgrremoveconfirm:"):
                try:
                    target = int(data.split(":", 2)[2])
                except ValueError:
                    await query.answer(t("common.invalid_button"))
                    return
                if self.db.remove_manager(target):
                    await query.answer(t("admin.mgr.removed"))
                else:
                    await query.answer(t("admin.mgr.not_manager"))
                await query.edit_message_text(
                    self._build_admin_managers_text(),
                    reply_markup=self._admin_managers_keyboard(),
                )
            elif data == "admin:allow":
                self._admin_pending[user.id] = {"action": "allow"}
                await query.edit_message_text(
                    t("admin.allow.prompt"),
                    reply_markup=self._admin_back_keyboard(),
                )
            elif data == "admin:unallow":
                self._admin_pending[user.id] = {"action": "unallow"}
                await query.edit_message_text(
                    t("admin.unallow.prompt"),
                    reply_markup=self._admin_back_keyboard(),
                )
            elif data == "admin:locale":
                await query.edit_message_text(
                    self._build_admin_locale_text(),
                    reply_markup=self._admin_locale_keyboard(),
                )
            elif data.startswith("admin:setlang:"):
                code = data.split(":", 2)[2]
                if code not in LANGUAGES:
                    await query.answer(t("common.invalid_button"))
                    return
                self.db.set_language(code)
                await query.answer(
                    t("admin.locale.lang_set", language=LANGUAGES[code])
                )
                await query.edit_message_text(
                    self._build_admin_locale_text(),
                    reply_markup=self._admin_locale_keyboard(),
                )
            elif data == "admin:countries":
                self._admin_locale[user.id] = {"page": 0}
                await query.edit_message_text(
                    self._admin_countries_text(user.id),
                    reply_markup=self._admin_countries_keyboard(user.id),
                )
            elif data.startswith("admin:countries:"):
                which = data.split(":", 2)[2]
                state = self._admin_locale.setdefault(user.id, {"page": 0})
                if which == "prev":
                    state["page"] = max(0, state.get("page", 0) - 1)
                elif which == "next":
                    state["page"] = state.get("page", 0) + 1
                else:
                    await query.answer(t("common.invalid_button"))
                    return
                await query.edit_message_text(
                    self._admin_countries_text(user.id),
                    reply_markup=self._admin_countries_keyboard(user.id),
                )
            elif data.startswith("admin:setcountry:"):
                name = data.split(":", 2)[2]
                country = get_country(name)
                if country is None:
                    await query.answer(t("common.invalid_button"))
                    return
                self.db.set_country(country.name)
                await query.answer(
                    t("admin.locale.country_set", country=country.name)
                )
                await query.edit_message_text(
                    self._build_admin_locale_text(),
                    reply_markup=self._admin_locale_keyboard(),
                )
            elif data == "admin:close":
                self._admin_pending.pop(user.id, None)
                try:
                    await query.delete_message()
                except Exception:
                    pass
            else:
                await query.answer(t("common.invalid_button"))
        except Exception as exc:
            logger.warning("admin callback %s failed: %s", data, type(exc).__name__)
            try:
                await query.answer(t("common.error_retry"))
            except Exception:
                pass

    async def _handle_admin_pending_input(
        self, msg: Message, user_id: int, text: str
    ) -> bool:
        """Handles the boss's (or a permitted manager's) reply while /admin
        waits for input: a numeric user id (ban/unban by id, allowlist
        add/remove, add manager) or the steps of adding a key (base URL ->
        model -> key). Returns True when the message was consumed as admin
        input (or cancelled); False when there was no pending input or the
        text is not admin input, so normal handling continues. Ban/unban
        here is GLOBAL (whole bot)."""
        pending = self._admin_pending.get(user_id)
        if not pending:
            return False
        action = pending.get("action")
        if action == "addkey":
            if not self._admin_has_perm(user_id, "tokens"):
                self._admin_pending.pop(user_id, None)
                await msg.reply_text(t("common.no_access"))
                return True
            return await self._handle_addkey_input(msg, user_id, pending, text)
        if action == "addimage":
            if not self._admin_has_perm(user_id, "image"):
                self._admin_pending.pop(user_id, None)
                await msg.reply_text(t("common.no_access"))
                return True
            return await self._handle_addimage_input(msg, user_id, pending, text)
        if action not in ("ban", "unban", "allow", "unallow", "mgradd"):
            self._admin_pending.pop(user_id, None)
            return False
        # Permission for the pending action: ban/unban/allow/unallow need
        # 'users'; adding a manager is boss-only.
        if action in ("ban", "unban", "allow", "unallow"):
            if not self._admin_has_perm(user_id, "users"):
                self._admin_pending.pop(user_id, None)
                await msg.reply_text(t("common.no_access"))
                return True
        elif action == "mgradd" and user_id != self.settings.boss_id:
            self._admin_pending.pop(user_id, None)
            await msg.reply_text(t("common.not_boss"))
            return True
        stripped = (text or "").strip()
        if stripped in ("لغو", "cancel", "/cancel"):
            self._admin_pending.pop(user_id, None)
            await msg.reply_text(t("common.cancelled"))
            return True
        if not stripped.isdigit():
            # Not an id and not cancel: drop the pending state and let
            # the message flow normally so the boss can still chat.
            self._admin_pending.pop(user_id, None)
            return False
        target_id = int(stripped)
        if action == "ban" and target_id == self.settings.boss_id:
            await msg.reply_text(t("ban.self"))
            self._admin_pending.pop(user_id, None)
            return True
        if action == "ban":
            newly = self.db.ban_user(
                chat_id=msg.chat.id,
                target_user_id=target_id,
                actor_id=user_id,
                global_ban=True,
            )
            await msg.reply_text(
                random.choice(t_list("ban.done")) + t("ban.global_suffix")
                if newly
                else t("ban.already_global")
            )
        elif action == "unban":
            removed = self.db.unban_user(
                chat_id=msg.chat.id,
                target_user_id=target_id,
                actor_id=user_id,
                global_ban=True,
            )
            await msg.reply_text(
                random.choice(t_list("unban.done")) + t("ban.global_suffix")
                if removed
                else t("unban.not_banned_global")
            )
        elif action == "allow":
            if self.db.add_to_allowlist(target_id, user_id):
                await msg.reply_text(t("admin.allow.added", id=target_id))
            else:
                await msg.reply_text(t("admin.allow.already"))
        elif action == "unallow":
            if self.db.remove_from_allowlist(target_id):
                await msg.reply_text(t("admin.unallow.removed", id=target_id))
            else:
                await msg.reply_text(t("admin.unallow.missing"))
        elif action == "mgradd":
            if target_id == self.settings.boss_id:
                await msg.reply_text(t("admin.mgr.is_boss"))
            elif self.db.add_manager(target_id, user_id):
                await msg.reply_text(
                    t("admin.mgr.added", id=target_id),
                )
                # Show the new manager's detail view right away so the
                # boss can toggle permissions immediately.
                await msg.reply_text(
                    self._build_admin_manager_detail_text(target_id),
                    reply_markup=self._admin_manager_detail_keyboard(target_id),
                )
            else:
                await msg.reply_text(t("admin.mgr.already"))
        self._admin_pending.pop(user_id, None)
        return True

    async def _handle_addkey_input(
        self, msg: Message, user_id: int, pending: dict, text: str
    ) -> bool:
        """One step of the /admin 'add key' flow: base_url -> model -> key.
        The key is validated live (GET {base_url}/models) before it joins
        the pool, then the pool is persisted to .env. The message holding
        the raw key is deleted best-effort right after it is read, so the
        key does not stay visible in the chat. Returns True when the
        message was consumed."""
        stripped = (text or "").strip()
        if stripped in ("لغو", "cancel", "/cancel"):
            self._admin_pending.pop(user_id, None)
            await msg.reply_text(t("common.cancelled"))
            return True
        step = pending.get("step")
        if step == "base_url":
            if not (
                stripped.startswith("http://") or stripped.startswith("https://")
            ):
                await msg.reply_text(t("admin.addkey.bad_url"))
                return True
            pending["base_url"] = stripped.rstrip("/")
            pending["step"] = "model"
            await msg.reply_text(t("admin.addkey.model_prompt"))
            return True
        if step == "model":
            if not stripped or len(stripped) > 200 or any(c.isspace() for c in stripped):
                await msg.reply_text(t("admin.addkey.bad_model"))
                return True
            pending["model"] = stripped
            pending["step"] = "key"
            await msg.reply_text(t("admin.addkey.key_prompt"))
            return True
        if step == "key":
            key = stripped.replace(" ", "").replace("\n", "")
            # Delete the message holding the raw key, best effort.
            try:
                await msg.delete()
            except Exception:
                pass
            if len(key) < 10:
                await msg.reply_text(t("admin.addkey.short_key"))
                return True
            base_url = pending.get("base_url", "")
            model = pending.get("model", "")
            if not base_url or not model:
                self._admin_pending.pop(user_id, None)
                await msg.reply_text(t("common.incomplete"))
                return True
            await msg.reply_text(t("admin.addkey.checking"))
            ok = await TokenPool.probe_entry(base_url, key)
            if not ok:
                self._admin_pending.pop(user_id, None)
                await msg.reply_text(t("admin.addkey.invalid"))
                return True
            added = await self.llm_client.token_pool.add_entry(
                ProviderEntry(base_url=base_url, key=key, model=model)
            )
            self._admin_pending.pop(user_id, None)
            if not added:
                await msg.reply_text(t("admin.addkey.duplicate"))
                return True
            persisted, err = self._persist_pool()
            tokens_text = self._build_admin_tokens_text()
            if persisted:
                await msg.reply_text(
                    t("admin.addkey.done", tokens=tokens_text),
                    reply_markup=self._admin_tokens_keyboard(),
                )
            else:
                await msg.reply_text(
                    t("admin.addkey.done_nosave", err=err, tokens=tokens_text),
                    reply_markup=self._admin_tokens_keyboard(),
                )
            return True
        # Unknown step: clear and fall through to normal handling.
        self._admin_pending.pop(user_id, None)
        return False

    async def _handle_addimage_input(
        self, msg: Message, user_id: int, pending: dict, text: str
    ) -> bool:
        """One step of the /admin 'add image provider' flow: base_url ->
        model -> key. The provider is validated live with a real image
        generation (LLMClient.probe_image) before it is saved; the test
        image is sent back as proof. The message holding the raw key is
        deleted best-effort right after it is read. Returns True when the
        message was consumed."""
        stripped = (text or "").strip()
        if stripped in ("لغو", "cancel", "/cancel"):
            self._admin_pending.pop(user_id, None)
            await msg.reply_text(t("common.cancelled"))
            return True
        step = pending.get("step")
        if step == "base_url":
            if not (
                stripped.startswith("http://") or stripped.startswith("https://")
            ):
                await msg.reply_text(t("admin.addkey.bad_url"))
                return True
            pending["base_url"] = stripped.rstrip("/")
            pending["step"] = "model"
            await msg.reply_text(t("admin.addimage.model_prompt"))
            return True
        if step == "model":
            if not stripped or len(stripped) > 200 or any(c.isspace() for c in stripped):
                await msg.reply_text(t("admin.addkey.bad_model"))
                return True
            pending["model"] = stripped
            pending["step"] = "key"
            await msg.reply_text(t("admin.addimage.key_prompt"))
            return True
        if step == "key":
            key = stripped.replace(" ", "").replace("\n", "")
            # Delete the message holding the raw key, best effort.
            try:
                await msg.delete()
            except Exception:
                pass
            if len(key) < 10:
                await msg.reply_text(t("admin.addkey.short_key"))
                return True
            base_url = pending.get("base_url", "")
            model = pending.get("model", "")
            if not base_url or not model:
                self._admin_pending.pop(user_id, None)
                await msg.reply_text(t("common.incomplete"))
                return True
            await msg.reply_text(t("admin.addimage.probing"))
            img_bytes = await LLMClient.probe_image(base_url, key, model)
            if img_bytes is None:
                self._admin_pending.pop(user_id, None)
                await msg.reply_text(t("admin.addimage.invalid"))
                return True
            self.db.set_image_provider(base_url, key, model)
            self.db.set_image_model("custom")
            self._admin_pending.pop(user_id, None)
            await msg.reply_text(
                t("admin.addimage.done", image=self._build_admin_image_text()),
                reply_markup=self._admin_image_keyboard(),
            )
            try:
                await msg.reply_photo(
                    photo=img_bytes,
                    caption=t("admin.addimage.test_caption"),
                )
            except Exception:
                pass
            return True
        # Unknown step: clear and fall through to normal handling.
        self._admin_pending.pop(user_id, None)
        return False

    async def handle_callback_query(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Handles inline-button presses: the self-update buttons
        ('update:*', boss-only, routed first) and the hidden admin
        panel ('admin:*', boss-only). Unknown callback data is ignored."""
        query = update.callback_query
        if not query or not query.data:
            return
        # Self-update buttons (boss taps these in PV, not in /admin):
        # route before the admin-panel branch.
        if query.data.startswith("update:"):
            await handle_update_callback(
                query, self.db, self.settings.boss_id, self.settings.update_repo
            )
            return
        # Hidden admin panel: route first, boss-only.
        if query.data.startswith(_ADMIN_CB + ":"):
            await self._handle_admin_callback(update, context)
            return
        return

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Main unified message & attachment handler."""
        msg = update.effective_message
        chat = update.effective_chat
        user = update.effective_user

        if not msg or not chat or not user or user.is_bot:
            return

        chat_id = chat.id
        user_id = user.id

        # Telegram service user (777000) posts service messages (e.g. in
        # channels); never treat them as a real user.
        if user_id == 777000:
            return

        # ==================================================================
        # 1. FIRST STEP: Check `blocked_users` in SQLite
        #    Ignored completely: no reply, no LLM, no search, no 'ورتکس دلار',
        #    even if replying to Vortex's messages or sending files.
        # ==================================================================
        if self.db.is_user_banned(chat_id, user_id, check_global=True):
            return

        # ==================================================================
        # 2. Private Chat (PV): open to EVERYONE (not just the Boss).
        #    Anyone can chat with Vortex in PV, no wake word needed —
        #    talking directly to the bot is activation by itself.
        #    (Daily 30-message limit + ban check still apply below.)
        # ==================================================================
        is_boss = user_id == self.settings.boss_id

        if chat.type not in {ChatType.GROUP, ChatType.SUPERGROUP, ChatType.PRIVATE}:
            return

        text_or_caption = (msg.text or msg.caption or "").strip()
        bot_id = context.bot.id

        # ==================================================================
        # 3. Boss Administrative Commands (Ban / Unban)
        #    - Strictly verified via numeric `user.id == BOSS_ID`
        #    - Must be a reply to another user's message
        #    - Does NOT require the word 'ورتکس'
        #    - Whole-message exact match after normalization
        #    - Never passes through LLM (immune to prompt injection)
        # ==================================================================
        if is_boss and msg.reply_to_message and msg.reply_to_message.from_user and not _is_service_message(msg.reply_to_message):
            target_user = msg.reply_to_message.from_user
            target_id = target_user.id

            is_ban_cmd = match_exact_command(text_or_caption, self.settings.ban_commands)
            is_unban_cmd = match_exact_command(text_or_caption, self.settings.unban_commands)

            if is_ban_cmd or is_unban_cmd:
                # Never allow banning Boss or the Bot itself
                if target_id == self.settings.boss_id:
                    await msg.reply_text(t("ban.self"))
                    return
                if target_id == bot_id:
                    await msg.reply_text(t("ban.bot_self", bot=_bot_name()))
                    return

                if is_ban_cmd:
                    newly_banned = self.db.ban_user(
                        chat_id=chat_id,
                        target_user_id=target_id,
                        actor_id=user_id,
                        global_ban=self.settings.global_ban_default,
                    )
                    if newly_banned:
                        await msg.reply_text(random.choice(t_list("ban.done")))
                    else:
                        await msg.reply_text(t("ban.already"))
                    return

                if is_unban_cmd:
                    was_unbanned = self.db.unban_user(
                        chat_id=chat_id,
                        target_user_id=target_id,
                        actor_id=user_id,
                        global_ban=self.settings.global_ban_default,
                    )
                    if was_unbanned:
                        await msg.reply_text(random.choice(t_list("unban.done")))
                    else:
                        await msg.reply_text(t("unban.not_banned"))
                    return

        # ==================================================================
        # 3b. Pending /admin input (boss or a permitted manager tapped
        #     ban/unban/allowlist/add-manager in the admin panel and the
        #     bot is waiting for a numeric user id, or the add-key flow).
        #     Consumed here, before activation, so a bare id never reaches
        #     the LLM. PV-only. The permission for the pending action is
        #     checked inside _handle_admin_pending_input.
        # ==================================================================
        if (is_boss or self.db.is_manager(user_id)) and chat.type == ChatType.PRIVATE:
            if await self._handle_admin_pending_input(msg, user_id, text_or_caption):
                return

        # ==================================================================
        # 4. Activation Rules
        #    - Message (or file caption) contains standalone word 'ورتکس'
        #    - OR user replied directly to a message sent by the bot itself
        #    - OR the message is a known slash command (no wake word needed;
        #      unknown slash commands like /foo return "" and never
        #      activate the bot; /start IS a known command and is handled
        #      below with a short welcome, no LLM call)
        #    - OR the message is in a private chat (anyone talking directly
        #      to Vortex in PV needs no wake word)
        # ==================================================================
        replied_msg = msg.reply_to_message
        is_reply_to_bot = bool(
            replied_msg
            and replied_msg.from_user
            and replied_msg.from_user.id == bot_id
            and not _is_service_message(replied_msg)
        )
        has_wake_word = has_vortex_wake_word(text_or_caption)
        slash_cmd, slash_args = parse_slash_command(
            text_or_caption, bot_username=context.bot.username
        )
        # In a private chat anyone talks to Vortex directly (no wake word).
        is_private_chat = chat.type == ChatType.PRIVATE

        if not (has_wake_word or is_reply_to_bot or is_private_chat or slash_cmd):
            return

        # ==================================================================
        # 4a. Private mode (/off): only the boss, managers and allowlisted
        #     users may use the bot. /on, /off and /admin are exempt (they
        #     have their own permission checks in 5b). In a group the bot
        #     stays silent for non-allowed users (no spam); in PV it
        #     answers with the reason.
        # ==================================================================
        if slash_cmd not in ("on", "off", "admin") and not self.db.is_bot_enabled():
            if not (
                is_boss
                or self.db.is_manager(user_id)
                or self.db.is_user_allowlisted(user_id)
            ):
                if is_private_chat:
                    await msg.reply_text(t("common.bot_off"))
                return

        # ==================================================================
        # 5. Rate Limiting (Boss is always exempt)
        # ==================================================================
        if not self.rate_limiter.is_allowed(chat_id, user_id):
            await msg.reply_text(t("common.rate_limit"))
            return

        # Track the sender for the boss-only stats (groups + members).
        # A DB error here must never break the reply.
        try:
            self.db.upsert_chat_user(
                chat_id, user_id, user.full_name or "", user.username or ""
            )
        except Exception:
            logger.warning(
                "upsert_chat_user failed for chat=%s user=%s", chat_id, user_id
            )

        # ==================================================================
        # 5b. Meta commands — free, never consume daily quota:
        #     /start (welcome, no LLM call), 'ورتکس آمار' / /stats (boss only),
        #     'ورتکس سهمیه' / /quota, 'ورتکس راهنما' / /help, 'ورتکس آیدی' / /id
        #     (Persian wake-word form OR slash form — same handler.)
        # ==================================================================
        if slash_cmd == "start":
            await msg.reply_text(t("start.text", bot=_bot_name()))
            return

        # /on and /off: bot-wide power switch (hidden like /admin, never
        # in /help or any menu). /on = public, everyone may use the bot;
        # /off = private, only the boss, managers and allowlisted users.
        # Boss-only, or a manager with the 'power' permission. Exempt
        # from the private-mode check (4a) so the bot can be turned back
        # on.
        if slash_cmd in ("on", "off"):
            if not (is_boss or self._admin_has_perm(user_id, "power")):
                await msg.reply_text(t("common.not_boss"))
                return
            enabled = slash_cmd == "on"
            self.db.set_bot_enabled(enabled)
            await msg.reply_text(
                t("admin.power.on") if enabled else t("admin.power.off")
            )
            return

        # Hidden admin panel: boss + managers, PV-only, never listed in
        # /help or any command menu — it exists only when /admin is typed.
        # A manager sees only the sections their permissions open; a
        # manager with no permissions gets a refusal.
        if slash_cmd == "admin":
            if not is_boss and not self.db.is_manager(user_id):
                await msg.reply_text(t("common.not_boss"))
                return
            if not is_boss and not self.db.get_manager_perms(user_id):
                await msg.reply_text(t("admin.no_perms"))
                return
            if chat.type != ChatType.PRIVATE:
                await msg.reply_text(t("admin.pv_only"))
                return
            await msg.reply_text(
                _admin_menu_text(), reply_markup=self._admin_menu_keyboard(user_id)
            )
            return

        if is_stats_query(text_or_caption) or slash_cmd == "stats":
            if not is_boss:
                await msg.reply_text(t("common.not_boss"))
                return
            # Never dump other groups' member lists into a group.
            if chat.type != ChatType.PRIVATE:
                await msg.reply_text(t("stats.pv_only"))
                return
            stats_text = await self._build_stats_text(context)
            await _send_reply(msg, stats_text)
            return

        if is_chat_history_query(text_or_caption):
            # Boss-only: who chatted with the bot and what was said.
            # The LLM refuses this on privacy grounds, so it is answered
            # deterministically from the stored history instead.
            # Non-boss users get the privacy line (what the LLM used to say).
            if not is_boss:
                await msg.reply_text(t("chats.privacy"))
                return
            if chat.type != ChatType.PRIVATE:
                # Never dump other users' chats into a group.
                await msg.reply_text(t("chats.pv_only"))
                return
            history_text = self._build_chat_history_text()
            await _send_reply(msg, history_text)
            return

        if is_quota_query(text_or_caption) or slash_cmd == "quota":
            if is_boss:
                await msg.reply_text(t("quota.boss"))
            else:
                used, remaining = self.db.get_daily_use(
                    user_id, self.settings.daily_limit_messages
                )
                await msg.reply_text(
                    t(
                        "quota.text",
                        used=_num(used),
                        remaining=_num(remaining),
                        limit=_num(self.settings.daily_limit_messages),
                    )
                )
            return

        if is_help_query(text_or_caption) or slash_cmd == "help":
            await msg.reply_text(
                t(
                    "help.text",
                    bot=_bot_name(),
                    currency=currency_label(),
                    city=current_country().capital,
                )
            )
            return

        if is_id_query(text_or_caption) or slash_cmd == "id":
            await msg.reply_text(t("id.text", id=user_id))
            return

        # ==================================================================
        # 5c. Daily quota: N messages per user per day (Boss exempt).
        #     Meta commands above are free; everything else costs 1.
        # ==================================================================
        if not is_boss:
            allowed, _used, _remaining = self.db.check_and_record_daily_use(
                user_id, self.settings.daily_limit_messages
            )
            if not allowed:
                await msg.reply_text(
                    t(
                        "quota.exceeded",
                        limit=_num(self.settings.daily_limit_messages),
                    )
                )
                return

        # ==================================================================
        # 6. Fast Path 1: 'ورتکس فراموشم کن' / /forget (Clear only this user's context)
        # ==================================================================
        if is_forget_me_query(text_or_caption) or slash_cmd == "forget":
            self.db.clear_user_context(chat_id, user_id)
            if is_boss:
                await msg.reply_text(t("forget.done_boss"))
            else:
                await msg.reply_text(t("forget.done"))
            return

        # ==================================================================
        # 7. Fast Path 2: 'ورتکس دلار' / /dollar (Bypasses LLM completely)
        # ==================================================================
        if is_dollar_query(text_or_caption) or slash_cmd == "dollar":
            dollar_reply = await self.dollar_service.get_dollar_message(is_boss=is_boss)
            await msg.reply_text(dollar_reply, parse_mode="Markdown")
            return

        # ==================================================================
        # 7c. Fast Paths 4-9: prices / gold / crypto / time / weather / price
        #     (after the daily-limit enforcement, like دلار; all cost 1 quota)
        #     Persian wake-word form OR slash form — same handler each.
        # ==================================================================
        if is_currency_query(text_or_caption) or slash_cmd == "currency":
            try:
                rows = await fetch_fiat()
                updated = await fetch_market_updated()
                text = format_fiat_text(rows, updated)
            except Exception:
                text = ""
            await _send_reply(msg, text or t("prices.unavailable"))
            return

        if is_gold_query(text_or_caption) or slash_cmd == "gold":
            try:
                rows = await fetch_gold()
                updated = await fetch_market_updated()
                oil = await fetch_oil()
                text = format_gold_text(rows, updated, oil)
            except Exception:
                text = ""
            await _send_reply(msg, text or t("prices.unavailable"))
            return

        if is_crypto_query(text_or_caption) or slash_cmd == "crypto":
            try:
                rows = await fetch_crypto()
                updated = await fetch_market_updated()
                text = format_crypto_text(rows, updated)
            except Exception:
                text = ""
            await _send_reply(msg, text or t("prices.unavailable"))
            return

        if is_time_query(text_or_caption) or slash_cmd == "time":
            try:
                await msg.reply_text(tehran_now_text())
            except Exception:
                await msg.reply_text(t("time.failed"))
            return

        weather_city = extract_weather_city(text_or_caption)
        if slash_cmd == "weather":
            weather_city = slash_args
        if weather_city is not None:
            if not weather_city:
                await msg.reply_text(
                    t("weather.ask_city", bot=_bot_name())
                )
                return
            try:
                weather = await fetch_weather(weather_city)
            except Exception:
                weather = None
            if weather:
                await _send_reply(msg, format_weather_text(weather))
            else:
                await msg.reply_text(t("weather.failed", city=weather_city))
            return

        price_name = extract_price_currency(text_or_caption)
        if slash_cmd == "price":
            price_name = slash_args
        if price_name is not None:
            if not price_name:
                await msg.reply_text(t("price.ask", bot=_bot_name()))
                return
            try:
                row = await lookup_currency(price_name)
            except Exception:
                row = None
            if row:
                await _send_reply(msg, format_single_currency(row))
            else:
                await msg.reply_text(t("price.unknown"))
            return

        # ==================================================================
        # 7d. Fast Paths 10-16: fun + utility extras (after the daily-limit
        #     enforcement, like prices; all cost 1 quota). Persian wake-word
        #     form OR slash form — same handler each.
        # ==================================================================
        if is_faal_query(text_or_caption) or slash_cmd == "faal":
            try:
                faal = await fetch_faal()
                text = format_faal(faal)
            except Exception:
                text = ""
            await _send_reply(msg, text or t("faal.failed"))
            return

        if is_news_query(text_or_caption) or slash_cmd == "news":
            try:
                items = await fetch_news()
                text = format_news(items)
            except Exception:
                text = ""
            await _send_reply(msg, text or t("news.failed"))
            return

        prayer_city = extract_prayer_city(text_or_caption)
        if slash_cmd == "prayer":
            prayer_city = slash_args
        if prayer_city is not None:
            try:
                result = await fetch_prayer_times(prayer_city or None)
                text = format_prayer_times(result)
            except Exception:
                text = ""
            await _send_reply(msg, text or t("prayer.failed"))
            return

        calc_expr = extract_calc_expr(text_or_caption)
        if slash_cmd == "calc":
            calc_expr = slash_args
        if calc_expr is not None:
            if not calc_expr:
                await msg.reply_text(t("calc.ask", bot=_bot_name()))
                return
            try:
                result = calc(calc_expr)
                text = format_calc(calc_expr, result)
            except Exception:
                text = ""
            await _send_reply(msg, text or t("calc.failed", bot=_bot_name()))
            return

        if is_dice_query(text_or_caption) or slash_cmd == "dice":
            await msg.reply_text(format_dice(roll_dice()))
            return

        if is_coin_query(text_or_caption) or slash_cmd == "coin":
            await msg.reply_text(format_coin(flip_coin()))
            return

        if is_joke_query(text_or_caption) or slash_cmd == "joke":
            await msg.reply_text(get_joke())
            return

        # ==================================================================
        # 7e. Fast Path: 'ورتکس دانلود کن <لینک>' / /download <لینک>
        #     Download a file from a link and send it back (costs 1 quota).
        #     The direct media URL is pulled out of the page source when
        #     the page has no download button (see bot/downloader.py).
        # ==================================================================
        download_url = extract_download_url(text_or_caption)
        if slash_cmd == "download":
            download_url = slash_args
        if download_url is not None:
            if not download_url:
                await msg.reply_text(t("download.ask", bot=_bot_name()))
                return
            status_msg = None
            try:
                status_msg = await msg.reply_text(t("download.downloading"))
            except Exception:
                status_msg = None
            try:
                await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.UPLOAD_DOCUMENT)
            except Exception:
                pass
            with self.workspace_mgr.isolated_workspace(prefix=f"vortex_dl_{chat_id}_{user_id}_") as dl_dir:
                try:
                    downloaded = await asyncio.to_thread(download_media, download_url, dl_dir)
                except DownloadError as exc:
                    fail_text = download_error_text(exc.reason)
                    if exc.reason == "too_large" and exc.detail:
                        fail_text = t("download.too_large_detail", size=exc.detail)
                    if status_msg is not None:
                        try:
                            await status_msg.edit_text(fail_text)
                        except Exception:
                            await msg.reply_text(fail_text)
                    else:
                        await msg.reply_text(fail_text)
                    try:
                        self.db.refund_daily_use(user_id)
                    except Exception:
                        pass
                    return
                except Exception:
                    fail_text = t("download.failed")
                    if status_msg is not None:
                        try:
                            await status_msg.edit_text(fail_text)
                        except Exception:
                            await msg.reply_text(fail_text)
                    else:
                        await msg.reply_text(fail_text)
                    try:
                        self.db.refund_daily_use(user_id)
                    except Exception:
                        pass
                    return
                if status_msg is not None:
                    try:
                        await status_msg.delete()
                    except Exception:
                        pass
                sent = await self._reply_document_with_retry(
                    msg, downloaded.path, downloaded.filename, t("download.ready")
                )
                if not sent:
                    await msg.reply_text(
                        t("download.send_failed")
                    )
            return

        # ==================================================================
        # 7b. Fast Path 3: 'ورتکس عکس ...' (Image generation, bypasses LLM)
        #     Runs after the rate-limit check above, like the dollar path.
        #     Also handles follow-ups that add something to the last image
        #     ("انویدیا هم توی عکس بیار" — usually a reply to the bot's
        #     image, so no wake word): the full prompt is rebuilt from
        #     the chat's last image prompt + the added element.
        # ==================================================================
        image_prompt = extract_image_prompt(text_or_caption)
        if image_prompt is None:
            # Bare "X هم بزار/بیار" (no "عکس" word, e.g. "یدونه خر هم بزار")
            # only counts as an image follow-up when there IS image
            # context: a reply to a photo, or a remembered last image
            # prompt in this chat. Without that anchor it could mean
            # anything ("یه چایی هم بزار").
            has_image_context = bool(
                (replied_msg and replied_msg.photo)
                or self._get_last_image_prompt(chat_id, user_id)
            )
            added = extract_image_add_prompt(
                text_or_caption, allow_bare=has_image_context
            )
            if added is not None:
                last_prompt = self._get_last_image_prompt(chat_id, user_id)
                if last_prompt:
                    image_prompt = f"{last_prompt} و {added}"
                else:
                    # No remembered prompt (bot restarted, or the
                    # follow-up was not a reply): generate just the
                    # added element instead of refusing.
                    image_prompt = added
        if image_prompt is not None:
            if not image_prompt:
                await msg.reply_text(t("image.ask", bot=_bot_name()))
                return
            # Status message while the image is being made (neutral, no provider label).
            status_msg = None
            try:
                status_msg = await msg.reply_text(t("image.making"))
            except Exception:
                status_msg = None
            try:
                await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.UPLOAD_PHOTO)
            except Exception:
                pass
            image_bytes, err = await self.llm_client.generate_image(image_prompt)
            if image_bytes:
                # Remember the prompt so a follow-up can add to it.
                self._last_image_prompt[(chat_id, user_id)] = (
                    image_prompt[:500], time.monotonic()
                )
                if status_msg is not None:
                    try:
                        await status_msg.delete()
                    except Exception:
                        pass
                sent = await self._reply_photo_with_retry(
                    msg, image_bytes, t("image.ready")
                )
                if not sent:
                    await msg.reply_text(t("image.send_failed"))
            elif err == "not_configured":
                fail_text = t("image.not_configured")
                if status_msg is not None:
                    try:
                        await status_msg.edit_text(fail_text)
                    except Exception:
                        await msg.reply_text(fail_text)
                else:
                    await msg.reply_text(fail_text)
            elif err == "disabled":
                fail_text = t("image.disabled")
                if status_msg is not None:
                    try:
                        await status_msg.edit_text(fail_text)
                    except Exception:
                        await msg.reply_text(fail_text)
                else:
                    await msg.reply_text(fail_text)
            else:
                fail_text = t("image.failed")
                if status_msg is not None:
                    try:
                        await status_msg.edit_text(fail_text)
                    except Exception:
                        await msg.reply_text(fail_text)
                else:
                    await msg.reply_text(fail_text)
            return

        # ==================================================================
        # 8. Detect File Activation:
        #    - Current message has a file whose caption includes 'ورتکس' (or replies to bot)
        #    - OR User replied to a message containing a file with a message containing 'ورتکس'
        # ==================================================================
        target_file_msg: Message | None = None
        file_id, filename, file_size = self._extract_attachment_info(msg)
        if file_id and (has_wake_word or is_reply_to_bot or is_private_chat):
            target_file_msg = msg
        elif replied_msg and has_wake_word:
            r_file_id, r_filename, r_file_size = self._extract_attachment_info(replied_msg)
            if r_file_id:
                target_file_msg = replied_msg
                file_id, filename, file_size = r_file_id, r_filename, r_file_size

        # Ephemeral replied text when User A replies to User B (and asks Vortex for opinion)
        ephemeral_replied_text: str | None = None
        ephemeral_replied_author: str | None = None
        if (
            replied_msg
            and not is_reply_to_bot
            and target_file_msg is not replied_msg
        ):
            r_text = (replied_msg.text or replied_msg.caption or "").strip()
            if r_text:
                ephemeral_replied_text = r_text
                if replied_msg.from_user:
                    ephemeral_replied_author = (
                        replied_msg.from_user.full_name or replied_msg.from_user.username or t("stats.user")
                    )

        sender_name = user.full_name or user.username or t("stats.user")
        user_prompt_text = text_or_caption or t("file.default_prompt")

        try:
            await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        except Exception:
            pass

        # ==================================================================
        # 9. File Processing Flow (6 Strict Steps + Isolated Temp Workspace)
        #    1) Download to isolated temp workspace
        #    2) Check type & size
        #    3) Read & extract content
        #    4) Analyze with LLM
        #    5) Reply to user's own message
        #    6) Immediately delete file & workspace in `finally`
        # ==================================================================
        # Oversized / undownloadable file + real question: the file
        # itself cannot be downloaded (Telegram Bot API caps bot
        # downloads at 20MB, no matter the configured limit), but the
        # user's text question can still be answered (e.g. via web
        # search). Skip the file flow so the regular chat flow
        # (section 10) handles the text instead of refusing outright.
        # TELEGRAM_BOT_DOWNLOAD_CAP_MB is the Bot API download ceiling.
        if (
            target_file_msg
            and file_id
            and file_size is not None
            and file_size > 20 * 1024 * 1024
            and strip_wake_word(text_or_caption).strip()
        ):
            await msg.reply_text(t("file.too_heavy"))
            target_file_msg = None

        if target_file_msg and file_id:
            # Pre-check metadata before downloading
            is_valid, ext, err_msg = self.file_processor.validate_file_meta(filename, file_size)
            if not is_valid:
                await msg.reply_text(err_msg)
                return

            extracted_data = None
            llm_result = None
            with self.workspace_mgr.isolated_workspace(prefix=f"vortex_in_{chat_id}_{user_id}_") as ws_dir:
                try:
                    # Step 1: Download into isolated temporary workspace
                    safe_name = self.file_processor.sanitize_filename(filename)
                    local_file_path: Path = ws_dir / safe_name
                    tg_file = await context.bot.get_file(file_id)
                    await tg_file.download_to_drive(custom_path=str(local_file_path))

                    # Step 2: Check actual downloaded size & type
                    actual_size = local_file_path.stat().st_size
                    is_valid_post, ext, err_msg_post = self.file_processor.validate_file_meta(
                        safe_name, actual_size
                    )
                    if not is_valid_post:
                        await msg.reply_text(err_msg_post)
                        return

                    # Step 3: Read and extract content safely (with timeout & resource caps)
                    extracted_data = await self.file_processor.extract_from_path(
                        local_file_path, safe_name, ext
                    )

                    # Step 3b: Transcribe audio (voice note / audio file /
                    # video audio track) with Groq Whisper. A failure here
                    # never breaks the reply (the bot answers from the
                    # frames/metadata instead).
                    audio_transcript: str | None = None
                    if extracted_data.media_kind in ("audio", "video") and extracted_data.audio_path:
                        try:
                            audio_transcript = await transcribe_audio(extracted_data.audio_path)
                        except Exception as exc:
                            logger.warning(
                                "Audio transcription failed for chat=%s user=%s err=%s",
                                chat_id, user_id, type(exc).__name__,
                            )
                            audio_transcript = None
                    # A bare voice note / video with no caption: answer what
                    # was said / shown instead of the generic file prompt.
                    if extracted_data.media_kind == "audio" and not text_or_caption:
                        user_prompt_text = t("file.voice_prompt")
                    elif extracted_data.media_kind == "video" and not text_or_caption:
                        user_prompt_text = t("file.video_prompt")

                    # Step 4: Analyze with LLM (live terminal-style status)
                    llm_result = await self._generate_reply_with_status(
                        msg,
                        chat_id=chat_id,
                        user_id=user_id,
                        sender_name=sender_name,
                        is_boss=is_boss,
                        user_text=user_prompt_text,
                        ephemeral_replied_text=ephemeral_replied_text,
                        ephemeral_replied_author=ephemeral_replied_author,
                        ephemeral_file_text=extracted_data.extracted_text,
                        ephemeral_image_b64=extracted_data.image_base64,
                        ephemeral_image_mime=extracted_data.image_mime,
                        ephemeral_audio_transcript=audio_transcript,
                        ephemeral_video_frames=extracted_data.video_frames_b64 or None,
                    )

                    # Step 5: Send explanation (reply to user's own message)
                    await _send_reply(msg, llm_result.text)

                    # The LLM path failed: the user got an error message,
                    # so give the daily-quota unit back.
                    if llm_result.text in (
                        t("llm.error_generic"),
                        t("llm.error_boss"),
                        t("llm.vision_unavailable"),
                    ):
                        try:
                            self.db.refund_daily_use(user_id)
                        except Exception:
                            pass

                    # If the user also requested creating a new output file from this file
                    for fspec in llm_result.files_to_create:
                        await self._create_and_send_output_file(msg, chat_id, user_id, fspec)

                    # If the LLM called create_image, send the generated photo(s)
                    for ispec in llm_result.images_to_create:
                        await self._send_output_image(msg, ispec)

                    # If the LLM downloaded a file, send it as a document
                    for dspec in llm_result.downloads_to_create:
                        await self._send_output_download(msg, dspec)

                except asyncio.TimeoutError:
                    logger.warning("File extraction timed out for chat=%s user=%s", chat_id, user_id)
                    await msg.reply_text(t("file.timeout"))
                    return
                except Exception as exc:
                    # Never log file contents; only log error class
                    logger.error(
                        "Error processing file in chat=%s user=%s err=%s",
                        chat_id,
                        user_id,
                        type(exc).__name__,
                    )
                    await msg.reply_text(t("file.read_failed"))
                    return
                # Step 6: Exiting the `with self.workspace_mgr.isolated_workspace(...)` block
                # immediately deletes `ws_dir` and `local_file_path` inside `finally`.

            # Post-deletion: store ONLY a short summary in user's isolated context (if enabled in config).
            # The user already got their answer; a failure here must never
            # surface as an error to them.
            if extracted_data and self.settings.store_file_summary_in_context:
                try:
                    short_summary = await self.llm_client.summarize_file_for_context(
                        extracted_data.filename, extracted_data.short_summary_seed
                    )
                    self.db.set_file_summary(chat_id, user_id, short_summary)
                except Exception as exc:
                    logger.warning(
                        "File summary store failed for chat=%s user=%s: %s",
                        chat_id,
                        user_id,
                        type(exc).__name__,
                    )
            return

        # ==================================================================
        # 10. Regular Group Message Flow (Text / Reply / Tool Calling)
        # ==================================================================
        llm_result = await self._generate_reply_with_status(
            msg,
            chat_id=chat_id,
            user_id=user_id,
            sender_name=sender_name,
            is_boss=is_boss,
            user_text=user_prompt_text,
            ephemeral_replied_text=ephemeral_replied_text,
            ephemeral_replied_author=ephemeral_replied_author,
        )

        await _send_reply(msg, llm_result.text)

        # The LLM path failed (generic error / vision unavailable): the
        # user got an error message, so give the daily-quota unit back.
        if llm_result.text in (
            t("llm.error_generic"),
            t("llm.error_boss"),
            t("llm.vision_unavailable"),
        ):
            try:
                self.db.refund_daily_use(user_id)
            except Exception:
                pass

        # If LLM invoked `create_file`, generate in isolated temp workspace, send, and delete immediately
        for fspec in llm_result.files_to_create:
            await self._create_and_send_output_file(msg, chat_id, user_id, fspec)

        # If LLM invoked `create_image`, send the generated photo(s)
        for ispec in llm_result.images_to_create:
            await self._send_output_image(msg, ispec)

        # If LLM invoked `download_file`, send the downloaded file(s)
        for dspec in llm_result.downloads_to_create:
            await self._send_output_download(msg, dspec)

    async def _build_stats_text(self, context: ContextTypes.DEFAULT_TYPE) -> str:
        """Boss-only stats (code-generated, never via LLM):
        groups with titles + member counts, top members with numeric
        ids, current chat model, and the image generator (GPT Image)."""
        lines: list[str] = [t("stats.title"), ""]
        groups = self.db.list_known_groups()
        lines.append(t("stats.groups", count=_num(len(groups))))

        # Resolve titles + real member counts best-effort (cap 20 groups).
        group_infos: list[tuple[int, str, int]] = []
        for chat_id in groups[:20]:
            members = self.db.list_group_members(chat_id)
            title = t("stats.unknown")
            count = len(members)
            try:
                chat = await context.bot.get_chat(chat_id)
                title = chat.title or chat.first_name or t("stats.unknown")
            except Exception:
                pass
            try:
                count = await context.bot.get_chat_member_count(chat_id)
            except Exception:
                pass
            group_infos.append((chat_id, title, count))
        group_infos.sort(key=lambda t: t[2], reverse=True)
        for chat_id, title, count in group_infos:
            lines.append(
                t("stats.group_row", title=title, count=_num(count), id=chat_id)
            )
        if len(groups) > 20:
            lines.append(t("stats.more_groups", count=_num(len(groups) - 20)))
        lines.append("")

        total_members = self.db.count_all_members()
        lines.append(t("stats.members_total", count=_num(total_members)))
        # Top members of the top 3 groups by member count.
        for chat_id, title, _count in group_infos[:3]:
            members = self.db.list_group_members(chat_id)[:5]
            if not members:
                continue
            lines.append(t("stats.top_members", title=title))
            for m in members:
                name = m["first_name"] or t("stats.user")
                uname = f"@{m['username']}" if m["username"] else "—"
                lines.append(
                    t(
                        "stats.member_row",
                        name=name,
                        username=uname,
                        id=m['user_id'],
                        count=_num(m['message_count']),
                    )
                )
        lines.append("")
        lines.append(t("stats.chat_model", model=self.llm_client.describe_active_model()))
        return "\n".join(lines)

    def _build_chat_history_text(self) -> str:
        """Boss-only chat history (code-generated, never via LLM): who
        chatted with the bot and what was said, verbatim, most recent
        30 messages from everyone except the boss himself."""
        rows = self.db.list_recent_chat_history(
            limit=30, exclude_user_id=self.settings.boss_id
        )
        if not rows:
            return t("chats.empty")
        # Group by user, preserving first-seen order.
        users: dict[int, dict] = {}
        order: list[int] = []
        for r in rows:
            uid = r["user_id"]
            if uid not in users:
                users[uid] = {
                    "first_name": r["first_name"],
                    "username": r["username"],
                    "messages": [],
                }
                order.append(uid)
            users[uid]["messages"].append(r)
        lines = [t("chats.title", bot=_bot_name()), ""]
        for uid in order:
            u = users[uid]
            name = u["first_name"] or t("stats.user")
            uname = f"@{u['username']}" if u["username"] else "—"
            lines.append(t("chats.user_row", name=name, uname=uname, id=uid))
            for m in u["messages"]:
                when = _local_stamp(m["created_at"])
                who = t("chats.them") if m["role"] == "user" else _bot_name()
                # One line per message; newlines inside a message are flattened.
                content = " ".join(str(m["content"]).split())
                stamp = f"[{when}] " if when else ""
                lines.append(f"  {stamp}{who}: {content}")
            lines.append("")
        return "\n".join(lines).rstrip()

    async def _generate_reply_with_status(
        self, msg: Message, **kwargs
    ) -> LLMResponseResult:
        """Run generate_reply while showing a live terminal-style status
        message (a code block, so Telegram renders it as code with a
        'copy code' button below) that updates as the bot works. The status
        is deleted once the final reply is ready, and the caller then sends
        the real answer. Status send/edit/delete failures never break the
        reply itself."""
        status_lines: list[str] = ["[+] session initialized"]
        status_msg = None
        last_edit = 0.0

        def _render() -> str:
            return "```\n" + "\n".join(status_lines) + "\n```"

        try:
            status_msg = await msg.reply_text(_render(), parse_mode="Markdown")
        except Exception:
            status_msg = None

        async def on_progress(line: str) -> None:
            nonlocal last_edit
            status_lines.append(line)
            if status_msg is None:
                return
            now = time.monotonic()
            if now - last_edit < 1.2:
                return
            last_edit = now
            try:
                await status_msg.edit_text(_render(), parse_mode="Markdown")
            except Exception:
                pass

        try:
            return await self.llm_client.generate_reply(
                on_progress=on_progress, **kwargs
            )
        finally:
            if status_msg is not None:
                try:
                    await status_msg.delete()
                except Exception:
                    pass

    async def _create_and_send_output_file(
        self,
        msg: Message,
        chat_id: int,
        user_id: int,
        fspec,
    ) -> None:
        """
        Builds a requested file (`txt`, `md`, `pdf`, `docx`, `xlsx`, `csv`, or code)
        inside an isolated temporary workspace, sends it as a reply in the group,
        and deletes it immediately inside `finally`.
        """
        with self.workspace_mgr.isolated_workspace(prefix=f"vortex_out_{chat_id}_{user_id}_") as out_dir:
            try:
                generated_path = await asyncio.to_thread(
                    self.file_processor.build_file_in_workspace,
                    out_dir,
                    fspec.filename,
                    fspec.content,
                )
                with generated_path.open("rb") as doc_stream:
                    await msg.reply_document(
                        document=doc_stream,
                        filename=generated_path.name,
                        caption=(fspec.caption or t("download.ready"))[:1024],
                        # A 45MB upload needs far more than the default
                        # ~20s write timeout, or Telegram aborts it.
                        write_timeout=180,
                        read_timeout=180,
                    )
            except Exception as exc:
                logger.error("Failed to create/send output file: %s", type(exc).__name__)
                await msg.reply_text(t("file.create_failed"))

    async def _reply_photo_with_retry(
        self, msg: Message, photo_bytes: bytes, caption: str
    ) -> bool:
        """Send a photo reply, retrying once after Telegram's flood
        control (RetryAfter). A generated/edited image must not be lost
        just because the group was busy: Telegram tells us how long to
        wait (`retry_after`), we wait (capped at 60s) and send again.
        Returns True when the photo was sent, False otherwise."""
        for attempt in range(2):
            try:
                await msg.reply_photo(
                    photo=io.BytesIO(photo_bytes),
                    caption=(caption or t("image.ready"))[:1024],
                )
                return True
            except RetryAfter as exc:
                wait = getattr(exc, "retry_after", 0) or 0
                if attempt == 0 and wait > 0:
                    wait = min(wait, 60)
                    logger.warning(
                        "Photo send rate-limited, retrying in %ss", wait
                    )
                    await asyncio.sleep(wait)
                    continue
                logger.error(
                    "Failed to send photo (RetryAfter, wait=%s)", wait
                )
                return False
            except Exception as exc:
                logger.error("Failed to send photo: %s", type(exc).__name__)
                return False
        return False

    async def _reply_document_with_retry(
        self, msg: Message, file_path: Path, filename: str, caption: str
    ) -> bool:
        """Send a file reply, retrying once after Telegram's flood
        control (RetryAfter), mirroring _reply_photo_with_retry.
        Returns True when the file was sent, False otherwise."""
        for attempt in range(2):
            try:
                with file_path.open("rb") as doc_stream:
                    await msg.reply_document(
                        document=doc_stream,
                        filename=filename,
                        caption=(caption or t("download.ready"))[:1024],
                        # A 45MB upload needs far more than the default
                        # ~20s write timeout, or Telegram aborts it.
                        write_timeout=180,
                        read_timeout=180,
                    )
                return True
            except RetryAfter as exc:
                wait = getattr(exc, "retry_after", 0) or 0
                if attempt == 0 and wait > 0:
                    wait = min(wait, 60)
                    logger.warning(
                        "Document send rate-limited, retrying in %ss", wait
                    )
                    await asyncio.sleep(wait)
                    continue
                logger.error(
                    "Failed to send document (RetryAfter, wait=%s)", wait
                )
                return False
            except Exception as exc:
                logger.error("Failed to send document: %s", type(exc).__name__)
                return False
        return False

    async def _send_output_image(self, msg: Message, ispec) -> None:
        """Send an image the LLM created via the create_image tool
        (a GeneratedImageSpec) as a photo reply in the group."""
        sent = await self._reply_photo_with_retry(
            msg, ispec.image_bytes, ispec.caption or t("image.ready")
        )
        if not sent:
            try:
                await msg.reply_text(t("image.send_failed"))
            except Exception:
                pass

    async def _send_output_download(self, msg: Message, dspec) -> None:
        """Send a file the LLM downloaded via the download_file tool
        (a GeneratedDownloadSpec) as a document reply, then delete the
        temporary directory it was downloaded into."""
        try:
            sent = await self._reply_document_with_retry(
                msg, dspec.path, dspec.filename, dspec.caption or t("download.ready")
            )
            if not sent:
                try:
                    await msg.reply_text(t("download.send_failed"))
                except Exception:
                    pass
        finally:
            try:
                shutil.rmtree(dspec.dir_path, ignore_errors=True)
            except Exception:
                pass


async def global_error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Global error handler that logs the exception class safely (without logging private file contents)
    and sends a short, witty message to the user instead of a stack trace.
    """
    err = context.error
    logger.error("Unhandled Telegram update error: %s", type(err).__name__ if err else "Unknown")
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(t("common.error"))
        except Exception:
            pass
