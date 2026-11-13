#!/usr/bin/env python3
"""Patch README.<lang>.md files translated from the 22-language source
up to the 40-language source.

Two mechanical fixes, both idempotent:
  1. The language-links line (line 3) is replaced with the generated
     40-language block for that language (own language bold).
  2. The two "195 countries and 22 languages" lines (the Features
     bullet starting with "- 🌍" and the Countries paragraph starting
     with "Vortex") get their 22 rendered as 40 — in whatever digit
     system the translation uses (Latin 22, Persian ۲۲, Arabic ٢٢,
     Devanagari २२, ...). The number is found by value, not by glyph,
     so any Unicode decimal-digit script works. A line whose 22 is
     written out as a word is reported, not guessed.

Files already translated from the 40-language source are left alone
(the script detects "already 40" and skips them).

Usage: python3 scripts/patch_readme_40.py [--check] [--langs fa,tr]
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

ORDER = ["en", "fa", "tr", "de", "fr", "es", "it", "nl", "ru", "uk", "pl",
         "sv", "pt", "ar", "hi", "ur", "zh", "ja", "ko", "id", "th", "vi",
         "ms", "bn", "pa", "mr", "te", "ta", "gu", "am", "sw", "ha", "fil",
         "ro", "hu", "cs", "el", "he", "da", "no"]
NATIVE = {
    "en": "English", "fa": "فارسی", "tr": "Türkçe", "de": "Deutsch",
    "fr": "Français", "es": "Español", "it": "Italiano",
    "nl": "Nederlands", "ru": "Русский", "uk": "Українська",
    "pl": "Polski", "sv": "Svenska", "pt": "Português", "ar": "العربية",
    "hi": "हिन्दी", "ur": "اردو", "zh": "中文", "ja": "日本語",
    "ko": "한국어", "id": "Bahasa Indonesia", "th": "ไทย",
    "vi": "Tiếng Việt", "ms": "Bahasa Melayu", "bn": "বাংলা", "pa": "ਪੰਜਾਬੀ", "mr": "मराठी",
    "te": "తెలుగు", "ta": "தமிழ்", "gu": "ગુજરાતી", "am": "አማርኛ",
    "sw": "Kiswahili", "ha": "Hausa", "fil": "Filipino", "ro": "Română",
    "hu": "Magyar", "cs": "Čeština", "el": "Ελληνικά", "he": "עברית",
    "da": "Dansk", "no": "Norsk",
}

DIGITS_RE = re.compile(r"\d+", re.UNICODE)


def run_value(run: str) -> int:
    """Integer value of a Unicode decimal-digit run, any script."""
    return int("".join(str(unicodedata.digit(ch)) for ch in run))


def render_in_script(value: int, run: str) -> str:
    """Render `value` using the digit glyphs of `run`'s script."""
    zero = ord(run[0]) - unicodedata.digit(run[0])
    return "".join(chr(zero + int(d)) for d in str(value))


def links_line_for(lang: str) -> str:
    parts = []
    for code in ORDER:
        name = NATIVE[code]
        if code == lang:
            parts.append(f"**{name}**")
        else:
            fname = "README.md" if code == "en" else f"README.{code}.md"
            parts.append(f"[{name}]({fname})")
    return " · ".join(parts)


def patch(text: str, lang: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    lines = text.split("\n")
    # 1. links line (line 3): regenerate the 40-language block.
    want_links = links_line_for(lang)
    if lines[2] != want_links:
        if "README." not in lines[2] and "**" not in lines[2]:
            notes.append("WARN: line 3 does not look like the links block")
        else:
            lines[2] = want_links
            notes.append("links block -> 40 languages")
    # 2. the two count lines: "- 🌍 ..." and "Vortex ...".
    for i, line in enumerate(lines):
        if not (line.startswith("- 🌍") or line.startswith("Vortex")):
            continue
        runs = [(m.group(0), m.start(), m.end())
                for m in DIGITS_RE.finditer(line)]
        values = [(run, run_value(run)) for run, _, _ in runs]
        if not any(v == 195 for _, v in values):
            continue  # not a count line (e.g. "Vortex" in other contexts)
        if any(v == 40 for _, v in values):
            continue  # already patched
        hit = [r for r, v in values if v == 22]
        if not hit:
            notes.append(f"WARN: line {i + 1} has 195 but no 22-valued "
                         "digit run (number written as a word?)")
            continue
        run = hit[0]
        lines[i] = line.replace(run, render_in_script(40, run), 1)
        notes.append(f"line {i + 1}: 22 -> 40 "
                     f"({run} -> {render_in_script(40, run)})")
    return "\n".join(lines), notes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--langs", default="")
    args = parser.parse_args()
    langs = ([c.strip() for c in args.langs.split(",") if c.strip()]
             if args.langs else [p.name[7:-3] for p in
                                 sorted(REPO.glob("README.*.md"))])
    problems = 0
    for lang in langs:
        path = REPO / f"README.{lang}.md"
        if not path.exists():
            print(f"SKIP README.{lang}.md: not downloaded yet")
            continue
        text = path.read_text(encoding="utf-8")
        fixed, notes = patch(text, lang)
        warns = [n for n in notes if n.startswith("WARN")]
        problems += len(warns)
        if fixed != text and not args.check:
            path.write_text(fixed, encoding="utf-8")
        status = "would patch" if args.check else "patched"
        print(f"{path.name}: {status}: "
              f"{'; '.join(notes) if notes else 'already 40, no change'}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
