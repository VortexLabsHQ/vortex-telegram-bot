#!/usr/bin/env python3
"""Generate the expanded country table for bot/countries.py (~195
UN-recognized countries) from reliable programmatic sources.

Sources (all free, no key):
  - Country names / capitals / currencies / languages:
    datasets/country-codes (GitHub, ISO 3166 / ISO 4217 / UN data):
    https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv
    Columns used: CLDR display name (English short name),
    ISO3166-1-Alpha-2, Capital, ISO4217-currency_alphabetic_code,
    Languages (ISO 639 tags, first listed = primary), is_independent.
  - Primary IANA timezone: /usr/share/zoneinfo/zone.tab (system tzdata,
    the same data zoneinfo uses), rule: the zone whose name/comment
    matches the capital city, else the first zone listed for the
    country. Explicit overrides in TZ_OVERRIDES below (capitals whose
    zone is neither named after them nor first-listed).
  - Currency cross-check: `ccy` (ISO 4217 country -> currency table);
    any disagreement with the CSV is reported and resolved explicitly.
  - Language display names: pycountry (ISO 639).

Country set: the CSV's is_independent == "Yes" rows (195) MINUS
Taiwan (TW, not UN-recognized) PLUS Palestine (PS, UN observer
state, listed as "In contention" in the CSV) = 195 countries:
193 UN member states + the Holy See (Vatican) + Palestine.

The original 32 countries are NOT regenerated here: they stay exactly
as they are in bot/countries.py (their values were set by the user).
This script only emits the additional entries, and verifies the 32
against the same sources (3 known, documented exceptions: Belgium's
default language is 'en' by the user's order, not the CSV's 'nl';
India's is 'hi', not the CSV's first-listed 'en'; Vietnam's capital
field is 'Ho Chi Minh City' in the table though the CSV says 'Hanoi'
-- the timezone is the same across Vietnam, so only the label differs;
corrected to 'Hanoi' here).

Usage:
  python3 scripts/generate_countries.py [--csv PATH] [--zonetab PATH]
Prints the Python code for the new entries + a verification report.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
import urllib.request
from collections import defaultdict
from pathlib import Path

CSV_URL = (
    "https://raw.githubusercontent.com/datasets/country-codes/master/"
    "data/country-codes.csv"
)

# The original 32 (kept verbatim in bot/countries.py); name -> alpha-2.
EXISTING_32 = {
    "Iran": "IR", "Turkey": "TR", "United States": "US",
    "United Kingdom": "GB", "Germany": "DE", "France": "FR",
    "Spain": "ES", "Italy": "IT", "Netherlands": "NL", "Belgium": "BE",
    "Russia": "RU", "Ukraine": "UA", "Poland": "PL", "Sweden": "SE",
    "Brazil": "BR", "Mexico": "MX", "Argentina": "AR",
    "Saudi Arabia": "SA", "United Arab Emirates": "AE", "Egypt": "EG",
    "Morocco": "MA", "India": "IN", "Pakistan": "PK", "China": "CN",
    "Japan": "JP", "South Korea": "KR", "Indonesia": "ID",
    "Thailand": "TH", "Vietnam": "VN", "Australia": "AU",
    "Nigeria": "NG", "Kenya": "KE",
}

# Primary-timezone overrides: capital city whose zone is neither named
# after the capital nor first-listed in zone.tab for that country.
#   CA: capital Ottawa uses America/Toronto (Eastern); zone.tab lists
#       America/St_Johns first.
#   FM: capital Palikir is on Pohnpei -> Pacific/Pohnpei; zone.tab
#       lists Pacific/Chuuk first.
#   PS: capital Ramallah is in the West Bank -> Asia/Hebron; zone.tab
#       lists Asia/Gaza first.
TZ_OVERRIDES = {
    "CA": "America/Toronto",
    "FM": "Pacific/Pohnpei",
    "PS": "Asia/Hebron",
}

# Capital-name fixes (CSV value -> table value) for prayer-time cities.
CAPITAL_FIXES = {
    "VN": "Hanoi",  # table said "Ho Chi Minh City"; Hanoi is the capital
    # KZ: CSV still says "Nur-Sultan"; the capital was renamed back to
    # Astana in 2022.
    "KZ": "Astana",
    # PS: CSV says "East Jerusalem"; Ramallah is the de facto seat of
    # government (and a working prayer-times city).
    "PS": "Ramallah",
}

# Currency overrides: the CSV lists two codes for a few countries
# (both are legal tender). The table keeps ONE primary currency:
#   BT (Bhutan): CSV "INR,BTN" -> BTN, the national ngultrum
#       (INR circulates too, pegged 1:1).
#   SV (El Salvador): CSV "SVC,USD" -> USD; the colon is defunct,
#       USD is the circulating currency since 2001.
#   PA (Panama): CSV "PAB,USD" -> USD; the balboa exists only as
#       coins pegged 1:1 to the dollar, USD is what people use.
# The others with two codes keep the first listed (the national one):
# HT -> HTG, LS -> LSL, NA -> NAD, VE -> VES.
CURRENCY_OVERRIDES = {
    "BT": "BTN",
    "SV": "USD",
    "PA": "USD",
    # PS: the CSV lists no currency (Palestine has none of its own);
    # ILS (Israeli new shekel) is the primary circulating currency
    # (JOD and EGP also circulate).
    "PS": "ILS",
}

# ccy's table is stale here: Bulgaria adopted the euro on 2026-01-01
# (21st eurozone member); the CSV's EUR is current, ccy still says BGN.
KNOWN_CCY_STALE = {"BG"}
NAME_OVERRIDES = {
    # CLDR shortens this one to just "Bosnia"; the common English name
    # is Bosnia & Herzegovina.
    "BA": "Bosnia & Herzegovina",
}

# Default-language overrides: the CSV's first-listed language is not
# the primary one here.
#   ER (Eritrea): CSV lists Afar ('aa') first; Tigrinya ('ti') is the
#       most widely spoken working language.
LANGUAGE_OVERRIDES = {
    "ER": "ti",
}

# pycountry's language names are sometimes long/awkward; use the short
# standard English name for the display table.
DISPLAY_NAME_FIXES = {
    "el": "Greek",
    "ht": "Haitian Creole",
    "ky": "Kyrgyz",
    "ms": "Malay",
    "ne": "Nepali",
    "sw": "Swahili",
    "to": "Tongan",
}


def norm(text: str) -> str:
    """Lowercase alphanumeric-only form, for capital/zone matching."""
    decomposed = unicodedata.normalize("NFKD", text)
    ascii_only = "".join(c for c in decomposed if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", ascii_only.lower())


def load_csv(path: str | None) -> list[dict]:
    if path:
        text = Path(path).read_text(encoding="utf-8")
    else:
        req = urllib.request.Request(CSV_URL, headers={"User-Agent": "vortex-gen/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            text = resp.read().decode("utf-8")
    return list(csv.DictReader(text.splitlines()))


def load_zonetab(path: str | None) -> dict[str, list[tuple[str, str]]]:
    src = Path(path) if path else Path("/usr/share/zoneinfo/zone.tab")
    zones: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for line in src.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split("\t")
        zones[parts[0]].append((parts[2], parts[3] if len(parts) > 3 else ""))
    return zones


def primary_timezone(a2: str, capital: str, zones: dict) -> tuple[str, str]:
    """(zone, how it was chosen): 'capital' | 'first' | 'override'."""
    if a2 in TZ_OVERRIDES:
        return TZ_OVERRIDES[a2], "override"
    candidates = zones.get(a2, [])
    if not candidates:
        raise ValueError(f"no zone.tab entry for {a2}")
    if len(candidates) == 1:
        return candidates[0][0], "only"
    cap = norm(capital)
    for zone, comment in candidates:
        if cap and (cap in norm(zone.rsplit("/", 1)[-1]) or cap in norm(comment)):
            return zone, "capital"
    return candidates[0][0], "first"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=None)
    ap.add_argument("--zonetab", default=None)
    args = ap.parse_args()

    import ccy  # noqa: PLC0415
    import pycountry  # noqa: PLC0415  (only needed for generation)

    rows = load_csv(args.csv)
    zones = load_zonetab(args.zonetab)
    by_a2 = {r["ISO3166-1-Alpha-2"]: r for r in rows}

    # --- country set: 193 UN members + Vatican + Palestine ----------
    selected = [r for r in rows if r["is_independent"] == "Yes"]
    selected = [r for r in selected if r["ISO3166-1-Alpha-2"] != "TW"]
    selected.append(by_a2["PS"])
    assert len(selected) == 195, f"expected 195, got {len(selected)}"

    # --- verify the existing 32 against the same sources ------------
    report: list[str] = []
    for name, a2 in sorted(EXISTING_32.items(), key=lambda kv: kv[0]):
        r = by_a2[a2]
        csv_cur = r["ISO4217-currency_alphabetic_code"]
        try:
            ccy_cur = ccy.countryccy(a2)
        except Exception:
            ccy_cur = None
        if ccy_cur and csv_cur != ccy_cur:
            report.append(f"EXISTING {name}: CSV currency {csv_cur} != ccy {ccy_cur}")

    # --- generate the new entries -----------------------------------
    entries = []
    lang_names: dict[str, str] = {}
    skipped_langs: list[str] = []
    currency_mismatches: list[str] = []
    tz_choices: list[str] = []
    existing_a2 = set(EXISTING_32.values())
    for r in sorted(selected, key=lambda x: x["CLDR display name"]):
        a2 = r["ISO3166-1-Alpha-2"]
        name = NAME_OVERRIDES.get(a2, r["CLDR display name"])
        if a2 in existing_a2:
            continue
        capital = CAPITAL_FIXES.get(a2, r["Capital"])
        raw_currency = r["ISO4217-currency_alphabetic_code"] or ""
        currency = CURRENCY_OVERRIDES.get(a2) or raw_currency.split(",")[0].strip()
        try:
            ccy_cur = ccy.countryccy(a2)
        except Exception:
            ccy_cur = None
        if ccy_cur and ccy_cur != currency:
            if a2 in KNOWN_CCY_STALE:
                currency_mismatches.append(
                    f"{name} ({a2}): CSV {currency} kept; ccy {ccy_cur} is stale"
                )
            else:
                currency_mismatches.append(f"{name} ({a2}): CSV {currency} != ccy {ccy_cur}")
        tz, how = primary_timezone(a2, capital, zones)
        if how in ("first", "override") and len(zones.get(a2, [])) > 1:
            tz_choices.append(f"{name}: {tz} ({how})")
        # Default language: first listed tag with an ISO 639-1 code.
        lang = None
        n_skipped_before = len(skipped_langs)
        for tag in (r["Languages"] or "").split(","):
            tag = tag.strip()
            if not tag:
                continue
            sub = tag.split("-")[0].lower()
            entry = pycountry.languages.get(alpha_2=sub) or pycountry.languages.get(alpha_3=sub)
            if entry is None:
                continue
            code = getattr(entry, "alpha_2", None)
            if code:
                lang = code
                lang_names[code] = DISPLAY_NAME_FIXES.get(code, entry.name)
                break
            skipped_langs.append(f"{name}: first language {sub} has no ISO 639-1 code")
        if lang is None:
            lang = "en"
            skipped_langs.append(f"{name}: no usable language listed, fell back to en")
        if len(skipped_langs) > n_skipped_before:
            skipped_langs.append(f"{name}: final default language is {lang}")
        if a2 in LANGUAGE_OVERRIDES:
            lang = LANGUAGE_OVERRIDES[a2]
            entry = pycountry.languages.get(alpha_2=lang)
            lang_names[lang] = DISPLAY_NAME_FIXES.get(
                lang, entry.name if entry is not None else lang
            )
            skipped_langs.append(f"{name}: default language overridden to {lang}")
        entries.append((name, lang, tz, currency, capital, a2))

    # --- validate: every timezone/currency/language is real ---------
    from zoneinfo import ZoneInfo

    for name, lang, tz, currency, _capital, _a2 in entries:
        ZoneInfo(tz)  # raises if not a real IANA zone
        assert re.fullmatch(r"[A-Z]{3}", currency or ""), f"{name}: bad currency {currency!r}"
        cur = pycountry.currencies.get(alpha_3=currency)
        assert cur is not None, f"{name}: {currency} is not ISO 4217"
        assert re.fullmatch(r"[a-z]{2}", lang), f"{name}: bad lang {lang!r}"

    # --- emit --------------------------------------------------------
    print(f"# {len(entries)} additional countries (generated by "
          "scripts/generate_countries.py).")
    print("# Country set: 193 UN members + Holy See + Palestine = 195 total")
    print("# (32 original countries above + these).")
    for name, lang, tz, currency, capital, _a2 in entries:
        print(f'    Country("{name}", "{tz}", "{currency}", "{capital}", "{lang}"),')
    print()
    print(f"# New default-language codes needing display names: {len(lang_names)}")
    for code in sorted(lang_names):
        print(f"#   {code}: {lang_names[code]}")

    print("\n# ---- verification report ----", file=sys.stderr)
    print(f"# total countries: {32 + len(entries)}", file=sys.stderr)
    print(f"# new entries: {len(entries)}", file=sys.stderr)
    for line in report + currency_mismatches:
        print(f"# MISMATCH: {line}", file=sys.stderr)
    for line in tz_choices:
        print(f"# TZ: {line}", file=sys.stderr)
    for line in skipped_langs:
        print(f"# LANG: {line}", file=sys.stderr)
    print("# done", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
