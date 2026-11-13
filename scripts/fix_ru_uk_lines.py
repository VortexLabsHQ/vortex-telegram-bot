#!/usr/bin/env python3
"""One-off: re-translate the two count lines for ru + uk with correct
number agreement (mechanical 22->40 gave "40 языка"/"40 мови", which
is wrong; correct is "40 языков"/"40 мов").

RUNS ON THE SERVER ONLY. Reads the NVIDIA key from
/home/ubuntu/mindcraft/keys.json itself; never prints it.
Prints a JSON object {lang: [line1, line2]} to stdout.
"""
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, "/tmp")
from readme_translate import call_nemotron, load_key, system_prompt  # noqa: E402

LINES = [
    "- 🌍 **195 countries** and **40 languages** — country and language "
    "are separate settings",
    "Vortex supports **195 countries** and **40 languages**. The country "
    "sets the time zone, the currency prices are shown in, the city used "
    "for prayer times, and local content. The language only sets what the "
    "bot says — a group in Belgium can use the country Belgium and the "
    "language English, for example. Both can be changed later from "
    "`/admin`.",
]

PROMPTS = {
    "ru": "Russian",
    "uk": "Ukrainian",
}


def main() -> None:
    key = load_key()
    out = {}
    for lang, name in PROMPTS.items():
        system = system_prompt(name) + (
            "\nTranslate ONLY the two lines below. Keep the Markdown "
            "bold markers (**...**), the 🌍 emoji, the word \"Vortex\", "
            "country names (Belgium), and `/admin` unchanged. Use the "
            "grammatically correct noun form after the number 40 in your "
            "language. Reply with the two translated lines only, one per "
            "line, no extra text.")
        res = call_nemotron(key, system, "\n".join(LINES),
                            max_tokens=2000)
        lines = [l for l in res.split("\n") if l.strip()]
        assert len(lines) == 2, f"{lang}: expected 2 lines, got {lines!r}"
        out[lang] = lines
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
