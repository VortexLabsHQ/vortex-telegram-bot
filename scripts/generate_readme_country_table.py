#!/usr/bin/env python3
"""Generate the country table for README.md from bot/countries.py.

The README's country table is the installer's source of truth for users:
the installer asks them to paste the English country name exactly as
listed here. To keep the two in sync, this table is NEVER hand-typed —
it is generated from ``bot/countries.py`` (195 countries) and inserted
into README.md (and every README.<lang>.md) between the markers::

    <!-- COUNTRY_TABLE_START -->
    ... generated table ...
    <!-- COUNTRY_TABLE_END -->

Usage:
  python3 scripts/generate_readme_country_table.py            # print table
  python3 scripts/generate_readme_country_table.py --write    # rewrite the
      # table in README.md (and every README.<lang>.md) in place
  python3 scripts/generate_readme_country_table.py --check    # exit 1 if
      # any README's table differs from countries.py

The table columns are: Country | Time zone | Currency | Capital.
Country names are the English keys from countries.py, in file order.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from bot.countries import COUNTRIES  # noqa: E402

START = "<!-- COUNTRY_TABLE_START -->"
END = "<!-- COUNTRY_TABLE_END -->"

LANG_NAMES = {
    "en": "English",
    "fa": "Persian",
    "tr": "Turkish",
    "de": "German",
    "fr": "French",
    "es": "Spanish",
    "it": "Italian",
    "nl": "Dutch",
    "ru": "Russian",
    "uk": "Ukrainian",
    "pl": "Polish",
    "sv": "Swedish",
    "pt": "Portuguese",
    "ar": "Arabic",
    "hi": "Hindi",
    "ur": "Urdu",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "id": "Indonesian",
    "th": "Thai",
    "vi": "Vietnamese",
    "ms": "Malay",
    "bn": "Bengali",
    "pa": "Punjabi",
    "mr": "Marathi",
    "te": "Telugu",
    "ta": "Tamil",
    "gu": "Gujarati",
    "am": "Amharic",
    "sw": "Swahili",
    "ha": "Hausa",
    "fil": "Filipino",
    "ro": "Romanian",
    "hu": "Hungarian",
    "cs": "Czech",
    "el": "Greek",
    "he": "Hebrew",
    "da": "Danish",
    "no": "Norwegian",
}


def render_table() -> str:
    """Render the full Markdown country table from bot/countries.py."""
    lines = [
        "| Country | Time zone | Currency | Capital |",
        "| --- | --- | --- | --- |",
    ]
    for name, c in COUNTRIES.items():
        lines.append(f"| {name} | {c.timezone} | {c.currency} | {c.capital} |")
    return "\n".join(lines)


def replace_table(text: str, table: str) -> str:
    """Replace the marked table block in *text* with *table*."""
    start = text.index(START)
    end = text.index(END)  # keep the END marker itself
    return text[: start + len(START)] + "\n\n" + table + "\n\n" + text[end:]


def readme_files() -> list[Path]:
    files = [REPO / "README.md"]
    files += sorted(REPO.glob("README.*.md"))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true",
                       help="rewrite the table in README.md and README.*.md")
    group.add_argument("--check", action="store_true",
                       help="exit 1 if any README table is out of sync")
    args = parser.parse_args()

    table = render_table()
    if not args.write and not args.check:
        print(table)
        return 0

    bad: list[str] = []
    for path in readme_files():
        if not path.exists():
            bad.append(f"{path.name}: missing file")
            continue
        text = path.read_text(encoding="utf-8")
        if START not in text or END not in text:
            bad.append(f"{path.name}: table markers missing")
            continue
        if args.write:
            path.write_text(replace_table(text, table), encoding="utf-8")
            print(f"updated {path.name} ({len(COUNTRIES)} countries)")
        else:
            if replace_table(text, table) != text:
                bad.append(f"{path.name}: table out of sync with "
                           "bot/countries.py")

    if bad:
        for line in bad:
            print("FAIL:", line, file=sys.stderr)
        return 1
    if args.check:
        print(f"OK: {len(readme_files())} README(s), "
              f"{len(COUNTRIES)} countries each")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
