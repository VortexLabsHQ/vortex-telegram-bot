"""Verify a translated locale file against bot/locale/en.json.

Checks (the supervision bar for Nemotron output):
  1. JSON parses.
  2. Key set is EXACTLY the English key set (no missing / extra keys).
  3. Value types match (str vs list) and list lengths match.
  4. Every {placeholder} in the English string is present in the
     translation, and no new placeholder appears.
  5. No empty strings.
  6. No placeholder text ("[translation]", "TODO", "Lorem", "XXX").
  7. The translation is actually in the target language: script checks
     for non-Latin languages, and a "still English" report for the rest.
  8. Strings identical to the English original are listed for review
     (a few are legitimate: pure emoji, URLs, the word "Vortex").

Usage:
  python3 scripts/verify_locales.py bot/locale/fa.json
  python3 scripts/verify_locales.py bot/locale/*.json
  python3 scripts/verify_locales.py --staging /tmp/locale-out/*.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EN_PATH = REPO / "bot" / "locale" / "en.json"

# Script ranges a translation must mostly use (for languages whose
# script is not Latin). Each entry: (unicode range regex, name).
SCRIPT_CHECKS = {
    "fa": (r"[\u0600-\u06FF]", "Arabic"),
    "ar": (r"[\u0600-\u06FF]", "Arabic"),
    "ur": (r"[\u0600-\u06FF]", "Arabic"),
    "zh": (r"[\u4E00-\u9FFF]", "CJK"),
    "ja": (r"[\u3040-\u30FF\u4E00-\u9FFF]", "Japanese kana/kanji"),
    "ko": (r"[\uAC00-\uD7A3]", "Hangul"),
    "ru": (r"[\u0400-\u04FF]", "Cyrillic"),
    "uk": (r"[\u0400-\u04FF]", "Cyrillic"),
    "th": (r"[\u0E00-\u0E7F]", "Thai"),
    "hi": (r"[\u0900-\u097F]", "Devanagari"),
}

# Values that are allowed to stay identical to the English original:
# pure emoji/punctuation, or strings that are only a URL/code.
IDENTICAL_OK = re.compile(r"^[^A-Za-z0-9\u0600-\u06FF\u4E00-\u9FFF\u3040-\u30FF\uAC00-\uD7A3\u0400-\u04FF\u0E00-\u0E7F\u0900-\u097F]*$")

BAD_MARKERS = ("[translation]", "TODO", "Lorem", "XXX", "???", "TRANSLATE")


def placeholders(text: str) -> set[str]:
    return set(re.findall(r"\{[a-zA-Z_][a-zA-Z0-9_]*\}", text))


def verify(path: Path, en: dict) -> tuple[list[str], list[str]]:
    """Returns (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{path}: JSON parse error: {exc}"], []
    if not isinstance(data, dict):
        return [f"{path}: top level is not a JSON object"], []

    en_keys = set(en)
    got_keys = set(data)
    if got_keys != en_keys:
        missing = sorted(en_keys - got_keys)
        extra = sorted(got_keys - en_keys)
        if missing:
            errors.append(f"missing keys ({len(missing)}): {missing[:8]}")
        if extra:
            errors.append(f"extra keys ({len(extra)}): {extra[:8]}")

    identical: list[str] = []
    no_script: list[str] = []
    script_re = None
    code = path.stem
    if code in SCRIPT_CHECKS:
        script_re = re.compile(SCRIPT_CHECKS[code][0])

    for key, en_val in en.items():
        if key not in data:
            continue
        tr_val = data[key]
        if type(en_val) is not type(tr_val):
            errors.append(f"{key}: type {type(en_val).__name__} -> {type(tr_val).__name__}")
            continue
        en_items = en_val if isinstance(en_val, list) else [en_val]
        tr_items = tr_val if isinstance(tr_val, list) else [tr_val]
        if len(en_items) != len(tr_items):
            errors.append(f"{key}: list length {len(en_items)} -> {len(tr_items)}")
            continue
        for i, (en_s, tr_s) in enumerate(zip(en_items, tr_items, strict=True)):
            where = f"{key}[{i}]" if isinstance(en_val, list) else key
            if not isinstance(tr_s, str) or not tr_s.strip():
                errors.append(f"{where}: empty translation")
                continue
            if placeholders(en_s) != placeholders(tr_s):
                errors.append(
                    f"{where}: placeholders {sorted(placeholders(en_s))} "
                    f"-> {sorted(placeholders(tr_s))}"
                )
            for marker in BAD_MARKERS:
                if marker in tr_s:
                    errors.append(f"{where}: placeholder text {marker!r}")
            if tr_s == en_s:
                if not IDENTICAL_OK.match(tr_s):
                    identical.append(where)
            elif script_re is not None:
                # A real translation should carry the target script in
                # most strings (URLs/names/emojis aside).
                if not script_re.search(tr_s) and re.search(r"[A-Za-z]", en_s):
                    no_script.append(where)

    if identical:
        warnings.append(
            f"identical to English ({len(identical)}): {identical[:10]}"
        )
    if no_script:
        warnings.append(
            f"no {SCRIPT_CHECKS[code][1]} script ({len(no_script)}): {no_script[:10]}"
        )
    return errors, warnings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()
    en = json.loads(EN_PATH.read_text(encoding="utf-8"))
    print(f"en.json: {len(en)} keys")
    total_errors = 0
    for f in args.files:
        path = Path(f)
        errors, warnings = verify(path, en)
        status = "OK " if not errors else "FAIL"
        print(f"[{status}] {path.name}: {len(errors)} errors, {len(warnings)} warnings")
        for e in errors:
            print(f"    ERR {e}")
            total_errors += 1
        for w in warnings:
            print(f"    WARN {w}")
    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
