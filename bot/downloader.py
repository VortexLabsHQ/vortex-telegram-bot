"""Download a file from a user-supplied link and hand it back to the chat.

Method — the one the user described (as the Skip bot does it for music):
the page is fetched with a browser User-Agent; the direct media URL is
pulled out of the page source — og:audio / og:video meta tags,
<audio> / <video> / <source> tags, JSON-LD contentUrl, or a direct media
URL embedded in the page's JSON — and then downloaded with a Referer
header pointing at the page, which is what unlocks servers that refuse
hotlinked / direct downloads.

Limits: Telegram bots can SEND at most 50MB per file, so downloads are
capped at 45MB (checked from Content-Length first, enforced while
streaming). All HTTP here is synchronous httpx; callers run it via
asyncio.to_thread so the bot's event loop never blocks.
"""

from __future__ import annotations

import json
import logging
import re
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

import httpx
from bs4 import BeautifulSoup

from bot.locale import fmt_num, t
from bot.web_tools import _is_safe_public_url

logger = logging.getLogger(__name__)

# Telegram's bot send limit is 50MB per file; keep a safety margin.
MAX_DOWNLOAD_BYTES = 45 * 1024 * 1024
PAGE_TIMEOUT = httpx.Timeout(20.0, connect=10.0)
DOWNLOAD_TIMEOUT = httpx.Timeout(300.0, connect=20.0)

BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

AUDIO_EXTS = {
    "mp3", "m4a", "oga", "ogg", "wav", "flac", "aac", "opus", "mid", "midi",
}
VIDEO_EXTS = {"mp4", "m4v", "webm", "mkv", "mov", "avi", "wmv", "flv"}
OTHER_EXTS = {"pdf", "epub", "zip", "rar", "7z", "jpg", "jpeg", "png", "gif", "webp"}
MEDIA_EXTS = AUDIO_EXTS | VIDEO_EXTS | OTHER_EXTS

_MEDIA_EXT_ALTS = "|".join(sorted(MEDIA_EXTS))
# A quoted media URL inside page source / embedded JSON, e.g.
# "url":"https://cdn.example.com/song.mp3?token=..." — the page text is
# unescaped (\/ -> /) before this runs, so escaped JSON URLs match too.
_MEDIA_URL_RE = re.compile(
    r"""["']((?:https?:)?//[^"'<>\s\\]+\.(?:%s)(?:[?#][^"'<>\s\\]*)?)["']"""
    % _MEDIA_EXT_ALTS,
    re.IGNORECASE,
)

_CONTENT_TYPE_EXT = {
    "audio/mpeg": ".mp3",
    "audio/mp4": ".m4a",
    "audio/ogg": ".ogg",
    "audio/wav": ".wav",
    "audio/x-wav": ".wav",
    "audio/flac": ".flac",
    "audio/aac": ".aac",
    "video/mp4": ".mp4",
    "video/webm": ".webm",
    "video/x-matroska": ".mkv",
    "application/pdf": ".pdf",
    "application/zip": ".zip",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
}

def download_error_text(reason: str) -> str:
    """User-facing text for a download failure `reason` (localized at
    call time, so an /admin language change applies immediately).
    Unknown reasons fall back to the generic failure text."""
    key = {
        "bad_url": "download.bad_url",
        "fetch_failed": "download.fetch_failed",
        "no_media": "download.no_media",
        "too_large": "download.too_large",
        "empty": "download.empty",
    }.get(reason)
    if key is None:
        return t("download.failed")
    return t(key)


class DownloadError(Exception):
    """A download failure with a short reason code and optional detail
    (e.g. the real size for 'too_large')."""

    def __init__(self, reason: str, detail: str = "") -> None:
        super().__init__(reason)
        self.reason = reason
        self.detail = detail


@dataclass
class DownloadedFile:
    path: Path
    filename: str
    size_bytes: int = 0
    content_type: str = ""
    # Only set by download_to_temp_dir: the temp dir the file lives in
    # (the caller deletes it after sending the file).
    dir_path: Path | None = None


def fa_size_str(n_bytes: int) -> str:
    """'78.5 MB' / '512 KB' — localized digits, for user messages.
    (Kept the old name for compatibility; digits follow the bot's
    current language.)"""
    if n_bytes >= 1024 * 1024:
        return t("download.size_mb", size=fmt_num(f"{n_bytes / (1024 * 1024):.1f}"))
    if n_bytes >= 1024:
        return t("download.size_kb", size=fmt_num(f"{n_bytes / 1024:.0f}"))
    return t("download.size_b", size=fmt_num(str(n_bytes)))


def _ext_of(url: str) -> str:
    try:
        path = urlparse(url).path
    except Exception:
        return ""
    suffix = path.rsplit(".", 1)[-1].lower() if "." in path.rsplit("/", 1)[-1] else ""
    return suffix


def _looks_like_media_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    value = value.strip()
    if not (value.startswith("http://") or value.startswith("https://") or value.startswith("//")):
        return False
    return _ext_of(value) in MEDIA_EXTS


def _sanitize_filename(filename: str) -> str:
    base = Path(filename or "download").name
    safe = re.sub(r"[^\w.\-\u0600-\u06FF]", "_", base)
    safe = safe.lstrip(".")[:120]
    return safe or "download"


def _unescape_embedded(text: str) -> str:
    """Undo the escaping found in embedded JSON (escaped slashes become
    /, \\u0026 becomes &, &amp; becomes &). Only used for the raw-source
    scan, never for parsing."""
    return text.replace("\\/", "/").replace("\\u0026", "&").replace("&amp;", "&")


def _walk_json_strings(data: object):
    """Yield every string value inside a parsed JSON structure."""
    if isinstance(data, str):
        yield data
    elif isinstance(data, dict):
        for value in data.values():
            yield from _walk_json_strings(value)
    elif isinstance(data, list):
        for item in data:
            yield from _walk_json_strings(item)


def _rank_candidates(urls: list[str]) -> list[str]:
    """Dedupe (keeping first-seen order), audio first, then video, then
    other media — a music page usually embeds the track plus a cover
    image, and the audio is what the user wants."""
    seen: dict[str, None] = {}
    for url in urls:
        seen.setdefault(url, None)
    unique = list(seen)

    def group(url: str) -> int:
        ext = _ext_of(url)
        if ext in AUDIO_EXTS:
            return 0
        if ext in VIDEO_EXTS:
            return 1
        return 2

    return sorted(unique, key=group)


def extract_media_url(html: str, page_url: str) -> str | None:
    """Find the direct media URL inside a page's HTML.

    Order: explicit media tags first (og:audio/og:video meta, <audio> /
    <video> / <source> — any http(s) URL there IS the media), then
    JSON-LD contentUrl, then a scan of the raw page source for quoted
    media URLs (the embedded-JSON case). Returns None when nothing is
    found.
    """
    soup = BeautifulSoup(html, "lxml")

    explicit: list[str] = []
    for prop in (
        "og:audio:secure_url",
        "og:audio",
        "og:video:secure_url",
        "og:video",
        "twitter:player:stream",
    ):
        tag = soup.find("meta", attrs={"property": prop}) or soup.find(
            "meta", attrs={"name": prop}
        )
        content = (tag.get("content") or "").strip() if tag else ""
        if content:
            explicit.append(content)
    for tag in soup.find_all(["audio", "video", "source"]):
        src = (tag.get("src") or "").strip()
        if src:
            explicit.append(src)

    scanned: list[str] = []
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            data = json.loads(script.string or "")
        except Exception:
            continue
        for value in _walk_json_strings(data):
            if isinstance(value, str) and _looks_like_media_url(value):
                scanned.append(value.strip())

    clean = _unescape_embedded(html)
    for m in _MEDIA_URL_RE.finditer(clean):
        scanned.append(m.group(1))

    def resolve(url: str) -> str:
        if url.startswith("//"):
            return "https:" + url
        if url.startswith(("http://", "https://")):
            return url
        # Relative URLs (e.g. /media/a.mp3) resolve against the FINAL
        # page URL (after redirects), not the original link.
        return urljoin(page_url, url)

    # Explicit candidates first, but only the ones that actually look
    # like media: og:video is very often an HTML embed player
    # (youtube.com/embed/...) and must not win over a real .mp3/.mp4.
    resolved_explicit = [resolve(u) for u in explicit]
    media_explicit = [u for u in resolved_explicit if _looks_like_media_url(u)]
    if media_explicit:
        return _rank_candidates(media_explicit)[0]
    resolved_scanned = [
        resolve(u) for u in scanned if _looks_like_media_url(resolve(u))
    ]
    ranked = _rank_candidates(resolved_scanned)
    return ranked[0] if ranked else None


def _is_media_content_type(content_type: str) -> bool:
    ctype = (content_type or "").lower().split(";")[0].strip()
    return (
        ctype.startswith(("audio/", "video/", "image/"))
        or ctype
        in {
            "application/pdf",
            "application/zip",
            "application/octet-stream",
            "application/x-rar-compressed",
            "application/x-7z-compressed",
            "application/epub+zip",
        }
    )


def resolve_media_url(page_url: str) -> tuple[str, str]:
    """Resolve a user-supplied link to (direct_media_url, referer).

    A direct media link is returned as-is; otherwise the page is
    fetched and the media URL is extracted from its source. The page
    URL, every redirect hop, and the extracted direct URL are all
    SSRF-validated. The page body is STREAMED and capped at ~2MB, so a
    direct-media link with no file extension serving a huge file is
    never buffered into RAM. Raises DownloadError ('bad_url' /
    'fetch_failed' / 'no_media').
    """
    parsed = urlparse(page_url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise DownloadError("bad_url")
    if not _is_safe_public_url(page_url):
        raise DownloadError("bad_url")
    if _looks_like_media_url(page_url):
        return page_url, page_url
    try:
        with httpx.Client(
            headers={"User-Agent": BROWSER_UA},
            follow_redirects=False,
            timeout=PAGE_TIMEOUT,
        ) as client:
            current = page_url
            for _hop in range(6):
                if not _is_safe_public_url(current):
                    raise DownloadError("bad_url")
                with client.stream("GET", current) as resp:
                    if resp.status_code in (301, 302, 303, 307, 308):
                        location = (resp.headers.get("location") or "").strip()
                        if not location:
                            raise DownloadError("fetch_failed")
                        current = urljoin(current, location)
                        continue
                    resp.raise_for_status()
                    final_url = str(resp.url)
                    ctype = resp.headers.get("content-type") or ""
                    if _is_media_content_type(ctype) or _looks_like_media_url(final_url):
                        return final_url, page_url
                    # Stream the HTML, capped at ~2MB.
                    chunks: list[bytes] = []
                    total = 0
                    for chunk in resp.iter_bytes(65536):
                        total += len(chunk)
                        if total > 2_000_000:
                            break
                        chunks.append(chunk)
                    html = b"".join(chunks).decode("utf-8", errors="replace")
                    direct = extract_media_url(html, final_url)
                    if not direct:
                        raise DownloadError("no_media")
                    if not _is_safe_public_url(direct):
                        raise DownloadError("bad_url")
                    return direct, page_url
            raise DownloadError("fetch_failed")
    except DownloadError:
        raise
    except httpx.HTTPError:
        raise DownloadError("fetch_failed")
    except Exception:
        raise DownloadError("fetch_failed")


def _filename_from_response(resp: httpx.Response, direct_url: str) -> str:
    cd = resp.headers.get("content-disposition") or ""
    name = ""
    m = re.search(r"filename\*\s*=\s*UTF-8''([^;]+)", cd, re.IGNORECASE)
    if m:
        try:
            name = unquote(m.group(1))
        except Exception:
            name = ""
    if not name:
        m = re.search(r'filename\s*=\s*"([^"]+)"', cd)
        if m:
            name = m.group(1)
    if not name:
        name = unquote(urlparse(direct_url).path.rsplit("/", 1)[-1])
    if not name or "." not in name.rsplit("/", 1)[-1]:
        ctype = (resp.headers.get("content-type") or "").lower().split(";")[0].strip()
        name = (name or "download") + _CONTENT_TYPE_EXT.get(ctype, "")
    return _sanitize_filename(name)


def download_media(page_url: str, dest_dir: Path) -> DownloadedFile:
    """Resolve + download a file into `dest_dir` (created if needed).
    Enforces the 45MB cap from Content-Length and while streaming.
    The direct URL and every redirect hop are SSRF-validated, and the
    response content-type must be media (an HTML embed player is
    rejected, not saved as a file). Raises DownloadError on any failure;
    a partial file is deleted."""
    direct_url, referer = resolve_media_url(page_url)
    if not _is_safe_public_url(direct_url):
        raise DownloadError("bad_url")
    headers = {"User-Agent": BROWSER_UA, "Referer": referer}
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    path: Path | None = None
    try:
        with httpx.Client(
            headers=headers, follow_redirects=False, timeout=DOWNLOAD_TIMEOUT
        ) as client:
            # Follow redirects manually with streaming, re-validating each
            # hop, so the body is never buffered before the content-type
            # and size checks run.
            current = direct_url
            for _hop in range(6):
                if not _is_safe_public_url(current):
                    raise DownloadError("bad_url")
                with client.stream("GET", current) as stream_resp:
                    if stream_resp.status_code in (301, 302, 303, 307, 308):
                        location = (stream_resp.headers.get("location") or "").strip()
                        if not location:
                            raise DownloadError("fetch_failed")
                        current = urljoin(current, location)
                        continue
                    stream_resp.raise_for_status()
                    ctype = stream_resp.headers.get("content-type") or ""
                    if not _is_media_content_type(ctype) and not _looks_like_media_url(current):
                        raise DownloadError("no_media")
                    total = stream_resp.headers.get("content-length")
                    if total is not None:
                        try:
                            if int(total) > MAX_DOWNLOAD_BYTES:
                                raise DownloadError("too_large", detail=fa_size_str(int(total)))
                        except ValueError:
                            pass
                    filename = _filename_from_response(stream_resp, current)
                    path = dest_dir / filename
                    size = 0
                    with path.open("wb") as f:
                        for chunk in stream_resp.iter_bytes(chunk_size=262144):
                            size += len(chunk)
                            if size > MAX_DOWNLOAD_BYTES:
                                raise DownloadError("too_large", detail=fa_size_str(size))
                            f.write(chunk)
                    if size == 0:
                        raise DownloadError("empty")
                    return DownloadedFile(
                        path=path,
                        filename=filename,
                        size_bytes=size,
                        content_type=stream_resp.headers.get("content-type") or "",
                    )
            raise DownloadError("fetch_failed")
    except DownloadError:
        if path is not None:
            try:
                path.unlink(missing_ok=True)
            except Exception:
                pass
        raise
    except httpx.HTTPError:
        if path is not None:
            try:
                path.unlink(missing_ok=True)
            except Exception:
                pass
        raise DownloadError("fetch_failed")
    except Exception:
        if path is not None:
            try:
                path.unlink(missing_ok=True)
            except Exception:
                pass
        raise DownloadError("fetch_failed")


def download_to_temp_dir(page_url: str, parent: Path | None = None) -> DownloadedFile:
    """Download into a fresh temp dir (for the LLM download_file tool —
    the handler sends the file and deletes the whole dir afterwards).
    When `parent` is given (the bot's workspace root), the temp dir is
    created inside it so the startup purge / TTL reaper can clean it up
    if the process crashes between download and send; otherwise the
    system temp dir is used."""
    tmp = Path(tempfile.mkdtemp(prefix="vortex_dl_tool_", dir=parent))
    try:
        downloaded = download_media(page_url, tmp)
    except Exception:
        shutil.rmtree(tmp, ignore_errors=True)
        raise
    downloaded.dir_path = tmp
    return downloaded
