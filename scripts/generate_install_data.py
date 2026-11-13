#!/usr/bin/env python3
"""Generate the country/language data embedded in install.sh.

install.sh is piped straight from GitHub (``curl ... | bash``), so at
install time it has no repo files to read: the 195 country names and
the 40 bot UI languages must be EMBEDDED in the script itself. This
script derives that block from bot/countries.py (the single source of
truth) and rewrites it in place, so the two can never drift apart.

Usage:
    python3 scripts/generate_install_data.py          # rewrite install.sh
    python3 scripts/generate_install_data.py --check  # exit 1 if stale

The generated block lives between the markers
    # BEGIN GENERATED INSTALL DATA
    # END GENERATED INSTALL DATA
in install.sh, in this format (one entry per line):

    COUNTRY_DATA='Iran|fa
    Turkey|tr
    ...'
    LANG_DATA='en|English
    fa|Persian (Farsi)
    ...'

Country lines are ``English name|default language code`` (sorted by
name); language lines are ``code|English display name`` (in
UI_LANGUAGES order). Names are stored verbatim — install.sh matches
them case/whitespace-insensitively, the same rules as
bot/countries.py::get_country.

Safety: the block is embedded in a single-quoted bash string, so a
name containing an ASCII single quote or a ``|`` would break the
script — this generator refuses to emit such data.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_SH = REPO_ROOT / "install.sh"

BEGIN_MARKER = "# BEGIN GENERATED INSTALL DATA"
END_MARKER = "# END GENERATED INSTALL DATA"


def build_block() -> str:
    """Render the generated block from bot/countries.py."""
    sys.path.insert(0, str(REPO_ROOT))
    from bot.countries import COUNTRIES, LANGUAGES, UI_LANGUAGES

    if len(COUNTRIES) != 195:
        raise SystemExit(f"expected 195 countries, got {len(COUNTRIES)}")
    if len(UI_LANGUAGES) != 40:
        raise SystemExit(f"expected 40 UI languages, got {len(UI_LANGUAGES)}")
    for code in UI_LANGUAGES:
        if code not in LANGUAGES:
            raise SystemExit(f"UI language {code!r} has no display name")

    country_lines = []
    for name in sorted(COUNTRIES):
        country = COUNTRIES[name]
        for bad in ("'", "|", "\n"):
            if bad in name:
                raise SystemExit(f"country name {name!r} contains {bad!r}")
        country_lines.append(f"{name}|{country.default_language}")
    lang_lines = []
    for code in UI_LANGUAGES:
        display = LANGUAGES[code]
        for bad in ("'", "|", "\n"):
            if bad in display:
                raise SystemExit(f"language name {display!r} contains {bad!r}")
        lang_lines.append(f"{code}|{display}")

    lines = [
        BEGIN_MARKER + " — do not edit by hand.",
        "# Regenerate with: python3 scripts/generate_install_data.py",
        "# Source: bot/countries.py (195 countries, 40 UI languages).",
        # "Côte d'Ivoire" carries a real U+2019 apostrophe; tell
        # shellcheck it is intentional, scoped to this block only.
        "# shellcheck disable=SC1112",
        "COUNTRY_DATA='" + "\n".join(country_lines) + "'",
        "LANG_DATA='" + "\n".join(lang_lines) + "'",
        END_MARKER,
    ]
    return "\n".join(lines) + "\n"


def replace_block(text: str, block: str) -> str:
    """Swap the generated block in install.sh's text for `block`."""
    start = text.find(BEGIN_MARKER)
    end = text.find(END_MARKER)
    if start < 0 or end < 0 or end < start:
        raise SystemExit(
            "install.sh is missing the GENERATED INSTALL DATA markers; "
            "refusing to guess where the block goes"
        )
    end = text.find("\n", end) + 1
    return text[:start] + block + text[end:]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="exit 1 (without writing) if install.sh is out of sync",
    )
    args = ap.parse_args()

    block = build_block()
    current = INSTALL_SH.read_text(encoding="utf-8")
    updated = replace_block(current, block)
    if updated == current:
        print("install.sh: embedded country/language data is up to date.")
        return 0
    if args.check:
        print(
            "install.sh: embedded country/language data is STALE.\n"
            "Run: python3 scripts/generate_install_data.py"
        )
        return 1
    INSTALL_SH.write_text(updated, encoding="utf-8")
    print("install.sh: embedded country/language data regenerated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
