"""
Fun + useful extras for Vortex Bot — Hafez fortune, news, prayer times,
calculator, dice, coin flip, jokes.

Free sources, no API key needed (all verified reachable from the server):
  - Ganjoor https://api.ganjoor.net/api/ganjoor/hafez/faal
      random Hafez ghazal (فال حافظ).
  - BBC RSS: Persian (https://feeds.bbci.co.uk/persian/rss.xml) when the
    bot language is Persian, otherwise BBC News
    (https://feeds.bbci.co.uk/news/rss.xml) — top headlines.
  - AlAdhan https://api.aladhan.com/v1/timingsByCity
      prayer times by city + country (the country's capital by
      default; the calculation method follows the country).

Calculator, dice, coin and jokes are pure code (no network). Jokes come
from the current language's "jokes" list in bot/locale/ (English
fallback). Public functions never raise (None / fallback text on failure).
"""

from __future__ import annotations

import ast
import logging
import random
import re
import time
import xml.etree.ElementTree as ET

import httpx

from bot.countries import country_now, current_country, prayer_method
from bot.locale import fmt_num, get_joke as _locale_joke, t
from bot.prices import (
    _GREGORIAN_MONTHS_FA,
    _JALALI_MONTHS,
    _PERSIAN_WEEKDAYS,
    gregorian_to_jalali,
)
from bot.security import get_wake_word, normalize_persian

logger = logging.getLogger(__name__)

_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

GANJOOR_FAAL_URL = "https://api.ganjoor.net/api/ganjoor/hafez/faal"
BBC_PERSIAN_RSS_URL = "https://feeds.bbci.co.uk/persian/rss.xml"
BBC_NEWS_RSS_URL = "https://feeds.bbci.co.uk/news/rss.xml"
ALADHAN_TIMINGS_BY_CITY_URL = "https://api.aladhan.com/v1/timingsByCity"

NEWS_CACHE_TTL = 900  # seconds (15 min)
PRAYER_CACHE_TTL = 3600  # seconds (1 hour)

# Persian city name -> English name for the AlAdhan API (it geocodes
# Latin-script city names; a Persian-script name may not resolve).
_PERSIAN_CITY_NAMES: dict[str, str] = {
    "تهران": "Tehran",
    "مشهد": "Mashhad",
    "اصفهان": "Isfahan",
    "شیراز": "Shiraz",
    "تبریز": "Tabriz",
    "کرج": "Karaj",
    "قم": "Qom",
    "اهواز": "Ahvaz",
    "رشت": "Rasht",
    "یزد": "Yazd",
}

# Fallback Hafez couplets when the Ganjoor API is unreachable.
_FAAL_FALLBACK = [
    (
        "غزل شمارهٔ ۱",
        "الا یا ایها الساقی ادر کاسا و ناولها\n"
        "که عشق آسان نمود اول ولی افتاد مشکل‌ها",
    ),
    (
        "غزل شمارهٔ ۲",
        "صلاح کار کجا و من خراب کجا\n"
        "ببین تفاوت ره کز کجاست تا به کجا",
    ),
    (
        "غزل شمارهٔ ۳",
        "اگر آن ترک شیرازی به دست آرد دل ما را\n"
        "به خال هندویش بخشم سمرقند و بخارا را",
    ),
]

# ======================================================================
# فال حافظ (Ganjoor random ghazal)
# ======================================================================

async def fetch_faal() -> tuple[str, str] | None:
    """Return (title, poem text) for a random Hafez ghazal, or None.

    No cache — every call is a fresh random faal. Falls back to a
    hardcoded couplet when the API is unreachable.
    """
    try:
        async with httpx.AsyncClient(timeout=15, headers={"User-Agent": _UA}) as c:
            r = await c.get(GANJOOR_FAAL_URL)
        if r.status_code != 200:
            raise ValueError(f"Ganjoor HTTP {r.status_code}")
        data = r.json()
        title = (data.get("title") or "فال حافظ").strip()
        text = (data.get("plainText") or "").replace("\r\n", "\n").strip()
        if not text:
            raise ValueError("empty poem")
        if len(text) > 1200:
            text = text[:1200].rstrip() + "…"
        return title, text
    except Exception as exc:
        logger.warning("faal fetch failed, using fallback: %s", exc)
        title, text = random.choice(_FAAL_FALLBACK)
        return title, text


def format_faal(faal: tuple[str, str] | None) -> str:
    if not faal:
        return t("faal.failed")
    title, text = faal
    return t("faal.title", title=title) + f"\n\n{text}"


# ======================================================================
# اخبار (BBC Persian RSS, top 5)
# ======================================================================

_news_cache: dict[str, object] = {"at": 0.0, "items": []}


async def fetch_news() -> list[dict]:
    """Top 5 headlines [{title, link}], cached 15 minutes. The source
    follows the bot language: BBC Persian for Persian, BBC News
    otherwise."""
    from bot.locale import current_language

    url = BBC_PERSIAN_RSS_URL if current_language() == "fa" else BBC_NEWS_RSS_URL
    now = time.time()
    if now - float(_news_cache["at"]) < NEWS_CACHE_TTL and _news_cache["items"]:
        return list(_news_cache["items"])  # type: ignore[arg-type]
    items: list[dict] = []
    try:
        async with httpx.AsyncClient(timeout=15, headers={"User-Agent": _UA}) as c:
            r = await c.get(url)
        if r.status_code != 200:
            raise ValueError(f"news RSS HTTP {r.status_code}")
        root = ET.fromstring(r.content)
        channel = root.find("channel")
        if channel is None:
            raise ValueError("no channel in RSS")
        for item in channel.findall("item")[:5]:
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            if title:
                items.append({"title": title[:90], "link": link})
        if not items:
            raise ValueError("no items in RSS")
    except Exception as exc:
        logger.warning("news fetch failed: %s", exc)
        return []
    _news_cache["at"] = now
    _news_cache["items"] = items
    return list(items)


def format_news(items: list[dict]) -> str:
    if not items:
        return t("news.failed")
    from bot.locale import current_language

    source = (
        t("news.source_fa") if current_language() == "fa" else t("news.source_en")
    )
    lines = [t("news.title", source=source)]
    for i, it in enumerate(items, 1):
        lines.append(f"{fmt_num(i)}. {it['title']}")
        if it.get("link"):
            lines.append(it["link"])
        lines.append("")
    return "\n".join(lines).strip()


# ======================================================================
# اوقات شرعی (AlAdhan, method 7 = Tehran)
# ======================================================================

_prayer_cache: dict[tuple[str, str, str], tuple[float, dict]] = {}


def _api_city_name(city: str) -> str:
    """City name for the AlAdhan API: Persian names map to their
    English spelling (the API geocodes Latin-script names)."""
    return _PERSIAN_CITY_NAMES.get(normalize_persian(city).strip(), city.strip())


def prayer_url(city: str, country: str, method: int, date: str) -> str:
    """AlAdhan timingsByCity URL for one day (date "DD-MM-YYYY").
    Pure builder (no network) so tests can check the URL shape."""
    from urllib.parse import quote

    return (
        f"{ALADHAN_TIMINGS_BY_CITY_URL}/{date}"
        f"?city={quote(city)}&country={quote(country)}&method={method}"
    )


async def fetch_prayer_times(city: str | None) -> tuple[str, dict] | None:
    """Return (city display name, timings dict) for today in the
    country's timezone. `city` is the user's city when given, else the
    current country's capital; the calculation method follows the
    country. Timings keys: Fajr, Sunrise, Dhuhr, Asr, Sunset, Maghrib,
    Isha, Midnight. Cached 1 hour per city+country+day. None on failure.
    """
    country = current_country()
    display = (city or "").strip() or country.capital
    api_city = _api_city_name(display)
    now = time.time()
    today = country_now(country.name)
    date_key = today.strftime("%Y-%m-%d")
    cache_key = (display, country.name, date_key)
    cached = _prayer_cache.get(cache_key)
    if cached and now - cached[0] < PRAYER_CACHE_TTL:
        return display, cached[1]
    try:
        date_str = today.strftime("%d-%m-%Y")
        url = prayer_url(
            api_city, country.name, prayer_method(country.name), date_str
        )
        async with httpx.AsyncClient(timeout=15, headers={"User-Agent": _UA}) as c:
            r = await c.get(url)
        if r.status_code != 200:
            raise ValueError(f"AlAdhan HTTP {r.status_code}")
        data = r.json()
        timings = (data.get("data") or {}).get("timings") or {}
        if not timings.get("Fajr"):
            raise ValueError("no timings in response")
        _prayer_cache[cache_key] = (now, timings)
        return display, timings
    except Exception as exc:
        logger.warning("prayer times fetch failed: %s", exc)
        return None


def format_prayer_times(result: tuple[str, dict] | None) -> str:
    if not result:
        return t("prayer.failed")
    name, timings = result
    country = current_country()
    dt = country_now(country.name)
    # Jalali date is Iran-specific; other countries get the Gregorian
    # date in the bot's language.
    if country.name == "Iran":
        try:
            jy, jm, jd = gregorian_to_jalali(dt.year, dt.month, dt.day)
            date_line = (
                f"{_PERSIAN_WEEKDAYS[dt.weekday()]} {fmt_num(jd)} "
                f"{_JALALI_MONTHS[jm - 1]} {fmt_num(jy)}"
            )
        except Exception:
            date_line = ""
    else:
        try:
            from bot.locale import current_language

            if current_language() == "fa":
                date_line = (
                    f"{_PERSIAN_WEEKDAYS[dt.weekday()]} {fmt_num(dt.day)} "
                    f"{_GREGORIAN_MONTHS_FA[dt.month - 1]} {fmt_num(dt.year)}"
                )
            else:
                date_line = dt.strftime("%A, %d %B %Y")
        except Exception:
            date_line = ""
    labels = [
        ("Fajr", t("prayer.fajr")),
        ("Sunrise", t("prayer.sunrise")),
        ("Dhuhr", t("prayer.dhuhr")),
        ("Asr", t("prayer.asr")),
        ("Sunset", t("prayer.sunset")),
        ("Maghrib", t("prayer.maghrib")),
        ("Isha", t("prayer.isha")),
        ("Midnight", t("prayer.midnight")),
    ]
    header = t("prayer.title", city=name)
    if date_line:
        header = t("prayer.title_date", city=name, date=date_line)
    lines = [header, ""]
    for key, label in labels:
        value = timings.get(key)
        if value:
            # AlAdhan returns "05:09 (IRST)" style in some cases; keep HH:MM.
            hhmm = value.split(" ")[0]
            lines.append(f"{label}: {fmt_num(hhmm)}")
    return "\n".join(lines)


# ======================================================================
# ماشین حساب (safe arithmetic, Persian digits + Persian words)
# ======================================================================

_PERSIAN_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
_ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")

_CALC_WORDS = [
    ("به توان", "**"),
    ("ضرب در", "*"),
    ("ضربدر", "*"),
    ("تقسیم بر", "/"),
    ("تقسیم", "/"),
    ("به علاوه", "+"),
    ("بعلاوه", "+"),
    ("منهای", "-"),
    ("منها", "-"),
    ("×", "*"),
    ("✕", "*"),
    ("÷", "/"),
]


def _eval_node(node: ast.AST) -> float:
    """Evaluate an AST node; only numbers and + - * / % ** ( ) allowed."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise ValueError("bad constant")
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Mod):
            return left % right
        if isinstance(node.op, ast.Pow):
            if abs(right) > 100 or abs(left) > 1e6:
                raise ValueError("power too large")
            # A negative base with a fractional exponent is a complex
            # number in Python ((-8) ** 0.5) — reject it instead of
            # returning a complex that crashes format_calc.
            if left < 0 and right != int(right):
                raise ValueError("complex result")
            return left**right
        raise ValueError("bad operator")
    if isinstance(node, ast.UnaryOp):
        value = _eval_node(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +value
        if isinstance(node.op, ast.USub):
            return -value
        raise ValueError("bad unary")
    raise ValueError("unsupported expression")


def calc(expr: str | None) -> float | None:
    """Safely evaluate an arithmetic expression (Persian digits/words OK).

    Returns None when the expression is empty or invalid.
    """
    if not expr:
        return None
    s = normalize_persian(expr)
    s = s.translate(_PERSIAN_DIGITS).translate(_ARABIC_DIGITS)
    for word, op in _CALC_WORDS:
        s = s.replace(word, op)
    # Map the operators users actually type before filtering: '^' is
    # power, 'x' is multiplication, '٫' is the Persian decimal point.
    # The old code silently DELETED them, so 2^10 became 210, 3x4 became
    # 34 and ۲٫۵*۲ became 50 — confident but wrong answers.
    s = s.replace("^", "**").replace("x", "*").replace("X", "*").replace("٫", ".")
    before = s
    s = re.sub(r"[^0-9+\-*/%().\s]", "", s).strip()
    # If anything (other than whitespace) was removed, the expression
    # contained something we don't understand — refuse instead of
    # silently computing a different expression.
    if re.sub(r"\s", "", before) != re.sub(r"\s", "", s):
        return None
    if not s or not re.search(r"\d", s):
        return None
    try:
        tree = ast.parse(s, mode="eval")
        result = _eval_node(tree)
    except Exception:
        return None
    if isinstance(result, complex):
        return None
    if result != result or result in (float("inf"), float("-inf")):
        return None
    return result


def format_calc(expr: str, result: float | None) -> str:
    if result is None or isinstance(result, complex):
        return t("calc.failed", bot=get_wake_word())
    if result == int(result) and abs(result) < 10**15:
        shown = fmt_num(int(result))
    else:
        shown = fmt_num(f"{result:.6f}".rstrip("0").rstrip("."))
    return t("calc.result", result=shown)


# ======================================================================
# تاس، سکه، جوک (pure chance / locale jokes)
# ======================================================================

def roll_dice() -> int:
    return random.randint(1, 6)


def format_dice(n: int) -> str:
    if n == 6:
        return t("dice.six", n=fmt_num(n))
    return t("dice.text", n=fmt_num(n))


def flip_coin() -> str:
    return random.choice(["heads", "tails"])


def format_coin(side: str) -> str:
    label = t("coin.heads") if side == "heads" else t("coin.tails")
    return t("coin.text", side=label)


def get_joke() -> str:
    """A random joke from the current language's locale list
    (English fallback)."""
    return _locale_joke()
