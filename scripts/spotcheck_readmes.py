#!/usr/bin/env python3
"""Read-only spot check of translator-produced README files on the server.
Usage: python3 /tmp/spotcheck_readmes.py README.gu.md README.ro.md
Checks: fence balance, install command byte-identical, country table
markers + Iran row present (English names), star count, links-block size.
Prints PASS/FAIL per file. Never modifies anything.
"""
import sys

INSTALL = ("curl -sSL https://raw.githubusercontent.com/"
           "VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash")


def check(path):
    problems = []
    t = open(path, encoding="utf-8").read()
    if t.count("```") % 2:
        problems.append("unbalanced fences")
    if INSTALL not in t:
        problems.append("install command missing/changed")
    if "<!-- COUNTRY_TABLE_START -->" not in t:
        problems.append("country table start marker missing")
    if "<!-- COUNTRY_TABLE_END -->" not in t:
        problems.append("country table end marker missing")
    if "| Iran | Asia/Tehran | IRR | Tehran |" not in t:
        problems.append("Iran row missing or translated")
    if t.count("⭐") < 2:
        problems.append(f"only {t.count('⭐')} star(s)")
    lines = t.split("\n")
    if len(lines) < 3 or lines[2].count("README.") < 39:
        problems.append("links block has <39 README links")
    return problems


for path in sys.argv[1:]:
    problems = check(path)
    print(("PASS " if not problems else "FAIL ") + path +
          ("" if not problems else ": " + "; ".join(problems)))
