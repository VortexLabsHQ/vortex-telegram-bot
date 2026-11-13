"""
Real-time USD exchange rate fetcher for Vortex Telegram Bot.
Bypasses the LLM completely when triggered by 'Vortex dollar' (or the
wake-word form in the bot's language).

Iran: the configured sources return the USD/IRR free-market rate
(Navasan / Alanchand / TGJU), formatted in Toman.
Other countries: the USD rate in the LOCAL currency comes from
Frankfurter (free, no key) — "1 USD = X <local currency>".
30-to-60 second in-memory cache (configurable via DOLLAR_CACHE_TTL_SECONDS).
"""

from __future__ import annotations

import logging
import random
import re
import time
from dataclasses import dataclass
from datetime import datetime

import httpx
from bs4 import BeautifulSoup

from bot.countries import country_now, currency_code, current_country
from bot.locale import fmt_num, t, t_list

logger = logging.getLogger(__name__)

_PERSIAN_DIGITS_MAP = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


@dataclass
class DollarQuote:
    price_toman: str
    source_name: str
    updated_at: str
    fetched_monotonic: float


class DollarService:
    def __init__(
        self,
        primary_url: str,
        fallback_url: str,
        second_fallback_url: str,
        cache_ttl_seconds: int = 45,
    ) -> None:
        self.primary_url = primary_url
        self.fallback_url = fallback_url
        self.second_fallback_url = second_fallback_url
        # Enforce 30 to 60 seconds TTL range per specification
        self.cache_ttl_seconds = max(30, min(60, cache_ttl_seconds))
        self._cached_quote: DollarQuote | None = None

    @staticmethod
    def _now_local_str() -> str:
        """Current local time in the bot's country ("YYYY-MM-DD HH:MM:SS")."""
        try:
            now = country_now()
        except Exception:
            now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def _fmt_rate(rate: float) -> str:
        """An FX rate with sensible precision: 4 decimals below 1,
        2 decimals up to 100, none above (e.g. 0.8543, 1.09, 157)."""
        if rate >= 100:
            text = f"{rate:,.0f}"
        elif rate >= 1:
            text = f"{rate:,.2f}"
        else:
            text = f"{rate:,.4f}"
        return fmt_num(text)

    @staticmethod
    def _normalize_digits(text: str) -> str:
        return text.translate(_PERSIAN_DIGITS_MAP)

    @staticmethod
    def _format_number(val: int | float | str) -> str:
        # Parse as a float (keep the decimal point): stripping every
        # non-digit turned "68500.5" into 685005 and a JSON float like
        # 1023450.0 into 10234500 (10x too big).
        raw = DollarService._normalize_digits(str(val)).replace(",", "").strip()
        try:
            num = int(float(raw))
        except (TypeError, ValueError):
            raise ValueError("Invalid numeric price")
        if num <= 0:
            raise ValueError("Invalid numeric price")
        # If reported in Rials (e.g. > 300,000), convert or note appropriately.
        # NOTE: this is a heuristic — once the Toman rate passes 300k it
        # misfires, so prefer sources that report Toman directly.
        if num > 300_000:
            toman = num // 10
            return f"{toman:,} تومان ({num:,} ریال)"
        return f"{num:,} تومان"

    async def _fetch_from_url(self, client: httpx.AsyncClient, url: str) -> DollarQuote:
        if not url:
            raise ValueError("Empty URL")

        resp = await client.get(url, follow_redirects=True)
        resp.raise_for_status()
        content_type = resp.headers.get("content-type", "").lower()

        # 1. Try JSON API parsing (Navasan, BrsApi, Bonbast JSON, custom JSON endpoint)
        if "application/json" in content_type or resp.text.strip().startswith(("{", "[")):
            data = resp.json()
            price_val = None
            updated_str = self._now_local_str()

            if isinstance(data, dict):
                # Common Iranian API structures (e.g., navasan: {"usd_sell": {"value": "68500", "date": "..."}})
                for key in ("usd_sell", "usd", "dollar", "dolar", "price_dollar_rl", "USD"):
                    if key in data:
                        item = data[key]
                        if isinstance(item, dict):
                            price_val = item.get("value") or item.get("price") or item.get("p")
                            updated_str = str(item.get("date") or item.get("time") or updated_str)
                        else:
                            price_val = item
                        break
                if price_val is None and "price" in data:
                    price_val = data["price"]
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and str(item.get("symbol", item.get("slug", ""))).upper() in {"USD", "DOLLAR"}:
                        price_val = item.get("price") or item.get("value")
                        updated_str = str(item.get("time") or item.get("updated_at") or updated_str)
                        break

            if price_val is not None:
                formatted = self._format_number(price_val)
                return DollarQuote(
                    price_toman=formatted,
                    source_name=t("dollar.source_api"),
                    updated_at=updated_str,
                    fetched_monotonic=time.monotonic(),
                )

        # 2. Try HTML Scraping (Alanchand, TGJU, or custom HTML page)
        html = resp.text
        soup = BeautifulSoup(html, "lxml")

        # Check TGJU specific attributes
        tgju_el = soup.select_one('[data-market-row="price_dollar_rl"] .price, span[data-col="info.last_trade.PDrCotVal"]')
        if tgju_el and tgju_el.get_text(strip=True):
            formatted = self._format_number(tgju_el.get_text(strip=True))
            return DollarQuote(
                price_toman=formatted,
                source_name=t("dollar.source_tgju"),
                updated_at=self._now_local_str(),
                fetched_monotonic=time.monotonic(),
            )

        # Generic regex fallback on visible text near 'دلار'.
        # The number must have 1-3 leading digits (a 7-digit Toman price
        # like 1,023,450 starts with a single digit). A sanity range
        # (30k–500k Toman) rejects stray numbers from elsewhere on the
        # page. The old patterns could match only the tail ("023,450")
        # and report "23,450 تومان" as the dollar rate.
        text_norm = self._normalize_digits(soup.get_text(" ", strip=True))
        match = re.search(r"دلار[^\d]{1,40}(\d{1,3}(?:,\d{3})+)", text_norm)
        price_text = match.group(1) if match else None
        if price_text:
            try:
                value = int(price_text.replace(",", ""))
            except ValueError:
                value = 0
            # "دلار" prices on these pages are in Toman (or Rials/10).
            # Reject anything outside a plausible dollar range.
            if not (30_000 <= value <= 5_000_000):
                price_text = None
        if price_text:
            formatted = self._format_number(price_text)
            return DollarQuote(
                price_toman=formatted,
                source_name=t("dollar.source_board"),
                updated_at=self._now_local_str(),
                fetched_monotonic=time.monotonic(),
            )

        raise ValueError(f"Could not parse USD price from {url}")

    async def get_dollar_message(self, is_boss: bool = False) -> str:
        """Returns a formatted response with the USD rate.

        Iran: the cached/fresh USD/IRR rate from the configured
        sources (Toman). Other countries: the USD rate in the local
        currency from Frankfurter ("1 USD = X <currency>")."""
        if current_country().name != "Iran":
            return await self._get_fx_message(is_boss=is_boss)
        now = time.monotonic()
        # Only an Iran-path quote may be reused here (an FX quote cached
        # before a country switch holds a rate, not a Toman price).
        cached_ir = (
            self._cached_quote
            if self._cached_quote is not None
            and self._cached_quote.source_name != t("dollar.source_fx")
            else None
        )
        if (
            cached_ir is not None
            and (now - cached_ir.fetched_monotonic) < self.cache_ttl_seconds
        ):
            quote = cached_ir
        else:
            quote = None
            urls_to_try = [
                u for u in (self.primary_url, self.fallback_url, self.second_fallback_url)
                if u and not u.endswith("api_key=")
            ]
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
                ),
                "Accept-Language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7",
            }
            async with httpx.AsyncClient(timeout=8.0, headers=headers) as client:
                for url in urls_to_try:
                    try:
                        quote = await self._fetch_from_url(client, url)
                        self._cached_quote = quote
                        break
                    except Exception as exc:
                        logger.warning("Dollar source failed (%s): %s", url, type(exc).__name__)

            if quote is None:
                # If all live sources failed, use stale cache if available, else return friendly message
                if cached_ir is not None:
                    quote = cached_ir
                else:
                    if is_boss:
                        return t("dollar.unavailable_boss")
                    return t("dollar.unavailable")

        if is_boss:
            return t(
                "dollar.boss",
                price=quote.price_toman,
                updated_at=quote.updated_at,
                source=quote.source_name,
            )

        templates = t_list("dollar.templates")
        template = random.choice(templates) if templates else (
            "💵 {price}\n🕒 `{updated_at}` ({source})"
        )
        return template.format(
            price=quote.price_toman,
            updated_at=quote.updated_at,
            source=quote.source_name,
        )

    async def _get_fx_message(self, is_boss: bool = False) -> str:
        """USD rate in the local currency (non-Iran countries), via
        Frankfurter. Falls back to the stale cached rate, else a
        localized error — never raises."""
        from bot.prices import usd_to_local_rate

        now = time.monotonic()
        # Only an FX quote may be reused here: an Iran-path quote cached
        # before a country switch holds a Toman price, not an FX rate.
        cached_fx = (
            self._cached_quote
            if self._cached_quote is not None
            and self._cached_quote.source_name == t("dollar.source_fx")
            else None
        )
        if (
            cached_fx is not None
            and (now - cached_fx.fetched_monotonic) < self.cache_ttl_seconds
        ):
            return self._format_fx_quote(cached_fx, is_boss=is_boss)
        rate = None
        try:
            rate = await usd_to_local_rate()
        except Exception as exc:
            logger.warning("FX dollar fetch failed: %s", type(exc).__name__)
        if rate is None:
            if cached_fx is not None:
                return self._format_fx_quote(cached_fx, is_boss=is_boss)
            if is_boss:
                return t("dollar.unavailable_boss")
            return t("dollar.unavailable")
        quote = DollarQuote(
            price_toman=self._fmt_rate(rate),
            source_name=t("dollar.source_fx"),
            updated_at=self._now_local_str(),
            fetched_monotonic=time.monotonic(),
        )
        self._cached_quote = quote
        return self._format_fx_quote(quote, is_boss=is_boss)

    def _format_fx_quote(self, quote: DollarQuote, is_boss: bool = False) -> str:
        """Render a cached/fresh FX quote ("1 USD = X <currency>")."""
        key = "dollar.fx_boss" if is_boss else "dollar.fx"
        return t(
            key,
            amount=quote.price_toman,
            currency=currency_code(),
            updated_at=quote.updated_at,
            source=quote.source_name,
        )
