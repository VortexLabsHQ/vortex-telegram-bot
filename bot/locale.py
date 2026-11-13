"""Locale (i18n) system for the Vortex Telegram Bot.

One JSON file per language lives in bot/locale/<code>.json (UTF-8).
Only English (en.json) ships with full coverage for now; translations
for the other languages land later as bot/locale/<code>.json files.

Lookup rules (``t``):
  1. the requested language's file,
  2. English ("en") as the fallback,
  3. the key itself (so a missing string is visible, never a crash).

Values support ``{var}`` formatting (``t("quota.text", used=3, ...)``).
The "jokes" key is special: it is a LIST of strings, not a message —
use ``get_joke()`` to pick one at random.

The current language is resolved per call through a provider callable
(wired in main.py / handlers.py to ``Database.get_language``), so an
/admin language change applies immediately. Without a provider the
default language ("en") is used. Pass ``lang=`` explicitly to override
it for one call (used by tests and by code that formats for a fixed
language).
"""

from __future__ import annotations

import json
import logging
import random
from pathlib import Path

logger = logging.getLogger(__name__)

LOCALE_DIR = Path(__file__).resolve().parent / "locale"
DEFAULT_LANG = "en"

_FA_DIGITS = str.maketrans("0123456789.,", "۰۱۲۳۴۵۶۷۸۹٫٬")

_cache: dict[str, dict] = {}
_language_provider = None  # type: ignore[assignment]


def set_language_provider(fn) -> None:
    """Register a zero-arg callable returning the current language code.
    Called once at startup from main.py / handlers.py with
    ``Database.get_language``; before that the default language applies."""
    global _language_provider
    _language_provider = fn


def current_language() -> str:
    """The bot's current language code (e.g. "en", "fa")."""
    try:
        if _language_provider is not None:
            lang = (_language_provider() or "").strip().lower()
            if lang:
                return lang
    except Exception:
        pass
    return DEFAULT_LANG


def list_languages() -> list[str]:
    """Language codes with a locale file present, sorted ("en" first)."""
    try:
        codes = sorted(p.stem for p in LOCALE_DIR.glob("*.json"))
    except Exception:
        codes = []
    if DEFAULT_LANG in codes:
        codes.remove(DEFAULT_LANG)
        codes.insert(0, DEFAULT_LANG)
    return codes


def _load_lang(lang: str) -> dict:
    """One language file as a dict ({} when missing/unreadable)."""
    lang = (lang or "").strip().lower()
    if lang in _cache:
        return _cache[lang]
    data: dict = {}
    try:
        path = LOCALE_DIR / f"{lang}.json"
        if path.is_file():
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                data = {}
    except Exception as exc:
        logger.warning("locale %s failed to load: %s", lang, type(exc).__name__)
        data = {}
    _cache[lang] = data
    return data


class Locale:
    """Strings for one language, with the en -> key fallback chain."""

    def __init__(self, lang: str = DEFAULT_LANG) -> None:
        self.lang = (lang or DEFAULT_LANG).strip().lower() or DEFAULT_LANG

    def t(self, key: str, lang: str | None = None, **vars) -> str:
        """Localize `key`; ``{var}`` placeholders are filled from `vars`.
        Fallback: requested lang -> "en" -> the key itself. A value that
        is not a string (e.g. the "jokes" list) returns the key."""
        wanted = (lang or self.lang or DEFAULT_LANG).strip().lower()
        value = None
        for candidate in (wanted, DEFAULT_LANG):
            data = _load_lang(candidate)
            if key in data and isinstance(data[key], str):
                value = data[key]
                break
        if value is None:
            return key
        if not vars:
            return value
        try:
            return value.format(**vars)
        except Exception:
            return value

    def jokes(self, lang: str | None = None) -> list[str]:
        """The "jokes" list for a language (English fallback when the
        language has none). Never raises; [] only when en.json is gone."""
        wanted = (lang or self.lang or DEFAULT_LANG).strip().lower()
        for candidate in (wanted, DEFAULT_LANG):
            data = _load_lang(candidate)
            items = data.get("jokes")
            if isinstance(items, list) and items:
                return [str(j) for j in items if str(j).strip()]
        return []

    def has(self, key: str, lang: str | None = None) -> bool:
        """True when `key` exists as a string in the language (or en)."""
        wanted = (lang or self.lang or DEFAULT_LANG).strip().lower()
        for candidate in (wanted, DEFAULT_LANG):
            if key in _load_lang(candidate):
                return True
        return False


_default = Locale(DEFAULT_LANG)


def t(key: str, lang: str | None = None, **vars) -> str:
    """Module-level localize: uses the current language (from the
    provider) when `lang` is omitted."""
    if lang is None:
        lang = current_language()
    return _default.t(key, lang=lang, **vars)


def t_list(key: str, lang: str | None = None) -> list[str]:
    """List-valued key (e.g. "ban.done", "dollar.templates"): the list
    from the requested language, else English, else []."""
    if lang is None:
        lang = current_language()
    wanted = (lang or DEFAULT_LANG).strip().lower()
    for candidate in (wanted, DEFAULT_LANG):
        data = _load_lang(candidate)
        items = data.get(key)
        if isinstance(items, list) and items:
            return [str(v) for v in items if str(v).strip()]
    return []


def get_joke(lang: str | None = None) -> str:
    """A random joke in the current language (English fallback)."""
    if lang is None:
        lang = current_language()
    items = _default.jokes(lang=lang)
    if not items:
        return ""
    return random.choice(items)


def fmt_num(value, lang: str | None = None) -> str:
    """Format a number for user-facing text: thousands separators, and
    Persian digits when the language is Persian ("fa"), Latin otherwise.
    Ints render as-is; floats render with 2 decimals. A digit string
    (e.g. a "05:09" time) is translated digit-by-digit for Persian."""
    if lang is None:
        lang = current_language()
    is_fa = (lang or "").strip().lower() == "fa"
    if isinstance(value, str):
        if is_fa:
            return value.translate(_FA_DIGITS)
        return value
    try:
        if isinstance(value, float):
            text = f"{value:,.2f}"
        else:
            text = f"{int(value):,}"
    except (TypeError, ValueError):
        return str(value)
    if is_fa:
        return text.translate(_FA_DIGITS)
    return text


def fmt_pct(value: float, lang: str | None = None) -> str:
    """A percentage magnitude with up to 2 decimals, localized digits."""
    try:
        text = f"{abs(float(value)):.2f}".rstrip("0").rstrip(".")
    except (TypeError, ValueError):
        return str(value)
    if (lang or current_language()).strip().lower() == "fa":
        return text.translate(_FA_DIGITS)
    return text
