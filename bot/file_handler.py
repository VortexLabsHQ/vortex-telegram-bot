"""
Isolated temporary workspace manager, safe file reader/extractor, and file generator
for Vortex Telegram Bot.

Security & Lifecycle Guarantees:
1. Per-request isolated temporary directory (`tempfile.TemporaryDirectory`) inside `TEMP_WORKSPACE_ROOT`.
2. Startup cleanup of any leftover directories + background TTL reaper (max 10 minutes).
3. Guaranteed cleanup inside `finally` blocks even on exceptions or timeouts.
4. Files are strictly treated as passive DATA (`<untrusted_file_content>`) and NEVER executed.
5. Memory & CPU bounds on PDF pages, Excel/CSV rows, image resolution, and total extracted characters.
6. File creation (`txt`, `md`, `pdf`, `docx`, `xlsx`, `csv`, and code files) inside the isolated
   temporary directory, sent to the group, and deleted immediately inside `finally`.
"""

from __future__ import annotations

import asyncio
import base64
import csv
import io
import json
import logging
import os
import re
import shutil
import subprocess
import tempfile
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

import openpyxl
from docx import Document as DocxDocument
from PIL import Image
from pypdf import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as pdf_canvas

from bot.locale import fmt_num, t
from bot.security import wrap_untrusted_data

logger = logging.getLogger(__name__)

# Supported input extensions
TEXT_CODE_EXTENSIONS = {
    ".txt", ".md", ".json", ".csv", ".py", ".js", ".ts", ".tsx", ".jsx",
    ".html", ".css", ".sh", ".bash", ".yaml", ".yml", ".toml", ".ini",
    ".cfg", ".sql", ".c", ".cpp", ".h", ".hpp", ".java", ".go", ".rs",
    ".php", ".rb", ".kt", ".swift", ".xml", ".env", ".dockerfile",
}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
DOCUMENT_EXTENSIONS = {".pdf", ".docx", ".xlsx"}
# Audio (voice notes are .ogg Opus) and video, analyzed via Groq Whisper
# transcription + mimo 2.6 vision on sampled frames.
AUDIO_EXTENSIONS = {".mp3", ".wav", ".ogg", ".opus", ".m4a", ".flac", ".aac"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".webm", ".mkv", ".avi"}
ALL_SUPPORTED_INPUT_EXTENSIONS = (
    TEXT_CODE_EXTENSIONS | IMAGE_EXTENSIONS | DOCUMENT_EXTENSIONS
    | AUDIO_EXTENSIONS | VIDEO_EXTENSIONS
)

# Analysis caps for audio/video (kept small: transcription + vision are slow)
MAX_MEDIA_DURATION_SECONDS = 300.0  # 5 min of audio/video
MAX_VIDEO_FRAMES = 6
VIDEO_FRAME_MAX_DIM = 640

# Supported output extensions for file creation tool
SUPPORTED_CREATE_EXTENSIONS = {
    ".txt", ".md", ".pdf", ".docx", ".xlsx", ".csv",
    ".py", ".js", ".ts", ".html", ".css", ".json", ".sql", ".sh", ".yaml", ".cpp", ".go", ".rs",
}


@dataclass
class ExtractedFileData:
    filename: str
    extension: str
    size_bytes: int
    is_image: bool
    extracted_text: str  # Wrapped in <untrusted_file_content>
    image_base64: str | None = None
    image_mime: str | None = None
    short_summary_seed: str = ""
    # Audio/video analysis (set only for audio/video files)
    media_kind: str = "file"  # 'file' | 'image' | 'audio' | 'video'
    audio_path: Path | None = None  # audio file, or the audio track of a video
    video_frames_b64: list[str] = field(default_factory=list)  # JPEG frames for vision
    duration_seconds: float = 0.0


class WorkspaceManager:
    """
    Manages isolated per-request temporary workspaces with:
    - Startup purge of leftover directories
    - Max 10-minute (600s) backup TTL reaper
    - Context manager with guaranteed `finally` deletion
    """

    def __init__(self, root_dir: Path, ttl_seconds: int = 600) -> None:
        self.root_dir = root_dir
        self.ttl_seconds = min(600, max(60, ttl_seconds))
        self.root_dir.mkdir(parents=True, exist_ok=True)

    def cleanup_all_on_startup(self) -> int:
        """Removes any leftover temporary directories from previous runs on bot startup."""
        removed_count = 0
        if not self.root_dir.exists():
            return 0
        for entry in self.root_dir.iterdir():
            try:
                if entry.is_dir():
                    shutil.rmtree(entry, ignore_errors=True)
                else:
                    entry.unlink(missing_ok=True)
                removed_count += 1
            except Exception as exc:
                logger.warning("Startup cleanup error for %s: %s", entry.name, type(exc).__name__)
        logger.info("Workspace startup cleanup finished. Removed %d leftover items.", removed_count)
        return removed_count

    def cleanup_expired_workspaces(self) -> int:
        """Backup TTL reaper: removes any workspace folder older than `ttl_seconds` (max 10 mins)."""
        removed_count = 0
        now = time.time()
        if not self.root_dir.exists():
            return 0
        for entry in self.root_dir.iterdir():
            try:
                stat = entry.stat()
                if (now - stat.st_mtime) > self.ttl_seconds:
                    if entry.is_dir():
                        shutil.rmtree(entry, ignore_errors=True)
                    else:
                        entry.unlink(missing_ok=True)
                    removed_count += 1
            except FileNotFoundError:
                continue
            except Exception as exc:
                logger.warning("TTL cleanup error for %s: %s", entry.name, type(exc).__name__)
        return removed_count

    @contextmanager
    def isolated_workspace(self, prefix: str = "vortex_req_") -> Iterator[Path]:
        """
        Creates an isolated temporary directory for a single file operation and
        guarantees complete deletion in the `finally` block.
        """
        self.root_dir.mkdir(parents=True, exist_ok=True)
        temp_dir = tempfile.mkdtemp(prefix=prefix, dir=str(self.root_dir))
        workspace_path = Path(temp_dir)
        try:
            yield workspace_path
        finally:
            try:
                shutil.rmtree(workspace_path, ignore_errors=True)
            except Exception as exc:
                logger.error("Failed to remove workspace %s: %s", workspace_path.name, type(exc).__name__)


class FileProcessor:
    def __init__(
        self,
        workspace_mgr: WorkspaceManager,
        max_file_size_bytes: int = 20 * 1024 * 1024,
        max_pdf_pages: int = 30,
        max_table_rows: int = 500,
        max_extracted_chars: int = 18000,
        process_timeout_seconds: int = 25,
    ) -> None:
        self.workspace_mgr = workspace_mgr
        self.max_file_size_bytes = max_file_size_bytes
        self.max_pdf_pages = max_pdf_pages
        self.max_table_rows = max_table_rows
        self.max_extracted_chars = max_extracted_chars
        self.process_timeout_seconds = process_timeout_seconds

    @staticmethod
    def sanitize_filename(filename: str) -> str:
        base = os.path.basename(filename or "file.txt")
        safe = re.sub(r"[^\w.\-\u0600-\u06FF]", "_", base)
        return safe[:120] or "file.txt"

    def validate_file_meta(self, filename: str, file_size: int | None) -> tuple[bool, str, str]:
        """
        Checks file size (<= max_file_size_bytes) and extension support
        BEFORE downloading. The limit comes from MAX_FILE_SIZE_MB.
        Returns `(is_valid, extension, error_message)` — the error
        message is localized and user-facing.
        """
        if file_size is not None and file_size > self.max_file_size_bytes:
            limit_mb = self.max_file_size_bytes // (1024 * 1024)
            return (
                False,
                "",
                t("file.too_large", limit=fmt_num(limit_mb)),
            )

        safe_name = self.sanitize_filename(filename)
        ext = Path(safe_name).suffix.lower()
        if not ext:
            # Dotfiles (".env", ".dockerfile") have no suffix — fall back
            # to the full name, which is listed in TEXT_CODE_EXTENSIONS.
            ext = Path(safe_name).name.lower()
        if ext not in ALL_SUPPORTED_INPUT_EXTENSIONS:
            return (
                False,
                ext,
                t("file.bad_format", ext=ext or "unknown"),
            )
        return True, ext, ""

    @staticmethod
    def _probe_duration_seconds(file_path: Path) -> float:
        """Media duration in seconds via ffprobe (-1.0 when unknown).
        -1.0 is returned (not 0.0) so a failed probe cannot silently
        bypass the duration cap: 0.0 > MAX is False, but -1.0 is
        treated as invalid by the callers."""
        try:
            out = subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", str(file_path)],
                capture_output=True, text=True, timeout=30,
            )
            val = float((out.stdout or "").strip() or -1.0)
            return val if val > 0 else -1.0
        except Exception:
            return -1.0

    @staticmethod
    def _extract_video_audio_track(file_path: Path, out_path: Path) -> bool:
        """Extract a video's audio track to MP3 (for Whisper)."""
        try:
            r = subprocess.run(
                ["ffmpeg", "-y", "-v", "error", "-i", str(file_path),
                 "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", str(out_path)],
                capture_output=True, text=True, timeout=120,
            )
            return r.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0
        except Exception:
            return False

    @staticmethod
    def _sample_video_frames(file_path: Path, duration: float, out_dir: Path) -> list[str]:
        """Sample up to MAX_VIDEO_FRAMES JPEG frames evenly across the
        video (scaled to VIDEO_FRAME_MAX_DIM), returned as base64 strings."""
        frames: list[str] = []
        if duration <= 0:
            duration = 10.0
        n = MAX_VIDEO_FRAMES
        # Evenly spaced timestamps, skipping the very first/last frame
        times = [duration * (i + 1) / (n + 1) for i in range(n)]
        for idx, ts in enumerate(times):
            out = out_dir / f"frame_{idx}.jpg"
            try:
                r = subprocess.run(
                    ["ffmpeg", "-y", "-v", "error", "-ss", f"{ts:.2f}",
                     "-i", str(file_path), "-frames:v", "1",
                     "-vf", f"scale={VIDEO_FRAME_MAX_DIM}:-1",
                     "-q:v", "4", str(out)],
                    capture_output=True, text=True, timeout=60,
                )
                if r.returncode == 0 and out.exists() and out.stat().st_size > 0:
                    frames.append(base64.b64encode(out.read_bytes()).decode("ascii"))
            except Exception:
                continue
        return frames

    def _extract_sync(self, file_path: Path, original_name: str, ext: str) -> ExtractedFileData:
        """
        Synchronous extraction helper executed in a worker thread with timeout protection.
        Never executes any file; strictly parses data with resource caps.
        """
        size_bytes = file_path.stat().st_size
        if size_bytes > self.max_file_size_bytes:
            raise ValueError("File exceeds maximum allowed size")

        # 1. Image files
        if ext in IMAGE_EXTENSIONS:
            with Image.open(file_path) as img:
                width, height = img.size
                fmt = (img.format or "PNG").upper()
                # Convert/resize if overly large to cap memory
                img_copy = img.copy()
                img_copy.thumbnail((1600, 1600))
                buf = io.BytesIO()
                save_fmt = "JPEG" if fmt not in {"PNG", "WEBP", "GIF"} else fmt
                if save_fmt == "JPEG" and img_copy.mode not in ("RGB", "L"):
                    img_copy = img_copy.convert("RGB")
                img_copy.save(buf, format=save_fmt, quality=85)
                b64_str = base64.b64encode(buf.getvalue()).decode("ascii")
                mime = f"image/{save_fmt.lower()}"

            meta_desc = f"تصویر با نام {original_name}، ابعاد {width}x{height} پیکسل، فرمت {fmt}."
            return ExtractedFileData(
                filename=original_name,
                extension=ext,
                size_bytes=size_bytes,
                is_image=True,
                extracted_text=wrap_untrusted_data("untrusted_file_content", meta_desc),
                image_base64=b64_str,
                image_mime=mime,
                short_summary_seed=meta_desc,
            )

        # 1b. Audio files: keep the file for Groq Whisper transcription.
        if ext in AUDIO_EXTENSIONS:
            duration = self._probe_duration_seconds(file_path)
            if duration < 0:
                raise ValueError("Could not determine audio duration")
            if duration > MAX_MEDIA_DURATION_SECONDS:
                raise ValueError("Audio exceeds maximum duration")
            meta_desc = f"فایل صوتی با نام {original_name}، مدت {duration:.0f} ثانیه، فرمت {ext}."
            return ExtractedFileData(
                filename=original_name,
                extension=ext,
                size_bytes=size_bytes,
                is_image=False,
                extracted_text=wrap_untrusted_data("untrusted_file_content", meta_desc),
                short_summary_seed=meta_desc,
                media_kind="audio",
                audio_path=file_path,
                duration_seconds=duration,
            )

        # 1c. Video files: audio track (Whisper) + sampled frames (mimo vision).
        if ext in VIDEO_EXTENSIONS:
            duration = self._probe_duration_seconds(file_path)
            if duration < 0:
                raise ValueError("Could not determine video duration")
            if duration > MAX_MEDIA_DURATION_SECONDS:
                raise ValueError("Video exceeds maximum duration")
            audio_out = file_path.parent / (file_path.stem + "_audio.mp3")
            has_audio = self._extract_video_audio_track(file_path, audio_out)
            frames = self._sample_video_frames(file_path, duration, file_path.parent)
            meta_desc = (
                f"فایل ویدیویی با نام {original_name}، مدت {duration:.0f} ثانیه، "
                f"فرمت {ext}، {len(frames)} فریم نمونه و "
                f"{'صدا دارد' if has_audio else 'بدون صدا'}."
            )
            return ExtractedFileData(
                filename=original_name,
                extension=ext,
                size_bytes=size_bytes,
                is_image=False,
                extracted_text=wrap_untrusted_data("untrusted_file_content", meta_desc),
                short_summary_seed=meta_desc,
                media_kind="video",
                audio_path=audio_out if has_audio else None,
                video_frames_b64=frames,
                duration_seconds=duration,
            )

        # 2. PDF files (capped at max_pdf_pages)
        if ext == ".pdf":
            reader = PdfReader(str(file_path))
            total_pages = len(reader.pages)
            pages_to_read = min(total_pages, self.max_pdf_pages)
            chunks: list[str] = [
                f"نام فایل PDF: {original_name} | تعداد کل صفحات: {total_pages} (خوانده شده: {pages_to_read} صفحه)"
            ]
            total_chars = 0
            for idx in range(pages_to_read):
                page_text = reader.pages[idx].extract_text() or ""
                chunks.append(f"--- صفحه {idx + 1} ---\n{page_text.strip()}")
                total_chars += len(page_text)
                if total_chars >= self.max_extracted_chars:
                    chunks.append("[ادامه متن به دلیل سقف حجم پردازش خلاصه/بریده شد...]")
                    break
            raw_text = "\n\n".join(chunks)[: self.max_extracted_chars]
            return ExtractedFileData(
                filename=original_name,
                extension=ext,
                size_bytes=size_bytes,
                is_image=False,
                extracted_text=wrap_untrusted_data("untrusted_file_content", raw_text),
                short_summary_seed=raw_text[:600],
            )

        # 3. Word (.docx) files
        if ext == ".docx":
            doc = DocxDocument(str(file_path))
            parts: list[str] = [f"نام فایل Word: {original_name}"]
            char_count = 0
            for para in doc.paragraphs:
                txt = para.text.strip()
                if txt:
                    parts.append(txt)
                    char_count += len(txt)
                    if char_count >= self.max_extracted_chars:
                        break
            for t_idx, table in enumerate(doc.tables[:10]):
                parts.append(f"[جدول {t_idx + 1}]")
                for row in table.rows[: self.max_table_rows]:
                    row_txt = " | ".join(cell.text.strip() for cell in row.cells)
                    parts.append(row_txt)
                    char_count += len(row_txt)
                    if char_count >= self.max_extracted_chars:
                        break
            raw_text = "\n".join(parts)[: self.max_extracted_chars]
            return ExtractedFileData(
                filename=original_name,
                extension=ext,
                size_bytes=size_bytes,
                is_image=False,
                extracted_text=wrap_untrusted_data("untrusted_file_content", raw_text),
                short_summary_seed=raw_text[:600],
            )

        # 4. Excel (.xlsx) files (read_only=True, capped at max_table_rows)
        if ext == ".xlsx":
            wb = openpyxl.load_workbook(str(file_path), read_only=True, data_only=True)
            try:
                parts = [f"نام فایل Excel: {original_name} | شیت‌ها: {', '.join(wb.sheetnames)}"]
                char_count = 0
                for sheet_name in wb.sheetnames[:5]:
                    ws = wb[sheet_name]
                    parts.append(f"=== شیت: {sheet_name} ===")
                    for row_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
                        if row_idx > self.max_table_rows:
                            parts.append(f"[سایر ردیف‌ها پس از ردیف {self.max_table_rows} نادیده گرفته شدند]")
                            break
                        row_vals = [str(cell) if cell is not None else "" for cell in row[:30]]
                        if any(row_vals):
                            line = " | ".join(row_vals)
                            parts.append(line)
                            char_count += len(line)
                            if char_count >= self.max_extracted_chars:
                                break
                raw_text = "\n".join(parts)[: self.max_extracted_chars]
            finally:
                wb.close()
            return ExtractedFileData(
                filename=original_name,
                extension=ext,
                size_bytes=size_bytes,
                is_image=False,
                extracted_text=wrap_untrusted_data("untrusted_file_content", raw_text),
                short_summary_seed=raw_text[:600],
            )

        # 5. CSV files (capped at max_table_rows)
        if ext == ".csv":
            raw_bytes = file_path.read_bytes()[: self.max_file_size_bytes]
            text_content = raw_bytes.decode("utf-8", errors="replace")
            reader = csv.reader(io.StringIO(text_content))
            lines = [f"نام فایل CSV: {original_name}"]
            for idx, row in enumerate(reader, start=1):
                if idx > self.max_table_rows:
                    lines.append(f"[سایر ردیف‌ها پس از ردیف {self.max_table_rows} نادیده گرفته شدند]")
                    break
                lines.append(" | ".join(row[:30]))
                if sum(len(x) for x in lines) >= self.max_extracted_chars:
                    break
            raw_text = "\n".join(lines)[: self.max_extracted_chars]
            return ExtractedFileData(
                filename=original_name,
                extension=ext,
                size_bytes=size_bytes,
                is_image=False,
                extracted_text=wrap_untrusted_data("untrusted_file_content", raw_text),
                short_summary_seed=raw_text[:600],
            )

        # 6. JSON files
        if ext == ".json":
            raw_bytes = file_path.read_bytes()[: self.max_file_size_bytes]
            text_content = raw_bytes.decode("utf-8", errors="replace")
            try:
                parsed = json.loads(text_content)
                pretty = json.dumps(parsed, ensure_ascii=False, indent=2)[: self.max_extracted_chars]
            except Exception:
                pretty = text_content[: self.max_extracted_chars]
            payload = f"نام فایل JSON: {original_name}\n{pretty}"
            return ExtractedFileData(
                filename=original_name,
                extension=ext,
                size_bytes=size_bytes,
                is_image=False,
                extracted_text=wrap_untrusted_data("untrusted_file_content", payload),
                short_summary_seed=payload[:600],
            )

        # 7. Plain text, Markdown, and source code files
        raw_bytes = file_path.read_bytes()[: self.max_file_size_bytes]
        text_content = raw_bytes.decode("utf-8", errors="replace")[: self.max_extracted_chars]
        payload = f"نام فایل: {original_name}\n\n{text_content}"
        return ExtractedFileData(
            filename=original_name,
            extension=ext,
            size_bytes=size_bytes,
            is_image=False,
            extracted_text=wrap_untrusted_data("untrusted_file_content", payload),
            short_summary_seed=payload[:600],
        )

    async def extract_from_path(self, file_path: Path, original_name: str, ext: str) -> ExtractedFileData:
        """Runs file extraction with an async timeout cap. Video needs
        far more than the default 25s (ffprobe + a 120s ffmpeg audio
        extraction + up to 6 frame grabs), so the timeout is per-kind:
        300s for video, 180s for audio, 25s otherwise. Note: wait_for
        cancels only the awaiting coroutine, not the worker thread, so
        a timed-out ffmpeg keeps running in the background — the
        per-kind timeout keeps that rare instead of routine."""
        if ext in VIDEO_EXTENSIONS:
            timeout = 300
        elif ext in AUDIO_EXTENSIONS:
            timeout = 180
        else:
            timeout = self.process_timeout_seconds
        return await asyncio.wait_for(
            asyncio.to_thread(self._extract_sync, file_path, original_name, ext),
            timeout=timeout,
        )

    # ------------------------------------------------------------------
    # File Creation in Temporary Workspace
    # ------------------------------------------------------------------

    def build_file_in_workspace(
        self,
        workspace_dir: Path,
        filename: str,
        content: str,
    ) -> Path:
        """
        Generates a file (`txt`, `md`, `pdf`, `docx`, `xlsx`, `csv`, or code file)
        inside `workspace_dir` and returns its path.
        """
        safe_name = self.sanitize_filename(filename)
        ext = Path(safe_name).suffix.lower()
        if not ext:
            safe_name += ".txt"
            ext = ".txt"
        if ext not in SUPPORTED_CREATE_EXTENSIONS:
            safe_name = Path(safe_name).stem + ".txt"
            ext = ".txt"

        out_path = workspace_dir / safe_name

        if ext == ".docx":
            doc = DocxDocument()
            for line in content.splitlines():
                if line.startswith("# "):
                    doc.add_heading(line[2:].strip(), level=1)
                elif line.startswith("## "):
                    doc.add_heading(line[3:].strip(), level=2)
                else:
                    doc.add_paragraph(line)
            doc.save(str(out_path))
            return out_path

        if ext == ".xlsx":
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "VortexData"
            ws.sheet_view.rightToLeft = True

            def _safe_cell(value: object) -> str:
                """Prefix formula-leading cells with a quote so LLM content
                (which may echo untrusted web text) starting with =, +,
                - or @ is stored as text, not a live spreadsheet formula."""
                s = str(value)
                if s[:1] in ("=", "+", "-", "@"):
                    return "'" + s
                return s

            # Try parsing CSV/pipe/tab lines or JSON array into rows
            rows_written = False
            try:
                parsed = json.loads(content)
                if isinstance(parsed, list):
                    header: list[str] | None = None
                    for item in parsed:
                        if isinstance(item, dict):
                            if header is None:
                                header = list(item.keys())
                                ws.append([_safe_cell(k) for k in header])
                                rows_written = True
                            # Align every row to the FIRST dict's header,
                            # not each dict's own key order.
                            ws.append(
                                [_safe_cell(item.get(k, "")) for k in header]
                            )
                        elif isinstance(item, list):
                            ws.append([_safe_cell(v) for v in item])
                            rows_written = True
            except Exception:
                pass

            if not rows_written:
                for line in content.splitlines():
                    if "|" in line:
                        cells = [c.strip() for c in line.strip("|").split("|")]
                    elif "," in line:
                        cells = next(csv.reader([line]))
                    else:
                        cells = [line]
                    ws.append([_safe_cell(c) for c in cells])
            wb.save(str(out_path))
            return out_path

        if ext == ".csv":
            with out_path.open("w", encoding="utf-8-sig", newline="") as f:
                writer = csv.writer(f)
                for line in content.splitlines():
                    if "|" in line:
                        writer.writerow([c.strip() for c in line.strip("|").split("|")])
                    else:
                        for row in csv.reader([line]):
                            writer.writerow(row)
            return out_path

        if ext == ".pdf":
            c = pdf_canvas.Canvas(str(out_path), pagesize=A4)
            width, height = A4
            y = height - 50
            # Persian needs a real Arabic-script font + shaping + bidi.
            # Vazirmatn is bundled with the bot (fonts/Vazirmatn-Regular.ttf);
            # arabic_reshaper + python-bidi shape and reorder RTL text.
            # Falls back to Helvetica (Latin only) when the font or the
            # shaping libraries are missing, so PDF creation never crashes.
            font_name = "Helvetica"
            reshaper = None
            bidi_algo = None
            try:
                from reportlab.pdfbase import pdfmetrics
                from reportlab.pdfbase.ttfonts import TTFont

                font_path = Path(__file__).resolve().parent.parent / "fonts" / "Vazirmatn-Regular.ttf"
                if font_path.exists():
                    pdfmetrics.registerFont(TTFont("Vazirmatn", str(font_path)))
                    font_name = "Vazirmatn"
            except Exception:
                font_name = "Helvetica"
            try:
                import arabic_reshaper
                from bidi.algorithm import get_display

                reshaper = arabic_reshaper
                bidi_algo = get_display
            except Exception:
                reshaper = None
                bidi_algo = None
            c.setFont(font_name, 11)
            for line in content.splitlines():
                # Wrap long lines
                for chunk_start in range(0, max(1, len(line)), 90):
                    segment = line[chunk_start : chunk_start + 90]
                    if reshaper is not None and bidi_algo is not None:
                        shaped = bidi_algo(reshaper.reshape(segment))
                        # Right-align: Persian reads right-to-left.
                        c.drawRightString(width - 45, y, shaped)
                    else:
                        c.drawString(45, y, segment)
                    y -= 16
                    if y < 50:
                        c.showPage()
                        c.setFont(font_name, 11)
                        y = height - 50
            c.save()
            return out_path

        # Default: txt, md, json, or code files (.py, .js, .html, etc.)
        out_path.write_text(content, encoding="utf-8")
        return out_path


def get_file_creation_tool_schema() -> dict[str, Any]:
    """Returns OpenAI-compatible tool schema for generating a file to send to the Telegram group."""
    return {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": (
                "ساخت و ارسال فایل در گروه تلگرام. فرمت‌های مجاز: "
                "txt, md, pdf, docx, xlsx, csv و فایل‌های کد (مثل py, js, html, json, sql)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "نام فایل به همراه پسوند (مثلاً report.docx یا data.xlsx یا script.py)",
                    },
                    "content": {
                        "type": "string",
                        "description": "محتوای کامل فایل (برای xlsx و csv می‌توان خطوط جداشده با کاما یا | یا آرایه JSON داد)",
                    },
                    "caption": {
                        "type": "string",
                        "description": "توضیح کوتاه و شوخ‌طبعانه که همراه فایل در گروه ارسال می‌شود",
                    },
                },
                "required": ["filename", "content"],
            },
        },
    }
