"""Audio transcription for the Vortex bot (Groq Whisper via the local proxy).

TokenHarbor does NOT offer an audio transcription endpoint (its /v1/audio/*
routes return 404), and mimo 2.6 rejects audio input in chat completions,
so speech is transcribed with Groq Whisper (whisper-large-v3-turbo) through
the existing nginx groq-forward proxy on 127.0.0.1:8090, which injects the
Groq API key — no key is needed in this code. The transcript is then passed
to the LLM (mimo 2.6 / DeepSeek) for analysis, so mimo still does the
"understanding" of what was said.
"""

from __future__ import annotations

import logging
from pathlib import Path

import httpx

logger = logging.getLogger(__name__)

DEFAULT_WHISPER_URL = "http://127.0.0.1:8090/openai/v1/audio/transcriptions"
DEFAULT_WHISPER_MODEL = "whisper-large-v3-turbo"

# Whisper accepts these (Groq). Telegram voice notes are .ogg (Opus).
_WHISPER_MIME = {
    ".mp3": "audio/mpeg",
    ".mp4": "audio/mp4",
    ".m4a": "audio/mp4",
    ".wav": "audio/wav",
    ".webm": "audio/webm",
    ".ogg": "audio/ogg",
    ".opus": "audio/ogg",
    ".flac": "audio/flac",
    ".aac": "audio/aac",
}


async def transcribe_audio(
    audio_path: Path,
    *,
    whisper_url: str = DEFAULT_WHISPER_URL,
    model: str = DEFAULT_WHISPER_MODEL,
    language: str | None = None,
    timeout_seconds: float = 120.0,
) -> str:
    """Transcribe an audio file with Groq Whisper. Returns the transcript
    text ('' when there is no speech). Raises on HTTP/network failure."""
    ext = audio_path.suffix.lower()
    mime = _WHISPER_MIME.get(ext, "audio/mpeg")
    data: dict[str, str] = {"model": model, "response_format": "json"}
    if language:
        data["language"] = language
    async with httpx.AsyncClient(timeout=timeout_seconds) as client:
        with audio_path.open("rb") as fh:
            files = {"file": (audio_path.name, fh, mime)}
            r = await client.post(whisper_url, files=files, data=data)
        r.raise_for_status()
        payload = r.json()
        text = (payload.get("text") or "").strip()
        return text
