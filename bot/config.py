"""
Configuration module for Vortex Telegram Bot.
Reads all settings and secrets strictly from environment variables (.env).
No secrets or API keys are hardcoded.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def _parse_bool(val: str | None, default: bool = False) -> bool:
    if val is None:
        return default
    return val.strip().lower() in {"1", "true", "yes", "on"}


def _parse_csv(val: str | None, default: list[str]) -> list[str]:
    if not val or not val.strip():
        return default
    return [item.strip() for item in val.split(",") if item.strip()]


def _llm_api_keys() -> list[str]:
    keys = _parse_csv(os.getenv("LLM_API_KEYS"), [])
    if not keys:
        single = os.getenv("LLM_API_KEY", "").strip()
        if single:
            keys = [single]
    return keys


@dataclass(frozen=True)
class ProviderEntry:
    """One LLM provider endpoint: base_url | key | model.

    The user adds providers in LLM_PROVIDERS as comma-separated entries,
    each ``base_url|key|model`` (base URL first, then the API key, then the
    model to use on that provider). This lets Vortex use several providers
    (e.g. TokenHarbor + IteraCompute) with automatic failover between them.
    """

    base_url: str
    key: str
    model: str


def _parse_providers() -> list[ProviderEntry]:
    raw = os.getenv("LLM_PROVIDERS", "").strip()
    entries: list[ProviderEntry] = []
    if raw:
        for part in raw.split(","):
            part = part.strip()
            if not part:
                continue
            fields = [f.strip() for f in part.split("|")]
            if len(fields) != 3 or not all(fields):
                raise ValueError(
                    "LLM_PROVIDERS entry must be base_url|key|model: %r" % part[:60]
                )
            entries.append(
                ProviderEntry(
                    base_url=fields[0].rstrip("/"), key=fields[1], model=fields[2]
                )
            )
    if not entries:
        # Backward compat: one entry per key from the old single-provider vars.
        base = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").strip()
        model = os.getenv("LLM_MODEL", "gpt-4o-mini").strip()
        for k in _llm_api_keys():
            entries.append(ProviderEntry(base_url=base, key=k, model=model))
    return entries


def find_env_file() -> Path | None:
    """Locate the .env file the bot reads: VORTEX_BOT_ENV when set, else
    ./.env in the working directory, else the file next to the bot
    package (bot/../.env). Returns None when no .env exists."""
    override = os.getenv("VORTEX_BOT_ENV", "").strip()
    if override:
        p = Path(override)
        return p if p.exists() else None
    cwd_env = Path.cwd() / ".env"
    if cwd_env.exists():
        return cwd_env
    pkg_env = Path(__file__).resolve().parent.parent / ".env"
    if pkg_env.exists():
        return pkg_env
    return None


def write_llm_pinned_model(env_path: Path, model: str) -> None:
    """Set (or clear, when model is empty) the LLM_PINNED_MODEL line in
    .env, preserving every other line. Atomic via temp file + os.replace.
    Raises on failure."""
    line = f"LLM_PINNED_MODEL={model}" if model else ""
    text = env_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    replaced = False
    out: list[str] = []
    for ln in lines:
        if ln.strip().startswith("LLM_PINNED_MODEL="):
            if line and not replaced:
                out.append(line)
                replaced = True
            continue
        out.append(ln)
    if line and not replaced:
        out.append(line)
    tmp = env_path.with_suffix(".env.tmp")
    tmp.write_text("\n".join(out) + "\n", encoding="utf-8")
    try:
        tmp.chmod(0o600)
    except Exception:
        pass
    os.replace(tmp, env_path)


def write_llm_manual_selection(
    env_path: Path, base_url: str, model: str
) -> None:
    """Set (or clear, when base_url/model are empty) the
    LLM_MANUAL_SELECTION line in .env (format base_url|model), preserving
    every other line. Atomic via temp file + os.replace, like
    write_llm_providers. Raises on failure."""
    line = f"LLM_MANUAL_SELECTION={base_url.rstrip('/')}|{model}" if base_url and model else ""
    text = env_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    replaced = False
    out: list[str] = []
    for ln in lines:
        if ln.strip().startswith("LLM_MANUAL_SELECTION="):
            if line and not replaced:
                out.append(line)
                replaced = True
            # Drop the line when clearing, and drop duplicates.
            continue
        out.append(ln)
    if line and not replaced:
        out.append(line)
    tmp = env_path.with_suffix(".env.tmp")
    tmp.write_text("\n".join(out) + "\n", encoding="utf-8")
    try:
        tmp.chmod(0o600)
    except Exception:
        pass
    os.replace(tmp, env_path)


def write_llm_providers(env_path: Path, entries: list[ProviderEntry]) -> None:
    """Rewrite the LLM_PROVIDERS line in .env from `entries`
    (base_url|key|model, comma-separated), preserving every other line,
    comment and blank line. Writes to a temp file in the same directory
    and atomically replaces .env, so a crash mid-write cannot corrupt
    it. Raises on failure — the caller must report it (the in-memory
    pool change stays, but a restart would revert it)."""
    line = "LLM_PROVIDERS=" + ",".join(
        f"{e.base_url.rstrip('/')}|{e.key}|{e.model}" for e in entries
    )
    text = env_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    replaced = False
    out: list[str] = []
    for ln in lines:
        if ln.strip().startswith("LLM_PROVIDERS="):
            if not replaced:
                out.append(line)
                replaced = True
            # Drop any duplicate LLM_PROVIDERS lines.
            continue
        out.append(ln)
    if not replaced:
        out.append(line)
    tmp = env_path.with_suffix(".env.tmp")
    tmp.write_text("\n".join(out) + "\n", encoding="utf-8")
    try:
        tmp.chmod(0o600)
    except Exception:
        pass
    os.replace(tmp, env_path)


@dataclass(frozen=True)
class Settings:
    # Telegram Core
    bot_token: str = field(default_factory=lambda: os.getenv("BOT_TOKEN", "").strip())
    boss_id: int = field(default_factory=lambda: int(os.getenv("BOSS_ID", "0").strip() or "0"))

    # Bot identity & locale (see bot/countries.py + bot/locale.py).
    # BOT_NAME is the wake word in groups: users say the bot's name to
    # talk to it (e.g. "Vortex dollar"). The Persian spelling "ورتکس"
    # is also accepted while the name is the default "Vortex".
    # BOT_COUNTRY / BOT_LANGUAGE are the install-time defaults; the
    # values in bot_settings (set by the installer or /admin) override
    # them at runtime, and the hardcoded defaults apply when neither
    # is set. Country and language are separate: the country drives
    # timezone, prices and prayer times; the language drives only the
    # bot's language.
    bot_name: str = field(
        default_factory=lambda: os.getenv("BOT_NAME", "Vortex").strip() or "Vortex"
    )
    bot_country: str = field(
        default_factory=lambda: os.getenv("BOT_COUNTRY", "United States").strip()
        or "United States"
    )
    bot_language: str = field(
        default_factory=lambda: os.getenv("BOT_LANGUAGE", "en").strip() or "en"
    )

    # LLM Provider Configuration (OpenAI-compatible: OpenAI, OpenRouter, Together, Local vLLM, etc.)
    llm_api_key: str = field(default_factory=lambda: os.getenv("LLM_API_KEY", "").strip())
    # Multiple keys for rotation/failover (comma-separated). Falls back to
    # the single LLM_API_KEY when empty. Add more TokenHarbor keys here.
    llm_api_keys: list[str] = field(default_factory=_llm_api_keys)
    # Multi-provider entries (base_url|key|model, comma-separated in
    # LLM_PROVIDERS). When set, this is the source of truth for the token
    # pool; the pool rotates and fails over between providers. When empty,
    # entries are built from LLM_BASE_URL + LLM_API_KEYS + LLM_MODEL.
    llm_providers: list[ProviderEntry] = field(default_factory=_parse_providers)
    # How often (seconds) every key is tested and the active key is
    # re-picked at random among healthy keys. Default 1800 = 30 min.
    token_health_check_interval_seconds: int = field(
        default_factory=lambda: int(os.getenv("TOKEN_HEALTH_CHECK_INTERVAL_SECONDS", "1800"))
    )
    # "Dead folder": JSON file where keys that stop working are quarantined.
    token_dead_path: Path = field(
        default_factory=lambda: Path(os.getenv("TOKEN_DEAD_PATH", "data/dead_tokens.json"))
    )
    # How often (seconds) quarantined keys are re-tested and revived when
    # they work again. Default 36000 = 10 h.
    token_dead_retry_interval_seconds: int = field(
        default_factory=lambda: int(os.getenv("TOKEN_DEAD_RETRY_INTERVAL_SECONDS", "36000"))
    )
    llm_base_url: str = field(
        default_factory=lambda: os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").strip()
    )
    llm_model: str = field(
        default_factory=lambda: os.getenv("LLM_MODEL", "gpt-4o-mini").strip()
    )
    # Pinned (locked) chat model, e.g. deepseek-ai/deepseek-v4.1-flash.
    # When set, the token pool keeps this model as the active entry while
    # it is healthy (no random rotation); it only falls back to another
    # healthy provider when the pinned one stops working, and returns to
    # it as soon as it recovers. Empty = random rotation as before.
    llm_pinned_model: str = field(
        default_factory=lambda: os.getenv("LLM_PINNED_MODEL", "").strip()
    )
    # The boss's manual active entry from /admin (base_url|model). Wins
    # over the pinned model while healthy; empty = no manual selection.
    llm_manual_selection: str = field(
        default_factory=lambda: os.getenv("LLM_MANUAL_SELECTION", "").strip()
    )
    llm_vision_model: str = field(
        default_factory=lambda: os.getenv("LLM_VISION_MODEL", os.getenv("LLM_MODEL", "gpt-4o-mini")).strip()
    )
    llm_temperature: float = field(
        default_factory=lambda: float(os.getenv("LLM_TEMPERATURE", "0.7"))
    )
    llm_max_tokens: int = field(
        default_factory=lambda: int(os.getenv("LLM_MAX_TOKENS", "1024"))
    )

    # Antigravity CLI (agy) provider — the local `agy` binary on this
    # server, logged in with the owner's Google account. Tried FIRST
    # for text-only turns (Gemini 3.8 -> Opus 4.6 -> GPT-OSS); the
    # token pool is the fallback when agy is disabled or fails.
    # NOTE: agy print mode conflicts with a running interactive `agy`
    # session, so never leave one running in tmux on this server.
    agy_enabled: bool = field(
        default_factory=lambda: _parse_bool(os.getenv("AGY_ENABLED"), False)
    )
    agy_timeout_seconds: float = field(
        default_factory=lambda: float(os.getenv("AGY_TIMEOUT_SECONDS", "20"))
    )

    # Search Configuration. Default is SearXNG (self-hosted, no key);
    # Tavily needs a key and is inert without one.
    search_provider: str = field(
        default_factory=lambda: os.getenv("SEARCH_PROVIDER", "searxng").strip().lower()
    )
    search_api_key: str = field(
        default_factory=lambda: os.getenv("SEARCH_API_KEY", "").strip()
    )
    search_max_results: int = field(
        default_factory=lambda: int(os.getenv("SEARCH_MAX_RESULTS", "5"))
    )

    # Dollar Rate Sources & Cache
    dollar_primary_url: str = field(
        default_factory=lambda: os.getenv(
            "DOLLAR_PRIMARY_URL", "https://api.navasan.tech/latest/?api_key="
        ).strip()
    )
    dollar_fallback_url: str = field(
        default_factory=lambda: os.getenv(
            "DOLLAR_FALLBACK_URL", "https://alanchand.com/currencies-price/usd"
        ).strip()
    )
    dollar_second_fallback_url: str = field(
        default_factory=lambda: os.getenv(
            "DOLLAR_SECOND_FALLBACK_URL", "https://www.tgju.org/profile/price_dollar_rl"
        ).strip()
    )
    dollar_cache_ttl_seconds: int = field(
        default_factory=lambda: int(os.getenv("DOLLAR_CACHE_TTL_SECONDS", "45"))
    )

    # Ban & Admin Configuration
    global_ban_default: bool = field(
        default_factory=lambda: _parse_bool(os.getenv("GLOBAL_BAN_DEFAULT"), False)
    )
    ban_commands: list[str] = field(
        default_factory=lambda: _parse_csv(
            os.getenv("BAN_COMMANDS"), ["بن", "بن کن", "بنش کن"]
        )
    )
    unban_commands: list[str] = field(
        default_factory=lambda: _parse_csv(
            os.getenv("UNBAN_COMMANDS"), ["انبنش کن", "آنبن", "انبن"]
        )
    )

    # Memory & Context Window Configuration
    database_path: Path = field(
        default_factory=lambda: Path(os.getenv("DATABASE_PATH", "data/vortex_bot.db"))
    )
    max_context_messages: int = field(
        default_factory=lambda: int(os.getenv("MAX_CONTEXT_MESSAGES", "12"))
    )
    summary_trigger_messages: int = field(
        default_factory=lambda: int(os.getenv("SUMMARY_TRIGGER_MESSAGES", "16"))
    )
    store_file_summary_in_context: bool = field(
        default_factory=lambda: _parse_bool(os.getenv("STORE_FILE_SUMMARY_IN_CONTEXT"), True)
    )

    # Rate Limiting (Boss is always exempt)
    rate_limit_requests: int = field(
        default_factory=lambda: int(os.getenv("RATE_LIMIT_REQUESTS", "6"))
    )
    rate_limit_window_seconds: int = field(
        default_factory=lambda: int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "60"))
    )

    # Daily per-user message quota (Boss is always exempt)
    daily_limit_messages: int = field(
        default_factory=lambda: int(os.getenv("DAILY_LIMIT_MESSAGES", "30"))
    )

    # Temporary Workspace & File Processing Limits
    temp_workspace_root: Path = field(
        default_factory=lambda: Path(os.getenv("TEMP_WORKSPACE_ROOT", "/tmp/vortex_workspaces"))
    )
    workspace_ttl_seconds: int = field(
        default_factory=lambda: min(600, int(os.getenv("WORKSPACE_TTL_SECONDS", "600")))
    )
    max_file_size_bytes: int = field(
        default_factory=lambda: int(os.getenv("MAX_FILE_SIZE_MB", "20")) * 1024 * 1024
    )
    max_pdf_pages: int = field(
        default_factory=lambda: int(os.getenv("MAX_PDF_PAGES", "30"))
    )
    max_table_rows: int = field(
        default_factory=lambda: int(os.getenv("MAX_TABLE_ROWS", "500"))
    )
    max_extracted_chars: int = field(
        default_factory=lambda: int(os.getenv("MAX_EXTRACTED_CHARS", "18000"))
    )
    file_process_timeout_seconds: int = field(
        default_factory=lambda: int(os.getenv("FILE_PROCESS_TIMEOUT_SECONDS", "25"))
    )

    # Paths
    system_prompt_path: Path = field(
        default_factory=lambda: Path(
            os.getenv("SYSTEM_PROMPT_PATH", "prompts/system_prompt.txt")
        )
    )

    # Self-update: daily check against the latest GitHub release.
    # UPDATE_CHECK_ENABLED=0 disables the check entirely.
    update_check_enabled: bool = field(
        default_factory=lambda: _parse_bool(os.getenv("UPDATE_CHECK_ENABLED"), True)
    )
    # "owner/repo" whose releases the updater watches. The check uses
    # the unauthenticated GitHub API, so it only works while the repo
    # is public; a private repo makes the check silently do nothing.
    update_repo: str = field(
        default_factory=lambda: os.getenv(
            "UPDATE_REPO", "VortexLabsHQ/vortex-telegram-bot"
        ).strip()
    )

    def validate(self) -> None:
        if not self.bot_token:
            raise ValueError("متغیر محیطی BOT_TOKEN تنظیم نشده است.")
        if self.boss_id <= 0:
            raise ValueError("متغیر محیطی BOSS_ID باید یک آیدی عددی معتبر تلگرام باشد.")
        if not self.llm_providers:
            raise ValueError("متغیر محیطی LLM_API_KEY تنظیم نشده است.")
        # Job intervals: clamp to sane ranges (a 0 or negative interval
        # would spin the job queue; a huge one would never run).
        # The old code silently clamped the dollar TTL to 30-60s with no
        # warning; now the effective values are logged at startup.
        if self.token_health_check_interval_seconds < 60:
            logger.warning(
                "TOKEN_HEALTH_CHECK_INTERVAL_SECONDS=%s too small; using 60s.",
                self.token_health_check_interval_seconds,
            )
            self.token_health_check_interval_seconds = 60
        if self.token_dead_retry_interval_seconds < 300:
            logger.warning(
                "TOKEN_DEAD_RETRY_INTERVAL_SECONDS=%s too small; using 300s.",
                self.token_dead_retry_interval_seconds,
            )
            self.token_dead_retry_interval_seconds = 300
        if not 5 <= self.dollar_cache_ttl_seconds <= 600:
            logger.warning(
                "DOLLAR_CACHE_TTL_SECONDS=%s out of range (5-600); using 45s.",
                self.dollar_cache_ttl_seconds,
            )
            self.dollar_cache_ttl_seconds = 45


settings = Settings()
