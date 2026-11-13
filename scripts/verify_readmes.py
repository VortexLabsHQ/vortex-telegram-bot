#!/usr/bin/env python3
"""Verify every README.<lang>.md against README.md (English).

Checks per language:
  1. File exists and parses as Markdown (balanced ``` fences).
  2. Install command byte-identical to the English README.
  3. Country table byte-identical to the English README (195 rows).
  4. Language-links block at the top: links to all 22 README files,
     current language bold, others linked.
  5. Support ask (⭐) present near the start AND near the end.
  6. Same `##` heading count as English, same link targets, same
     fenced code blocks (byte-identical).
  7. No placeholder text (TODO, Lorem, [translation], [[...]] leftovers).
  8. Script check: the text is actually in the target language's script
     (Arabic script for fa/ar/ur, Cyrillic for ru/uk, CJK for zh/ja,
     Hangul for ko, Thai for th, Devanagari for hi) and not just English.

Usage: python3 scripts/verify_readmes.py [--langs fa,tr]
Exit 0 when every checked language passes.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

LANGS = ["fa", "tr", "de", "fr", "es", "it", "nl", "ru", "uk", "pl", "sv",
         "pt", "ar", "hi", "ur", "zh", "ja", "ko", "id", "th", "vi",
         "ms", "bn", "pa", "mr", "te", "ta", "gu", "am", "sw", "ha", "fil",
         "ro", "hu", "cs", "el", "he", "da", "no"]
ALL = ["en"] + LANGS

INSTALL_CMD = ("curl -sSL https://raw.githubusercontent.com/"
               "VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash")
START = "<!-- COUNTRY_TABLE_START -->"
END = "<!-- COUNTRY_TABLE_END -->"

# Unicode ranges that must appear in the translation (sample of the body
# outside code blocks and the country table).
SCRIPT_RANGES = {
    "fa": [("\u0600", "\u06ff")],
    "ar": [("\u0600", "\u06ff")],
    "ur": [("\u0600", "\u06ff")],
    "ru": [("\u0400", "\u04ff")],
    "uk": [("\u0400", "\u04ff")],
    "zh": [("\u4e00", "\u9fff")],
    "ja": [("\u3040", "\u30ff"), ("\u4e00", "\u9fff")],
    "ko": [("\uac00", "\ud7a3")],
    "th": [("\u0e00", "\u0e7f")],
    "hi": [("\u0900", "\u097f")],
    "bn": [("\u0980", "\u09ff")],
    "pa": [("\u0a00", "\u0a7f")],
    "mr": [("\u0900", "\u097f")],
    "te": [("\u0c00", "\u0c7f")],
    "ta": [("\u0b80", "\u0bff")],
    "gu": [("\u0a80", "\u0aff")],
    "am": [("\u1200", "\u137f")],
    "el": [("\u0370", "\u03ff")],
    "he": [("\u0590", "\u05ff")],
}

PLACEHOLDERS = ("TODO", "Lorem", "[translation]", "[[CODEBLOCK_",
                "[[COUNTRY_TABLE]]", "[[LANG_LINKS]]")


def table_block(text: str) -> str:
    return text[text.index(START):text.index(END) + len(END)]


def code_blocks(text: str) -> list[str]:
    return re.findall(r"```[^\n]*\n.*?```", text, re.DOTALL)


def link_targets(text: str) -> list[str]:
    return sorted(re.findall(r"\]\(([^)\s]+)\)", text))


def headings(text: str) -> list[str]:
    return re.findall(r"(?m)^## .+$", text)


def check(lang: str, en: str) -> list[str]:
    path = REPO / f"README.{lang}.md"
    problems: list[str] = []
    if not path.exists():
        return [f"missing file {path.name}"]
    text = path.read_text(encoding="utf-8")

    # 1. fence balance
    if text.count("```") % 2:
        problems.append("unbalanced ``` fences")

    # 2. install command byte-identical
    if INSTALL_CMD not in text:
        problems.append("install command missing or changed")
    elif text.count(INSTALL_CMD) != en.count(INSTALL_CMD):
        problems.append("install command count differs from English")

    # 3. country table byte-identical
    try:
        if table_block(text) != table_block(en):
            problems.append("country table differs from English")
    except ValueError:
        problems.append("country table markers missing")

    # 4. language-links block at the top
    top = "\n".join(text.split("\n")[:3])
    for code in ALL:
        fname = "README.md" if code == "en" else f"README.{code}.md"
        if code == lang:
            if f"]({fname})" in top:
                problems.append(f"own language {lang} should be bold, "
                                "not a link")
        elif f"]({fname})" not in top:
            problems.append(f"links block missing {fname}")

    # 5. support ask at start and end
    head, tail = text[:2000], text[-2000:]
    if "⭐" not in head:
        problems.append("no ⭐ support ask near the start")
    if "⭐" not in tail:
        problems.append("no ⭐ support ask near the end")
    if "github.com/VortexLabsHQ" not in head:
        problems.append("no VortexLabsHQ link near the start")

    # 6. structure parity (links line excluded: each language bolds itself)
    if len(headings(text)) != len(headings(en)):
        problems.append(f"heading count {len(headings(text))} != "
                        f"English {len(headings(en))}")
    body_en = "\n".join(en.split("\n")[3:])
    body_tx = "\n".join(text.split("\n")[3:])
    if link_targets(body_tx) != link_targets(body_en):
        problems.append("link targets differ from English")
    if code_blocks(text) != code_blocks(en):
        problems.append("fenced code blocks differ from English")

    # 7. no placeholder text
    for ph in PLACEHOLDERS:
        if ph in text:
            problems.append(f"placeholder text left in file: {ph!r}")

    # 8. script check (body only: strip code blocks + country table)
    body = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    body = body.replace(table_block(text), "") if START in body else body
    if lang in SCRIPT_RANGES:
        hit = any(any(lo <= ch <= hi for lo, hi in SCRIPT_RANGES[lang])
                  for ch in body)
        if not hit:
            problems.append("no characters in the target language's script")
    # Latin-script languages: must not be (near-)identical to English
    if lang not in SCRIPT_RANGES:
        en_body = re.sub(r"```.*?```", "", en, flags=re.DOTALL)
        same_lines = sum(
            1 for a, b in zip(body.splitlines(), en_body.splitlines())
            if a.strip() and a.strip() == b.strip())
        total = sum(1 for l in en_body.splitlines() if l.strip())
        if total and same_lines / total > 0.5:
            problems.append(f"looks untranslated ({same_lines}/{total} "
                            "lines identical to English)")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--langs", default="",
                        help="comma-separated codes (default: all 21)")
    args = parser.parse_args()
    langs = ([c.strip() for c in args.langs.split(",") if c.strip()]
             if args.langs else LANGS)
    en = (REPO / "README.md").read_text(encoding="utf-8")
    failed = 0
    for lang in langs:
        problems = check(lang, en)
        if problems:
            failed += 1
            print(f"FAIL README.{lang}.md:")
            for p in problems:
                print(f"   - {p}")
        else:
            print(f"PASS README.{lang}.md")
    print(f"\n{len(langs) - failed}/{len(langs)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
