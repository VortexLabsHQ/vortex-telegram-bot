"""
Live market prices, local time / date, and weather for Vortex Bot.

Free sources, no API key needed (all verified reachable from the server):
  - TGJU https://call1.tgju.org/ajax.json
      fiat currencies + gold/coins in Toman (IRAN ONLY).
  - Frankfurter https://api.frankfurter.dev/v1/latest
      FX rates vs USD (units per 1 USD).
  - gold-api https://api.gold-api.com/price/XAU
      live gold spot in USD per troy ounce (free, no key; verified
      live 2026-11-13: {"price": 3885.87, "currency": "USD", ...}).
  - datahub.io EIA Brent daily CSV
      https://datahub.io/core/oil-prices/_r/-/data/brent-daily.csv
      (columns Date,Price; USD per barrel; a DAILY settlement series,
      usually one day behind — not intraday).
  - Nobitex https://apiv2.nobitex.ir/market/stats
      BTC/ETH/USDT/DOGE/TRX in Rial (IRAN ONLY).
  - CoinGecko https://api.coingecko.com/api/v3/simple/price
      crypto prices in USD.
  - Open-Meteo geocoding + forecast (weather by city name).

Country-aware: when the bot country is Iran, fiat/gold come from TGJU
(Toman) and crypto from Nobitex (Toman). For every other country,
fiat/gold/oil/crypto are priced in USD and converted to the LOCAL
currency with the Frankfurter USD rate (5-minute cache). Crypto stays
in USD with the local-currency equivalent shown alongside. All output
uses the local currency code (Toman for IRR). If a source fails, the
previous cached value is kept (or the row is omitted) — never a crash.

Everything is formatted with locale-aware digits (Persian digits for
fa, Latin otherwise). The market bundle (TGJU + Frankfurter + Nobitex
+ CoinGecko + gold + oil) is cached for 5 minutes; weather is cached
10 minutes per city. Public functions never raise (empty lists / None
on failure).
"""

from __future__ import annotations

import asyncio
import logging
import time
from datetime import datetime

import httpx

from bot.countries import country_now, country_timezone, currency_code, current_country
from bot.locale import current_language, fmt_num, fmt_pct, t
from bot.security import normalize_persian

logger = logging.getLogger(__name__)

_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

TGJU_URL = "https://call1.tgju.org/ajax.json"
FRANKFURTER_URL = "https://api.frankfurter.dev/v1/latest"
GOLD_API_URL = "https://api.gold-api.com/price/XAU"
OIL_CSV_URL = "https://datahub.io/core/oil-prices/_r/-/data/brent-daily.csv"
NOBITEX_URL = (
    "https://apiv2.nobitex.ir/market/stats"
    "?srcCurrency=btc,eth,usdt,doge,trx&dstCurrency=rls"
)
COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

MARKET_CACHE_TTL = 300  # seconds
WEATHER_CACHE_TTL = 600  # seconds
FX_CACHE_TTL = 300  # seconds

# (TGJU key, locale label key, ISO code)
FIAT = [
    ("price_dollar_rl", "prices.label.usd", "USD"),
    ("price_eur", "prices.label.eur", "EUR"),
    ("price_gbp", "prices.label.gbp", "GBP"),
    ("price_cny", "prices.label.cny", "CNY"),
    ("price_aed", "prices.label.aed", "AED"),
    ("price_try", "prices.label.try", "TRY"),
]
# (TGJU key, locale label key) — Iran only (TGJU gold/coins).
GOLD = [
    ("geram18", "prices.label.gold_18k"),
    ("mesghal", "prices.label.mesghal"),
    ("sekee", "prices.label.sekee"),
    ("sekeb", "prices.label.sekeb"),
    ("nim", "prices.label.nim"),
    ("rob", "prices.label.rob"),
]
# (Nobitex/CoinGecko key, locale label key, CoinGecko id)
CRYPTO = [
    ("btc", "prices.label.btc", "bitcoin"),
    ("eth", "prices.label.eth", "ethereum"),
    ("usdt", "prices.label.usdt", "tether"),
    ("doge", "prices.label.doge", "dogecoin"),
    ("trx", "prices.label.trx", "tron"),
]

# Troy ounce in grams (gold is quoted per troy ounce).
TROY_OUNCE_GRAMS = 31.1035

# Normalized name -> ISO code (keys are passed through normalize_persian
# at lookup time; both آ/ا spellings are listed where they differ).
_CURRENCY_ALIASES = {
    "دلار": "USD",
    "دلار امریکا": "USD",
    "دلار آمریکا": "USD",
    "usd": "USD",
    "dollar": "USD",
    "یورو": "EUR",
    "یورو اروپا": "EUR",
    "eur": "EUR",
    "euro": "EUR",
    "پوند": "GBP",
    "پوند انگلیس": "GBP",
    "پوند انگلستان": "GBP",
    "gbp": "GBP",
    "pound": "GBP",
    "درهم": "AED",
    "درهم امارات": "AED",
    "aed": "AED",
    "dirham": "AED",
    "لیر": "TRY",
    "لیر ترکیه": "TRY",
    "try": "TRY",
    "lira": "TRY",
    "یوان": "CNY",
    "یوان چین": "CNY",
    "cny": "CNY",
    "yuan": "CNY",
}

# Open-Meteo weather code -> locale label key.
_WEATHER_CODES = {
    0: "prices.weather.clear",
    1: "prices.weather.mostly_clear",
    2: "prices.weather.partly_cloudy",
    3: "prices.weather.cloudy",
    45: "prices.weather.fog",
    48: "prices.weather.fog",
    51: "prices.weather.drizzle",
    53: "prices.weather.drizzle",
    55: "prices.weather.drizzle",
    56: "prices.weather.freezing_drizzle",
    57: "prices.weather.freezing_drizzle",
    61: "prices.weather.rain",
    63: "prices.weather.rain",
    65: "prices.weather.rain",
    66: "prices.weather.freezing_rain",
    67: "prices.weather.freezing_rain",
    71: "prices.weather.snow",
    73: "prices.weather.snow",
    75: "prices.weather.snow",
    77: "prices.weather.snow_grains",
    80: "prices.weather.rain_showers",
    81: "prices.weather.rain_showers",
    82: "prices.weather.rain_showers",
    85: "prices.weather.snow_showers",
    86: "prices.weather.snow_showers",
    95: "prices.weather.thunderstorm",
    96: "prices.weather.thunderstorm_hail",
    99: "prices.weather.thunderstorm_hail",
}

_JALALI_MONTHS = [
    "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند",
]
# Transliterated Jalali month names (proper nouns, used when the bot
# language is not Persian).
_JALALI_MONTHS_EN = [
    "Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar",
    "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand",
]
# Index = datetime.weekday() (Monday=0 .. Sunday=6)
_PERSIAN_WEEKDAYS = [
    "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یک‌شنبه",
]
_GREGORIAN_MONTHS_FA = [
    "ژانویه", "فوریه", "مارس", "آوریل", "مه", "ژوئن",
    "ژوئیه", "اوت", "سپتامبر", "اکتبر", "نوامبر", "دسامبر",
]

# One shared 5-minute cache for the whole market bundle (rows, not text).
_market_cache: dict = {"ts": 0.0, "fiat": [], "gold": [], "crypto": [], "oil": [], "updated": ""}
# Per-city weather cache: key -> (ts, result dict)
_weather_cache: dict[str, tuple[float, dict]] = {}
# USD -> local currency rate cache: (currency, ts, rate)
_fx_cache: dict[str, tuple[float, float]] = {}


def currency_label(code: str | None = None) -> str:
    """Display name for a currency in user-facing prices: "Toman" for
    IRR (Toman is the colloquial unit, IRR/10), the ISO code otherwise."""
    code = code or currency_code()
    if code == "IRR":
        return t("prices.currency.toman")
    return code


def fa_num(n) -> str:
    """Format a number with thousands separators, in the current
    language's digits (Persian for fa, Latin otherwise). Ints render
    as-is; floats render with 2 decimals (for USD values)."""
    return fmt_num(n)


def _fmt_pct(value: float) -> str:
    """Format a percentage magnitude with up to 2 decimals, localized digits."""
    return fmt_pct(value)


def _change_suffix(change_pct) -> str:
    """' 🔺 2.5%' / ' 🔻 1.2%' / '' (minus sign stripped, like the Rubika bot)."""
    if change_pct is None:
        return ""
    try:
        v = float(str(change_pct).replace("٬", "").replace(",", ""))
    except (TypeError, ValueError):
        return ""
    if v > 0:
        return t("prices.change_up", pct=_fmt_pct(v))
    if v < 0:
        return t("prices.change_down", pct=_fmt_pct(v))
    return ""


def _fmt_temp(value) -> str:
    """Temperature: 18 -> '18', 18.5 -> '18.5' (localized digits)."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        return str(value)
    if v == int(v):
        return fmt_num(str(int(v)))
    return fmt_num(f"{v:.1f}")


# ----------------------------------------------------------------------
# Jalali calendar (pure Python, no dependency)
# ----------------------------------------------------------------------

def gregorian_to_jalali(gy: int, gm: int, gd: int) -> tuple[int, int, int]:
    """Convert a Gregorian date to (Jalali year, month, day).

    Standard arithmetic algorithm (same as jalaali-js). Verified against
    2025-03-20 = 1403-12-30 and 2026-03-21 = 1405-01-01.
    """
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if gy <= 1600:
        jy = 0
        gy -= 621
    else:
        jy = 979
        gy -= 1600
    gy2 = gy + 1 if gm > 2 else gy
    days = (
        (365 * gy)
        + ((gy2 + 3) // 4)
        - ((gy2 + 99) // 100)
        + ((gy2 + 399) // 400)
        - 80
        + gd
        + g_d_m[gm - 1]
    )
    jy += 33 * (days // 12053)
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if days < 186:
        jm = 1 + (days // 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + ((days - 186) // 30)
        jd = 1 + ((days - 186) % 30)
    return jy, jm, jd


def tehran_now_text(now: datetime | None = None) -> str:
    """Local time + date in the bot's country (kept the old name for
    compatibility; the timezone now follows the configured country).

    Iran: Jalali date + Gregorian date in parentheses (Persian month /
    weekday names when the bot language is Persian, transliterated /
    English names otherwise). Other countries: Gregorian date only.

    Example (Iran, fa):
        🕐 Time in Tehran: 14:32:05
        📅 Today: سه‌شنبه ۱۹ آبان ۱۴۰۵ (۱۹ نوامبر ۲۰۲۶)
    Never raises (falls back to local time on ZoneInfo failure).
    """
    country = current_country()
    try:
        tz = country_timezone(country.name)
        dt = now.astimezone(tz) if now is not None else datetime.now(tz)
    except Exception:
        dt = now or datetime.now()
    try:
        time_str = fmt_num(dt.strftime("%H:%M:%S"))
        title = t("prices.time_title", city=country.capital, time=time_str)
        lang = current_language()
        if country.name == "Iran":
            jy, jm, jd = gregorian_to_jalali(dt.year, dt.month, dt.day)
            if lang == "fa":
                date = (
                    f"{_PERSIAN_WEEKDAYS[dt.weekday()]} {fmt_num(jd)} "
                    f"{_JALALI_MONTHS[jm - 1]} {fmt_num(jy)} "
                    f"({fmt_num(dt.day)} {_GREGORIAN_MONTHS_FA[dt.month - 1]} "
                    f"{fmt_num(dt.year)})"
                )
            else:
                date = (
                    f"{dt.strftime('%A')} {jd} {_JALALI_MONTHS_EN[jm - 1]} {jy} "
                    f"({dt.day} {dt.strftime('%B')} {dt.year})"
                )
        elif lang == "fa":
            date = (
                f"{_PERSIAN_WEEKDAYS[dt.weekday()]} {fmt_num(dt.day)} "
                f"{_GREGORIAN_MONTHS_FA[dt.month - 1]} {fmt_num(dt.year)}"
            )
        else:
            date = dt.strftime("%A, %d %B %Y")
        return f"{title}\n{t('prices.time_date', date=date)}"
    except Exception:
        logger.warning("tehran_now_text failed: %s", "format-error")
        return t("prices.time_unknown", city=country.capital)


# ----------------------------------------------------------------------
# Fetching (httpx, never raises from public functions)
# ----------------------------------------------------------------------

def _rials_to_toman(value) -> int | None:
    try:
        return int(str(value).replace(",", "").strip()) // 10
    except (TypeError, ValueError):
        return None


async def _get_json(client: httpx.AsyncClient, url: str, params: dict | None = None):
    resp = await client.get(url, params=params)
    resp.raise_for_status()
    return resp.json()


async def _fetch_tgju(client: httpx.AsyncClient):
    """Returns (fiat_partial, gold_rows, updated_str). fiat_partial rows
    lack usd_per_unit (merged later from Frankfurter). Amounts are in
    Toman (Iran path); "local" is the amount in the local currency
    (Toman here), "toman" is kept as an alias."""
    try:
        data = await _get_json(client, TGJU_URL)
        cur = data.get("current", {}) if isinstance(data, dict) else {}
        fiat: list[dict] = []
        for key, label_key, code in FIAT:
            item = cur.get(key) or {}
            toman = _rials_to_toman(item.get("p")) if item.get("p") else None
            if toman is None:
                continue
            fiat.append(
                {
                    "label_key": label_key,
                    "code": code,
                    "local": toman,
                    "toman": toman,
                    "usd_per_unit": None,
                    "change_pct": item.get("dp"),
                }
            )
        gold: list[dict] = []
        for key, label_key in GOLD:
            item = cur.get(key) or {}
            toman = _rials_to_toman(item.get("p")) if item.get("p") else None
            if toman is None:
                continue
            gold.append(
                {
                    "label_key": label_key,
                    "local": toman,
                    "toman": toman,
                    "change_pct": item.get("dp"),
                }
            )
        updated = (cur.get("price_dollar_rl") or {}).get("t", "") or ""
        return fiat, gold, updated
    except Exception as exc:
        logger.warning("TGJU fetch failed: %s", type(exc).__name__)
        return [], [], ""


async def _fetch_frankfurter(
    client: httpx.AsyncClient, symbols: str = "EUR,GBP,AED,TRY,CNY"
) -> dict[str, float]:
    """Returns {ISO code: USD value of one unit} (USD itself = 1.0).
    `symbols` are the non-USD codes to fetch (comma-separated)."""
    try:
        data = await _get_json(
            client,
            FRANKFURTER_URL,
            params={"base": "USD", "symbols": symbols},
        )
        rates = data.get("rates", {}) if isinstance(data, dict) else {}
        out: dict[str, float] = {"USD": 1.0}
        for code, per_usd in rates.items():
            try:
                v = float(per_usd)
                if v > 0:
                    out[str(code).upper()] = 1.0 / v
            except (TypeError, ValueError):
                continue
        return out
    except Exception as exc:
        logger.warning("Frankfurter fetch failed: %s", type(exc).__name__)
        return {}


async def _fetch_gold_usd(client: httpx.AsyncClient) -> dict:
    """Live gold spot from gold-api.com (free, no key): USD per troy
    ounce. Returns {"usd_per_oz": float} or {} on failure."""
    try:
        data = await _get_json(client, GOLD_API_URL)
        price = float((data or {}).get("price", 0) or 0)
        if price <= 0:
            raise ValueError("no gold price in response")
        return {"usd_per_oz": price}
    except Exception as exc:
        logger.warning("gold-api fetch failed: %s", type(exc).__name__)
        return {}


async def _fetch_oil_usd(client: httpx.AsyncClient) -> dict:
    """Latest Brent crude spot from the EIA daily series (datahub.io,
    free, no key): USD per barrel + the settlement date. Returns
    {"usd_per_barrel": float, "date": "YYYY-MM-DD"} or {} on failure.
    The series is daily, so the price is usually one day behind."""
    try:
        resp = await client.get(OIL_CSV_URL)
        resp.raise_for_status()
        # Last valid "YYYY-MM-DD,price" row wins (the file is ~18k rows).
        for line in reversed(resp.text.splitlines()):
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 2:
                continue
            date, price = parts
            if len(date) != 10 or date[4] != "-" or date[7] != "-":
                continue
            try:
                value = float(price)
            except ValueError:
                continue
            if value > 0:
                return {"usd_per_barrel": value, "date": date}
        raise ValueError("no valid oil row in CSV")
    except Exception as exc:
        logger.warning("oil CSV fetch failed: %s", type(exc).__name__)
        return {}


async def _fetch_nobitex(client: httpx.AsyncClient) -> dict[str, dict]:
    """Returns {key: {"toman": int, "change_pct": ...}} for crypto."""
    try:
        data = await _get_json(client, NOBITEX_URL)
        stats = data.get("stats", {}) if isinstance(data, dict) else {}
        out: dict[str, dict] = {}
        for key, _label, _cg_id in CRYPTO:
            item = stats.get(f"{key}-rls") or {}
            if not item.get("latest"):
                continue
            try:
                toman = int(item["latest"]) // 10
            except (TypeError, ValueError):
                continue
            out[key] = {"toman": toman, "change_pct": item.get("dayChange")}
        return out
    except Exception as exc:
        logger.warning("Nobitex fetch failed: %s", type(exc).__name__)
        return {}


async def _fetch_coingecko(client: httpx.AsyncClient) -> dict[str, float]:
    """Returns {coingecko id: USD price}."""
    try:
        ids = ",".join(cg_id for _key, _label, cg_id in CRYPTO)
        data = await _get_json(
            client, COINGECKO_URL, params={"ids": ids, "vs_currencies": "usd"}
        )
        out: dict[str, float] = {}
        if isinstance(data, dict):
            for _key, _label, cg_id in CRYPTO:
                item = data.get(cg_id) or {}
                try:
                    out[cg_id] = float(item["usd"])
                except (TypeError, ValueError, KeyError):
                    continue
        return out
    except Exception as exc:
        logger.warning("CoinGecko fetch failed: %s", type(exc).__name__)
        return {}


async def usd_to_local_rate() -> float | None:
    """Local-currency units per 1 USD (Frankfurter, 5-min cache).
    None when the rate cannot be fetched. For Iran this is None —
    the IRR rate comes from TGJU instead (Frankfurter has no IRR)."""
    code = currency_code()
    if code == "IRR":
        return None
    now = time.monotonic()
    cached = _fx_cache.get(code)
    if cached and now - cached[0] < FX_CACHE_TTL:
        return cached[1]
    rate: float | None = None
    try:
        async with httpx.AsyncClient(timeout=10.0, headers={"User-Agent": _UA}) as client:
            data = await _get_json(
                client,
                FRANKFURTER_URL,
                params={"base": "USD", "symbols": code},
            )
            per_usd = (data.get("rates", {}) or {}).get(code)
            if per_usd:
                rate = float(per_usd)
    except Exception as exc:
        logger.warning("FX fetch failed: %s", type(exc).__name__)
    if rate is not None and rate > 0:
        _fx_cache[code] = (now, rate)
        return rate
    if cached:
        return cached[1]
    return None


def _oil_rows(oil_usd: dict, local_per_usd: float | None) -> list[dict]:
    """One Brent row in the local currency from {"usd_per_barrel",
    "date"} (or [] when either input is missing)."""
    if not oil_usd or not local_per_usd:
        return []
    try:
        usd = float(oil_usd["usd_per_barrel"])
    except (KeyError, TypeError, ValueError):
        return []
    if usd <= 0:
        return []
    return [
        {
            "label_key": "prices.label.oil_brent",
            "local": round(usd * local_per_usd, 2),
            "usd": usd,
            "date": oil_usd.get("date", ""),
            "change_pct": None,
        }
    ]


async def fetch_market_bundle() -> dict:
    """Fetch (or reuse the 5-minute cache of) the whole market bundle:
    {"fiat": [...], "gold": [...], "crypto": [...], "oil": [...],
    "updated": str}. Never raises.

    Iran: TGJU (fiat + gold in Toman) + Nobitex (crypto in Toman) +
    CoinGecko (crypto USD) + Frankfurter (USD values) + Brent oil in
    Toman (Brent USD x TGJU dollar rate).
    Other countries: Frankfurter (fiat in local currency) + gold-api
    (gold per gram/ounce in local currency) + CoinGecko (crypto USD x
    local rate) + Brent oil in local currency.
    """
    now = time.monotonic()
    if _market_cache["ts"] and now - _market_cache["ts"] < MARKET_CACHE_TTL:
        return _market_cache
    country = current_country()
    is_iran = country.name == "Iran"
    local_code = country.currency
    fiat: list[dict] = []
    gold: list[dict] = []
    crypto: list[dict] = []
    oil: list[dict] = []
    updated = ""
    try:
        async with httpx.AsyncClient(timeout=10.0, headers={"User-Agent": _UA}) as client:
            if is_iran:
                results = await asyncio.gather(
                    _fetch_tgju(client),
                    _fetch_frankfurter(client),
                    _fetch_nobitex(client),
                    _fetch_coingecko(client),
                    _fetch_oil_usd(client),
                )
                # results[0] is the TGJU 3-tuple (fiat rows, gold rows, updated).
                fiat_partial, gold, updated = results[0]
                frank = results[1]
                nobi = results[2]
                gecko = results[3]
                oil_usd = results[4]
                for row in fiat_partial:
                    usd = frank.get(row["code"])
                    row["usd_per_unit"] = usd
                    fiat.append(row)
                usd_toman = None
                for row in fiat:
                    if row.get("code") == "USD":
                        usd_toman = row.get("local")
                        break
                oil = _oil_rows(oil_usd, float(usd_toman) if usd_toman else None)
                for key, label_key, cg_id in CRYPTO:
                    item = nobi.get(key)
                    if not item:
                        continue
                    crypto.append(
                        {
                            "label_key": label_key,
                            "local": item["toman"],
                            "toman": item["toman"],
                            "usd": gecko.get(cg_id),
                            "change_pct": item.get("change_pct"),
                        }
                    )
            else:
                symbols = ",".join(
                    sorted({c for _k, _l, c in FIAT if c != "USD"} | {local_code})
                )
                results = await asyncio.gather(
                    _fetch_frankfurter(client, symbols=symbols),
                    _fetch_coingecko(client),
                    _fetch_gold_usd(client),
                    _fetch_oil_usd(client),
                )
                frank = results[0]
                gecko = results[1]
                gold_usd = results[2]
                oil_usd = results[3]
                # Frankfurter returns USD value of one unit; invert for
                # local units per USD.
                usd_value = frank.get(local_code)
                local_per_usd = (1.0 / usd_value) if usd_value else None
                if local_per_usd:
                    for _key, label_key, code in FIAT:
                        usd = frank.get(code)
                        if usd is None:
                            continue
                        fiat.append(
                            {
                                "label_key": label_key,
                                "code": code,
                                "local": round(usd * local_per_usd, 2),
                                "usd_per_unit": usd,
                                "change_pct": None,
                            }
                        )
                    if gold_usd.get("usd_per_oz"):
                        per_oz = float(gold_usd["usd_per_oz"])
                        per_gram = per_oz / TROY_OUNCE_GRAMS
                        gold.append(
                            {
                                "label_key": "prices.label.gold_gram",
                                "local": round(per_gram * local_per_usd, 2),
                                "usd": round(per_gram, 2),
                                "change_pct": None,
                            }
                        )
                        gold.append(
                            {
                                "label_key": "prices.label.gold_ounce",
                                "local": round(per_oz * local_per_usd, 2),
                                "usd": round(per_oz, 2),
                                "change_pct": None,
                            }
                        )
                    oil = _oil_rows(oil_usd, local_per_usd)
                    for key, label_key, cg_id in CRYPTO:
                        usd_price = gecko.get(cg_id)
                        if usd_price is None:
                            continue
                        crypto.append(
                            {
                                "label_key": label_key,
                                "local": round(float(usd_price) * local_per_usd, 2),
                                "usd": usd_price,
                                "change_pct": None,
                            }
                        )
    except Exception as exc:
        logger.warning("market bundle fetch failed: %s", type(exc).__name__)
    # Only overwrite the cache with sections that actually have data.
    # A transient outage used to wipe the good prices and stamp the
    # empty result fresh, so every price command stayed unavailable for
    # 5 minutes even after the sources recovered.
    if fiat:
        _market_cache["fiat"] = fiat
    if gold:
        _market_cache["gold"] = gold
    if crypto:
        _market_cache["crypto"] = crypto
    if oil:
        _market_cache["oil"] = oil
    if updated:
        _market_cache["updated"] = updated
    _market_cache["ts"] = time.monotonic()
    return _market_cache


async def fetch_fiat() -> list[dict]:
    """Fiat rows {label_key, code, local, usd_per_unit, change_pct} (never raises)."""
    try:
        bundle = await fetch_market_bundle()
        return list(bundle.get("fiat", []))
    except Exception as exc:
        logger.warning("fetch_fiat failed: %s", type(exc).__name__)
        return []


async def fetch_gold() -> list[dict]:
    """Gold rows {label_key, local, change_pct} (never raises)."""
    try:
        bundle = await fetch_market_bundle()
        return list(bundle.get("gold", []))
    except Exception as exc:
        logger.warning("fetch_gold failed: %s", type(exc).__name__)
        return []


async def fetch_crypto() -> list[dict]:
    """Crypto rows {label_key, local, usd, change_pct} (never raises)."""
    try:
        bundle = await fetch_market_bundle()
        return list(bundle.get("crypto", []))
    except Exception as exc:
        logger.warning("fetch_crypto failed: %s", type(exc).__name__)
        return []


async def fetch_oil() -> list[dict]:
    """Oil rows {label_key, local, usd, date} (never raises)."""
    try:
        bundle = await fetch_market_bundle()
        return list(bundle.get("oil", []))
    except Exception as exc:
        logger.warning("fetch_oil failed: %s", type(exc).__name__)
        return []


async def fetch_market_updated() -> str:
    """The TGJU update timestamp string ("" when unknown)."""
    try:
        bundle = await fetch_market_bundle()
        return bundle.get("updated", "") or ""
    except Exception:
        return ""


async def lookup_currency(name: str | None) -> dict | None:
    """Look up one fiat currency by Persian name or English code.
    Returns the fiat row dict, or None when unknown / fetch failed.
    Both the input and the alias keys are normalized (Persian
    normalization + strip + lowercase) so "USD", "Dollar" and " دلار "
    all match."""
    if not name:
        return None
    key = normalize_persian(name).strip().lower()
    code = None
    for alias, c in _CURRENCY_ALIASES.items():
        if normalize_persian(alias).strip().lower() == key:
            code = c
            break
    if not code:
        return None
    rows = await fetch_fiat()
    for row in rows:
        if row.get("code") == code:
            return row
    return None


# ----------------------------------------------------------------------
# Weather (Open-Meteo geocoding + forecast)
# ----------------------------------------------------------------------

async def fetch_weather(city: str) -> dict | None:
    """Fetch current weather for a city name (any language).
    Returns {city_name, country, temp_c, humidity, condition_key,
    wind_kmh} or None on failure. Cached 10 minutes per city."""
    if not city or not city.strip():
        return None
    key = city.strip().lower()
    now = time.monotonic()
    cached = _weather_cache.get(key)
    if cached and now - cached[0] < WEATHER_CACHE_TTL:
        return cached[1]
    result: dict | None = None
    try:
        geo_lang = "fa" if current_language() == "fa" else "en"
        async with httpx.AsyncClient(timeout=10.0, headers={"User-Agent": _UA}) as client:
            geo = await _get_json(
                client,
                GEOCODING_URL,
                params={"name": city.strip(), "count": 1, "language": geo_lang, "format": "json"},
            )
            results = geo.get("results", []) if isinstance(geo, dict) else []
            if not results:
                return None
            place = results[0]
            lat = place.get("latitude")
            lon = place.get("longitude")
            if lat is None or lon is None:
                return None
            fc = await _get_json(
                client,
                FORECAST_URL,
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
                    "timezone": "auto",
                },
            )
            current = fc.get("current", {}) if isinstance(fc, dict) else {}
            if "temperature_2m" not in current:
                return None
            try:
                code = int(current.get("weather_code"))
            except (TypeError, ValueError):
                code = -1
            result = {
                "city_name": place.get("name") or city.strip(),
                "country": place.get("country") or "",
                "temp_c": current.get("temperature_2m"),
                "humidity": current.get("relative_humidity_2m"),
                "condition_key": _WEATHER_CODES.get(code),
                "wind_kmh": current.get("wind_speed_10m"),
            }
    except Exception as exc:
        logger.warning("weather fetch failed for %r: %s", city, type(exc).__name__)
        return None
    if result is not None:
        # Prune expired entries and cap the cache so distinct user-typed
        # city strings cannot grow it without bound.
        expired = [
            k for k, (ts, _) in _weather_cache.items() if now - ts >= WEATHER_CACHE_TTL
        ]
        for k in expired:
            _weather_cache.pop(k, None)
        while len(_weather_cache) >= 500:
            _weather_cache.pop(next(iter(_weather_cache)))
        _weather_cache[key] = (time.monotonic(), result)
    return result


# ----------------------------------------------------------------------
# Formatting (plain Persian, no Markdown asterisks)
# ----------------------------------------------------------------------

def format_fiat_text(rows: list[dict], updated: str = "") -> str:
    """One line per currency: label, local currency, USD value, daily change."""
    if not rows:
        return ""
    label = currency_label()
    lines = [t("prices.fiat_title"), ""]
    for row in rows:
        local = row.get("local", row.get("toman"))
        line = f"{t(row['label_key'])}: {fa_num(local)} {label}"
        usd = row.get("usd_per_unit")
        if usd is not None:
            line += f" ({fa_num(float(usd))} USD)"
        line += _change_suffix(row.get("change_pct"))
        lines.append(line)
    if updated:
        lines.append("")
        lines.append(t("prices.updated", updated=updated))
    return "\n".join(lines).strip()


def format_gold_text(
    rows: list[dict], updated: str = "", oil: list[dict] | None = None
) -> str:
    """One line per gold/coin item: label, local currency, daily change.
    An oil section (Brent, local currency) is appended when given."""
    if not rows and not oil:
        return ""
    label = currency_label()
    lines = [t("prices.gold_title"), ""]
    for row in rows:
        local = row.get("local", row.get("toman"))
        line = f"{t(row['label_key'])}: {fa_num(local)} {label}"
        line += _change_suffix(row.get("change_pct"))
        lines.append(line)
    if oil:
        lines.append("")
        lines.append(t("prices.oil_title"))
        lines.append("")
        for row in oil:
            local = row.get("local")
            line = (
                f"{t(row['label_key'], date=row.get('date', ''))}: "
                f"{fa_num(local)} {label}"
            )
            line += _change_suffix(row.get("change_pct"))
            lines.append(line)
    if updated:
        lines.append("")
        lines.append(t("prices.updated", updated=updated))
    return "\n".join(lines).strip()


def format_crypto_text(rows: list[dict], updated: str = "") -> str:
    """One line per coin: label, local currency, USD, daily change."""
    if not rows:
        return ""
    label = currency_label()
    lines = [t("prices.crypto_title"), ""]
    for row in rows:
        local = row.get("local", row.get("toman"))
        line = f"{t(row['label_key'])}: {fa_num(local)} {label}"
        usd = row.get("usd")
        if usd is not None:
            line += f" ({fa_num(float(usd))} USD)"
        line += _change_suffix(row.get("change_pct"))
        lines.append(line)
    if updated:
        lines.append("")
        lines.append(t("prices.updated", updated=updated))
    return "\n".join(lines).strip()


def format_weather_text(w: dict | None) -> str:
    """Current weather for one city (localized)."""
    if not w:
        return ""
    place = w.get("city_name", "")
    country = w.get("country", "")
    sep = "، " if current_language() == "fa" else ", "
    country_suffix = f"{sep}{country}" if country else ""
    header = t("prices.weather_title", place=place, country=country_suffix)
    lines = [header, ""]
    temp = w.get("temp_c")
    if temp is not None:
        lines.append(t("prices.weather_temp", temp=_fmt_temp(temp)))
    condition = w.get("condition_key")
    if condition:
        lines.append(t("prices.weather_condition", condition=t(condition)))
    elif w.get("condition_fa"):
        lines.append(t("prices.weather_condition", condition=w["condition_fa"]))
    humidity = w.get("humidity")
    if humidity is not None:
        try:
            hum = fmt_num(f"{float(humidity):.0f}")
        except (TypeError, ValueError):
            hum = str(humidity)
        lines.append(t("prices.weather_humidity", humidity=hum))
    wind = w.get("wind_kmh")
    if wind is not None:
        try:
            wind_s = _fmt_temp(wind)
        except Exception:
            wind_s = str(wind)
        lines.append(t("prices.weather_wind", wind=wind_s))
    return "\n".join(lines).strip()


def format_single_currency(row: dict | None) -> str:
    """One currency: label, local currency, USD value, daily change."""
    if not row:
        return ""
    local = row.get("local", row.get("toman"))
    lines = [t("prices.single_title", label=t(row["label_key"])), ""]
    lines.append(
        t("prices.single_amount", amount=fa_num(local), currency=currency_label())
    )
    usd = row.get("usd_per_unit")
    if usd is not None:
        lines.append(t("prices.single_usd", usd=fa_num(float(usd))))
    suffix = _change_suffix(row.get("change_pct"))
    if suffix:
        lines.append(t("prices.single_change", suffix=suffix))
    return "\n".join(lines).strip()
