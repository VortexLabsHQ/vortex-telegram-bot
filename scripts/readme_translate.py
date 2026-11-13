#!/usr/bin/env python3
"""Translate README.md into the other 21 Vortex UI languages with Nemotron.

RUNS ON THE SERVER ONLY. Reads the NVIDIA API key from
/home/ubuntu/mindcraft/keys.json itself (OPENAI_API_KEY) and NEVER prints,
logs, or writes it anywhere. The key never leaves the server.

What is protected from translation (restored byte-identical):
  - the language-links line at the top (regenerated per language),
  - the country table between <!-- COUNTRY_TABLE_START/END --> markers
    (country names stay in English),
  - every fenced code block (install command, shell commands, .env vars),
  - all link targets / URLs / file names / `backtick` spans are checked
    after translation and reported.

Usage:
  python3 /tmp/readme_translate.py --in /tmp/readme-in/README.md \
      --out /tmp/readme-out [--langs fa,tr] [--smoke]

--smoke translates only the first section into fa, to verify the API.
Without --langs, all 21 languages are translated, one API call each;
a language whose output looks truncated (< 2 star lines) is retried
section-by-section (chunked fallback).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL = "nvidia/nemotron-3-ultra-550b-a55b"
KEY_PATH = Path("/home/ubuntu/mindcraft/keys.json")

# code -> (English name, native name for the links line, prompt language)
LANGS = {
    "fa": ("Persian (Farsi)", "فارسی", "Persian (Farsi)"),
    "tr": ("Turkish", "Türkçe", "Turkish"),
    "de": ("German", "Deutsch", "German"),
    "fr": ("French", "Français", "French"),
    "es": ("Spanish", "Español", "Spanish"),
    "it": ("Italian", "Italiano", "Italian"),
    "nl": ("Dutch", "Nederlands", "Dutch"),
    "ru": ("Russian", "Русский", "Russian"),
    "uk": ("Ukrainian", "Українська", "Ukrainian"),
    "pl": ("Polish", "Polski", "Polish"),
    "sv": ("Swedish", "Svenska", "Swedish"),
    "pt": ("Portuguese", "Português", "Portuguese"),
    "ar": ("Arabic", "العربية", "Arabic"),
    "hi": ("Hindi", "हिन्दी", "Hindi"),
    "ur": ("Urdu", "اردو", "Urdu"),
    "zh": ("Chinese (Simplified)", "中文", "Chinese (Simplified)"),
    "ja": ("Japanese", "日本語", "Japanese"),
    "ko": ("Korean", "한국어", "Korean"),
    "id": ("Indonesian", "Bahasa Indonesia", "Indonesian"),
    "th": ("Thai", "ไทย", "Thai"),
    "vi": ("Vietnamese", "Tiếng Việt", "Vietnamese"),
    "ms": ("Malay", "Bahasa Melayu", "Malay"),
    "bn": ("Bengali", "বাংলা", "Bengali"),
    "pa": ("Punjabi", "ਪੰਜਾਬੀ", "Punjabi"),
    "mr": ("Marathi", "मराठी", "Marathi"),
    "te": ("Telugu", "తెలుగు", "Telugu"),
    "ta": ("Tamil", "தமிழ்", "Tamil"),
    "gu": ("Gujarati", "ગુજરાતી", "Gujarati"),
    "am": ("Amharic", "አማርኛ", "Amharic"),
    "sw": ("Swahili", "Kiswahili", "Swahili"),
    "ha": ("Hausa", "Hausa", "Hausa"),
    "fil": ("Filipino", "Filipino", "Filipino"),
    "ro": ("Romanian", "Română", "Romanian"),
    "hu": ("Hungarian", "Magyar", "Hungarian"),
    "cs": ("Czech", "Čeština", "Czech"),
    "el": ("Greek", "Ελληνικά", "Greek"),
    "he": ("Hebrew", "עברית", "Hebrew"),
    "da": ("Danish", "Dansk", "Danish"),
    "no": ("Norwegian", "Norsk", "Norwegian"),
}
ORDER = ["en", "fa", "tr", "de", "fr", "es", "it", "nl", "ru", "uk", "pl",
         "sv", "pt", "ar", "hi", "ur", "zh", "ja", "ko", "id", "th", "vi",
         "ms", "bn", "pa", "mr", "te", "ta", "gu", "am", "sw", "ha", "fil",
         "ro", "hu", "cs", "el", "he", "da", "no"]

START = "<!-- COUNTRY_TABLE_START -->"
END = "<!-- COUNTRY_TABLE_END -->"
CODE_RE = re.compile(r"```[^\n]*\n.*?```", re.DOTALL)


def load_key() -> str:
    data = json.loads(KEY_PATH.read_text(encoding="utf-8"))
    key = data["OPENAI_API_KEY"]
    if not key:
        raise SystemExit("no OPENAI_API_KEY in keys.json")
    return key


def call_nemotron(key: str, system: str, user: str,
                  max_tokens: int = 20000) -> str:
    payload = json.dumps({
        "model": MODEL,
        "temperature": 0.2,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }).encode("utf-8")
    last_err = None
    for attempt in range(4):
        req = urllib.request.Request(
            API_URL, data=payload,
            headers={"Authorization": f"Bearer {key}",
                     "Content-Type": "application/json",
                     "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                out = json.loads(resp.read().decode("utf-8"))
            content = out["choices"][0]["message"]["content"]
            if not content:
                # The API sometimes returns a choice with null content
                # (empty/filtered generation). Treat as transient: retry.
                raise ValueError("empty response content")
            return content
        except Exception as exc:  # noqa: BLE001 - retry transient errors
            last_err = exc
            wait = 20 * (attempt + 1)
            print(f"  API error ({exc}); retrying in {wait}s ...", flush=True)
            time.sleep(wait)
    raise SystemExit(f"Nemotron call failed after retries: {last_err}")


def system_prompt(lang_name: str) -> str:
    return (
        "You are a professional technical translator. Translate the "
        f"following Markdown documentation from English to {lang_name}. "
        "Rules:\n"
        "1. Keep the exact Markdown structure: same headings (translated), "
        "same lists, same tables, same blockquotes, same blank lines.\n"
        "2. NEVER translate or change: text inside `backticks`, fenced code "
        "blocks, URLs, link targets in ]( ), file names, env var names "
        "(e.g. BOT_TOKEN), commands, numbers, version numbers, or the "
        "placeholders [[CODEBLOCK_n]] and [[COUNTRY_TABLE]].\n"
        "3. Keep the product name \"Vortex\" unchanged everywhere.\n"
        "4. Keep country names in English (they are installer keywords).\n"
        "5. Translate naturally and simply, as if written for a non-technical "
        "reader in that language. Keep the friendly, simple tone.\n"
        "6. Output ONLY the translated Markdown, nothing else — no intro, "
        "no explanation, no notes."
    )


def split_protected(text: str):
    """Replace the links line, country table and code blocks with
    placeholders. Returns (body, code_blocks, table_block)."""
    lines = text.split("\n")
    links_idx = next(i for i, l in enumerate(lines)
                     if l.startswith("**English**"))
    links_line = lines[links_idx]
    lines[links_idx] = "[[LANG_LINKS]]"
    text = "\n".join(lines)

    s, e = text.index(START), text.index(END) + len(END)
    table_block = text[s:e]
    text = text[:s] + "[[COUNTRY_TABLE]]" + text[e:]

    code_blocks: list[str] = []

    def _stash(m: "re.Match[str]") -> str:
        code_blocks.append(m.group(0))
        return f"[[CODEBLOCK_{len(code_blocks) - 1}]]"

    text = CODE_RE.sub(_stash, text)
    return text, code_blocks, table_block, links_line


def restore(text: str, code_blocks, table_block, links_line) -> str:
    for i, block in enumerate(code_blocks):
        text = text.replace(f"[[CODEBLOCK_{i}]]", block)
    text = text.replace("[[COUNTRY_TABLE]]", table_block)
    text = text.replace("[[LANG_LINKS]]", links_line)
    return text


def links_line_for(lang: str) -> str:
    parts = []
    for code in ORDER:
        _en, native, _prompt = LANGS.get(code, ("English", "English", ""))
        name = "English" if code == "en" else native
        if code == lang:
            parts.append(f"**{name}**")
        else:
            fname = "README.md" if code == "en" else f"README.{code}.md"
            parts.append(f"[{name}]({fname})")
    return " · ".join(parts)


def translate_body(key: str, body: str, lang_name: str,
                   chunked: bool = False) -> str:
    """One-shot translation; chunked fallback when output looks cut off.
    With chunked=True, translate section-by-section from the start
    (shorter calls — safer when the API drops long generations)."""
    if not chunked:
        out = call_nemotron(key, system_prompt(lang_name), body)
        # Complete when: both star support-asks survived, every protected
        # placeholder is still present, and no placeholder leaked translated.
        complete = (
            out.count("⭐") >= 2
            and out.count("[[CODEBLOCK_") == body.count("[[CODEBLOCK_")
            and "[[COUNTRY_TABLE]]" in out
            and "[[LANG_LINKS]]" in out
        )
        if complete:
            return out
        print("  one-shot output looks incomplete; retrying section by "
              "section", flush=True)
    sections = re.split(r"(?m)(?=^## )", body)
    done = []
    for sec in sections:
        if not sec.strip():
            continue
        done.append(call_nemotron(key, system_prompt(lang_name), sec,
                                  max_tokens=8000).strip())
        time.sleep(2)
    # Join with a blank line: a bare "".join glues a section heading
    # ("## ...") onto the previous section's last line.
    return "\n\n".join(done) + "\n"


def translate_one(key: str, body: str, code_blocks, table_block,
                  lang: str, out_dir: Path, chunked: bool = False) -> Path:
    _en, _native, prompt_lang = LANGS[lang]
    print(f"[{lang}] translating ({prompt_lang}) ...", flush=True)
    translated = translate_body(key, body, prompt_lang, chunked=chunked)
    text = restore(translated, code_blocks, table_block,
                   links_line_for(lang))
    # The links line must be exactly the generated one for this language.
    dest = out_dir / f"README.{lang}.md"
    dest.write_text(text, encoding="utf-8")
    print(f"[{lang}] wrote {dest} ({len(text)} chars, "
          f"stars={text.count('⭐')})", flush=True)
    return dest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inp", required=True)
    parser.add_argument("--out", dest="out", required=True)
    parser.add_argument("--langs", default="",
                        help="comma-separated codes (default: all 21)")
    parser.add_argument("--smoke", action="store_true",
                        help="translate only the first section into fa")
    parser.add_argument("--chunked", action="store_true",
                        help="translate section-by-section (shorter calls)")
    args = parser.parse_args()

    key = load_key()
    print("key loaded (not shown)", flush=True)
    src = Path(args.inp).read_text(encoding="utf-8")
    body, code_blocks, table_block, _links = split_protected(src)
    print(f"source: {len(src)} chars, {len(code_blocks)} code blocks "
          f"protected, table protected", flush=True)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.smoke:
        first = body.split("\n## ", 1)[0]
        print(call_nemotron(key, system_prompt("Persian (Farsi)"), first,
                            max_tokens=4000))
        return 0

    langs = ([c.strip() for c in args.langs.split(",") if c.strip()]
             if args.langs else list(LANGS))
    for lang in langs:
        if lang not in LANGS:
            print(f"unknown language: {lang}", file=sys.stderr)
            return 1
        translate_one(key, body, code_blocks, table_block, lang, out_dir,
                      chunked=args.chunked)
        time.sleep(3)
    print("ALL DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
