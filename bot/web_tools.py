"""
Web search and webpage content extraction tools for Vortex Telegram Bot.
All external web content is strictly wrapped as untrusted data (`<untrusted_web_content>`)
to prevent indirect prompt injection attacks.
Also enforces SSRF protection (blocking private/loopback IP ranges).
"""

from __future__ import annotations

import html
import ipaddress
import logging
import re
import socket
from typing import Any
from urllib.parse import quote, quote_plus, urlparse

import httpx
from bs4 import BeautifulSoup

from bot.security import wrap_untrusted_data

logger = logging.getLogger(__name__)


def _is_safe_public_url(url: str) -> bool:
    """
    Validates that the URL uses http/https and does not resolve to localhost,
    loopback, link-local, private, reserved or unspecified addresses (SSRF
    protection). IPv4-mapped IPv6 addresses (e.g. ::ffff:127.0.0.1) are
    unwrapped before the check, so they cannot smuggle a loopback address.
    NOTE: this does a synchronous DNS lookup; call the async wrapper
    `_is_safe_public_url_async` from async code so the event loop is not
    blocked.
    """
    try:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            return False
        hostname = parsed.hostname
        if not hostname:
            return False
        if hostname.lower() in {"localhost", "127.0.0.1", "::1", "0.0.0.0"}:
            return False

        addr_info = socket.getaddrinfo(hostname, None)
        for item in addr_info:
            ip_str = item[4][0]
            ip_obj = ipaddress.ip_address(ip_str)
            # Unwrap IPv4-mapped IPv6 (e.g. ::ffff:127.0.0.1 -> 127.0.0.1).
            if isinstance(ip_obj, ipaddress.IPv6Address) and ip_obj.ipv4_mapped is not None:
                ip_obj = ip_obj.ipv4_mapped
            if (
                ip_obj.is_private
                or ip_obj.is_loopback
                or ip_obj.is_link_local
                or ip_obj.is_multicast
                or ip_obj.is_reserved
                or ip_obj.is_unspecified
            ):
                return False
        return True
    except Exception:
        return False


async def _is_safe_public_url_async(url: str) -> bool:
    """Async wrapper: runs the (blocking) DNS lookup in a thread so a
    slow or dead domain never stalls the event loop."""
    import asyncio

    return await asyncio.to_thread(_is_safe_public_url, url)


def _strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s or "")
    return html.unescape(re.sub(r"\s+", " ", s)).strip()


def _parse_searxng_json(data: dict, max_results: int) -> list[dict[str, str]]:
    """Parse SearXNG /search?format=json results into title/url/snippet dicts."""
    results: list[dict[str, str]] = []
    for item in (data.get("results") or [])[:max_results]:
        title = str(item.get("title", "")).strip()
        url = str(item.get("url", "")).strip()
        snippet = _strip_tags(str(item.get("content", "")))
        if title and url.startswith("http"):
            results.append({"title": title, "url": url, "snippet": snippet})
        if len(results) >= max_results:
            break
    return results


class WebToolkit:
    def __init__(
        self,
        search_provider: str = "tavily",
        search_api_key: str = "",
        max_results: int = 5,
        max_chars: int = 12000,
    ) -> None:
        self.search_provider = search_provider.lower()
        self.search_api_key = search_api_key
        self.max_results = max_results
        self.max_chars = max_chars

    async def web_search(self, query: str) -> str:
        """
        Searches the web for `query` using the configured search provider
        (Tavily API, Serper API, or self-hosted SearXNG) and returns
        formatted results with URLs wrapped as untrusted data.
        """
        query = (query or "").strip()
        if not query:
            return "عبارت جستجو خالی است."

        results: list[dict[str, str]] = []
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
            )
        }

        async with httpx.AsyncClient(timeout=12.0, headers=headers) as client:
            # 1. Tavily Search API
            if self.search_provider == "tavily" and self.search_api_key:
                try:
                    resp = await client.post(
                        "https://api.tavily.com/search",
                        json={
                            "api_key": self.search_api_key,
                            "query": query,
                            "max_results": self.max_results,
                            "include_answer": False,
                        },
                    )
                    resp.raise_for_status()
                    data = resp.json()
                    for item in data.get("results", [])[: self.max_results]:
                        results.append(
                            {
                                "title": str(item.get("title", "")),
                                "url": str(item.get("url", "")),
                                "snippet": str(item.get("content", "")),
                            }
                        )
                except Exception as exc:
                    logger.warning("Tavily search error: %s", type(exc).__name__)

            # 2. Serper.dev Google Search API
            elif self.search_provider == "serper" and self.search_api_key:
                try:
                    resp = await client.post(
                        "https://google.serper.dev/search",
                        headers={"X-API-KEY": self.search_api_key, "Content-Type": "application/json"},
                        json={"q": query, "num": self.max_results},
                    )
                    resp.raise_for_status()
                    data = resp.json()
                    for item in data.get("organic", [])[: self.max_results]:
                        results.append(
                            {
                                "title": str(item.get("title", "")),
                                "url": str(item.get("link", "")),
                                "snippet": str(item.get("snippet", "")),
                            }
                        )
                except Exception as exc:
                    logger.warning("Serper search error: %s", type(exc).__name__)

            # 3. Self-hosted SearXNG (local Docker, no key). Primary web search.
            #    Wikipedia stays as the last resort.
            if not results:
                try:
                    resp = await client.get(
                        "http://127.0.0.1:8080/search",
                        params={"q": query, "format": "json"},
                    )
                    resp.raise_for_status()
                    results = _parse_searxng_json(resp.json(), self.max_results)
                except Exception as exc:
                    logger.warning("SearXNG search error: %s", type(exc).__name__)
            if not results:
                try:
                    resp = await client.get(
                        "https://en.wikipedia.org/w/api.php",
                        params={
                            "action": "query",
                            "list": "search",
                            "srsearch": query,
                            "format": "json",
                            "srlimit": str(self.max_results),
                        },
                    )
                    resp.raise_for_status()
                    data = resp.json()
                    for item in data.get("query", {}).get("search", [])[: self.max_results]:
                        title = str(item.get("title", ""))
                        results.append(
                            {
                                "title": title,
                                "url": "https://en.wikipedia.org/wiki/"
                                + quote(title.replace(" ", "_")),
                                "snippet": _strip_tags(str(item.get("snippet", ""))),
                            }
                        )
                except Exception as exc:
                    logger.warning("Wikipedia fallback search error: %s", type(exc).__name__)

        if not results:
            return "نتیجه‌ای در جستجوی وب پیدا نشد."

        formatted_lines = [f"نتایج جستجوی وب برای «{query}» (حتماً منبع/لینک را در پاسخ ذکر کن):"]
        for i, res in enumerate(results, start=1):
            formatted_lines.append(
                f"{i}. عنوان: {res['title']}\n   منبع (URL): {res['url']}\n   خلاصه: {res['snippet']}"
            )
        raw_output = "\n\n".join(formatted_lines)[: self.max_chars]
        return wrap_untrusted_data("untrusted_web_content", raw_output)

    async def fetch_webpage(self, url: str) -> str:
        """
        Fetches a public webpage, strips scripts/styles, extracts readable text,
        and wraps the result in `<untrusted_web_content>` tags.
        SSRF-safe: redirects are followed MANUALLY (max 5 hops) and EVERY
        hop is re-validated with _is_safe_public_url, so a public URL that
        302-redirects to 127.0.0.1 / 169.254.169.254 is rejected. The body
        is streamed and capped at ~1MB so a huge page cannot exhaust memory.
        """
        import asyncio
        from urllib.parse import urljoin

        url = (url or "").strip()
        if not await _is_safe_public_url_async(url):
            return "آدرس وب نامعتبر است یا دسترسی به آن مجاز نیست."

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
            )
        }
        try:
            async with httpx.AsyncClient(
                timeout=12.0, headers=headers, follow_redirects=False
            ) as client:
                current_url = url
                resp = None
                for _hop in range(6):
                    resp = await client.get(current_url)
                    if resp.status_code in (301, 302, 303, 307, 308):
                        location = resp.headers.get("location", "").strip()
                        if not location:
                            break
                        next_url = urljoin(current_url, location)
                        if not await _is_safe_public_url_async(next_url):
                            return "آدرس وب نامعتبر است یا دسترسی به آن مجاز نیست."
                        current_url = next_url
                        continue
                    break
                if resp is None:
                    return "خطا در دریافت یا خواندن محتوای صفحه وب."
                resp.raise_for_status()
                content_type = resp.headers.get("content-type", "").lower()
                if "text/html" not in content_type and "text/plain" not in content_type:
                    return f"فرمت صفحه وب پشتیبانی نمی‌شود ({content_type})."

                # Stream the body, capped at ~1MB (the old code buffered
                # the whole response before truncating).
                chunks: list[bytes] = []
                total = 0
                async for chunk in resp.aiter_bytes(65536):
                    total += len(chunk)
                    if total > 1_000_000:
                        break
                    chunks.append(chunk)
                html_text = b"".join(chunks).decode("utf-8", errors="replace")
                soup = BeautifulSoup(html_text[:300_000], "lxml")
                for tag in soup(["script", "style", "noscript", "iframe", "svg", "header", "footer", "nav"]):
                    tag.decompose()

                title = soup.title.get_text(strip=True) if soup.title else current_url
                text = soup.get_text("\n", strip=True)
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                cleaned_text = "\n".join(lines)[: self.max_chars]

                payload = f"عنوان صفحه: {title}\nآدرس منبع (URL): {current_url}\n\nمتن استخراج‌شده:\n{cleaned_text}"
                return wrap_untrusted_data("untrusted_web_content", payload)
        except Exception as exc:
            logger.warning("fetch_webpage failed for %s: %s", url, type(exc).__name__)
            return "خطا در دریافت یا خواندن محتوای صفحه وب."


def get_web_tool_schemas() -> list[dict[str, Any]]:
    """Returns OpenAI-compatible tool definitions for web search and browsing."""
    return [
        {
            "type": "function",
            "function": {
                "name": "web_search",
                "description": "جستجو در اینترنت برای یافتن اطلاعات به‌روز، اخبار، مستندات یا پاسخ سوالات. هنگام استفاده حتماً منبع را ذکر کن.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "عبارت جستجو به فارسی یا انگلیسی",
                        }
                    },
                    "required": ["query"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "fetch_webpage",
                "description": "باز کردن و استخراج متن یک صفحه وب با آدرس URL مشخص. هنگام استفاده حتماً منبع را ذکر کن.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "آدرس کامل صفحه وب (http یا https)",
                        }
                    },
                    "required": ["url"],
                },
            },
        },
    ]
