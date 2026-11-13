#!/usr/bin/env python3
"""Fix intra-document anchors in README.md and README.<lang>.md.

Problem: translators localize the `#countries` anchor (e.g. German
`#länder`), which breaks the link from the install section to the
country table. The fix has two parts, both mechanical:

  1. Every README gets an explicit `<a id="countries"></a>` line right
     before the "Countries" heading (the heading immediately above the
     <!-- COUNTRY_TABLE_START --> marker), so `#countries` resolves no
     matter what the heading itself says in that language.
  2. Any `#...` link target that is not `#countries` is rewritten to
     `#countries` (it is the only intra-document anchor in the README).

Usage: python3 scripts/fix_readme_anchors.py [--check]
Idempotent; safe to run on every README in the repo.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ANCHOR = '<a id="countries"></a>'
TABLE_MARKER = "<!-- COUNTRY_TABLE_START -->"
ANCHOR_RE = re.compile(r"\]\(#([^)]+)\)")


def fix(text: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    # 1. rewrite stray intra-document anchors to #countries
    def _sub(m: "re.Match[str]") -> str:
        if m.group(1) == "countries":
            return m.group(0)
        notes.append(f"anchor #{m.group(1)} -> #countries")
        return "](#countries)"

    text = ANCHOR_RE.sub(_sub, text)
    # 2. insert the explicit anchor before the Countries heading
    if ANCHOR not in text:
        lines = text.split("\n")
        marker = next(i for i, l in enumerate(lines)
                      if TABLE_MARKER in l)
        heads = [i for i in range(marker) if lines[i].startswith("## ")]
        if heads:
            head = max(heads)
            lines[head:head] = [ANCHOR, ""]
        else:
            # Fallback (e.g. a translation that lost the heading): anchor
            # directly above the table marker.
            lines[marker:marker] = [ANCHOR, ""]
            notes.append("no Countries heading found; anchored above the "
                         "table marker instead")
        text = "\n".join(lines)
        notes.append("inserted <a id=\"countries\"></a> before Countries "
                     "heading")
    return text, notes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changed = 0
    for path in [REPO / "README.md", *sorted(REPO.glob("README.*.md"))]:
        text = path.read_text(encoding="utf-8")
        fixed, notes = fix(text)
        if fixed != text:
            changed += 1
            if args.check:
                print(f"WOULD FIX {path.name}: {'; '.join(notes)}")
            else:
                path.write_text(fixed, encoding="utf-8")
                print(f"fixed {path.name}: {'; '.join(notes)}")
    if args.check and changed:
        return 1
    print(f"{changed} file(s) changed" if not args.check else "all anchors OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
