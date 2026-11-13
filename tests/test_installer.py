"""Tests for the interactive installer (install.sh) and its data
generator (scripts/generate_install_data.py).

Run: python tests/test_installer.py
Covers:
  - the generated country/language block in install.sh is in sync
    with bot/countries.py (generate_install_data.py --check) and
    matches it exactly (195 names + default languages, 40 UI langs)
  - bash -n syntax check (and shellcheck, when installed)
  - the shell country matching agrees with bot/countries.get_country
    (exact, case variants, whitespace variants, unknown -> no match)
  - suggestions: prefix matches first, then substring matches
  - lang_known / lang_display for the 40 UI languages
  - the systemd unit file the installer writes (ExecStart, User,
    WorkingDirectory, Restart=always) and the sudoers rule text
    (restart/stop/start, visudo -c passes)
  - the one-command install line is documented in the header

The full interactive flow is exercised by tests/test_installer_e2e.sh
(dry run against a local git repo + stub HTTP servers), which is not
part of the CI loop because it builds a real venv and pip-installs.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bot.countries import COUNTRIES, LANGUAGES, UI_LANGUAGES, get_country

REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_SH = REPO_ROOT / "install.sh"
GENERATOR = REPO_ROOT / "scripts" / "generate_install_data.py"

passed = failed = 0


def check(name, cond, extra=""):
    global passed, failed
    if cond:
        passed += 1
        print(f"  PASS {name}")
    else:
        failed += 1
        print(f"  FAIL {name} {extra}")


def bash_lib(code):
    """Run bash code with install.sh sourced in library mode."""
    script = (
        "export VORTEX_INSTALLER_LIB=1\n"
        f"source {INSTALL_SH}\n"
        + code
    )
    return subprocess.run(
        ["bash", "-c", script],
        capture_output=True, text=True, timeout=60,
    )


# ------------------------------------------------------------------- generator

r = subprocess.run(
    [sys.executable, str(GENERATOR), "--check"],
    capture_output=True, text=True, timeout=60,
)
check("generate_install_data.py --check is clean", r.returncode == 0, r.stdout + r.stderr)

text = INSTALL_SH.read_text(encoding="utf-8")
m = re.search(
    r"COUNTRY_DATA='(.*?)'\nLANG_DATA='(.*?)'",
    text, re.DOTALL,
)
check("install.sh contains the generated data block", m is not None)
if m:
    embedded_countries = {}
    for line in m.group(1).splitlines():
        name, lang = line.split("|")
        embedded_countries[name] = lang
    expected_countries = {c.name: c.default_language for c in COUNTRIES.values()}
    check("embedded countries == bot/countries.py (195)",
          embedded_countries == expected_countries,
          f"embedded={len(embedded_countries)} expected={len(expected_countries)}")
    embedded_langs = {}
    for line in m.group(2).splitlines():
        code, name = line.split("|")
        embedded_langs[code] = name
    expected_langs = {code: LANGUAGES[code] for code in UI_LANGUAGES}
    check("embedded UI languages == bot/countries.py (23)",
          embedded_langs == expected_langs)

# ------------------------------------------------------------------- syntax

r = subprocess.run(["bash", "-n", str(INSTALL_SH)],
                   capture_output=True, text=True, timeout=60)
check("bash -n install.sh", r.returncode == 0, r.stderr)

shellcheck = subprocess.run(["which", "shellcheck"],
                            capture_output=True, text=True)
if shellcheck.returncode == 0:
    r = subprocess.run(["shellcheck", str(INSTALL_SH)],
                       capture_output=True, text=True, timeout=120)
    check("shellcheck install.sh is clean", r.returncode == 0, r.stdout)
else:
    print("  SKIP shellcheck (not installed)")

# ------------------------------------------------------------------- country matching

CASES = [
    # (installer input, expected country name or None)
    ("Turkey", "Turkey"),
    ("turkey", "Turkey"),
    ("TURKEY", "Turkey"),
    ("  turkey  ", "Turkey"),
    ("United   States", "United States"),
    ("united states", "United States"),
    ("UNITED STATES", "United States"),
    ("Iran", "Iran"),
    ("  IRAN ", "Iran"),
    ("Côte d’Ivoire", "Côte d’Ivoire"),
    ("côte d’ivoire", "Côte d’Ivoire"),
    ("Belgium", "Belgium"),
    ("São Tomé & Príncipe", "São Tomé & Príncipe"),
    ("Atlantis", None),
    ("", None),
    ("Turke", None),
    ("United", None),
]
for raw, expected in CASES:
    py = get_country(raw)
    py_name = py.name if py else None
    check(f"python get_country({raw!r}) == {expected!r}",
          py_name == expected, repr(py_name))
    # Pass the case through an env var so quoting can never break it.
    env = {"VORTEX_CASE": raw, "PATH": "/usr/bin:/bin:/usr/local/bin"}
    r = subprocess.run(
        ["bash", "-c",
         "export VORTEX_INSTALLER_LIB=1\n"
         f"source {INSTALL_SH}\n"
         'if out="$(find_country "$VORTEX_CASE")"; then '
         'printf \'%s\' "${out%%|*}"; else printf \'NOMATCH\'; fi'],
        capture_output=True, text=True, timeout=60, env=env,
    )
    got = r.stdout if r.stdout != "NOMATCH" else None
    check(f"bash find_country({raw!r}) == {expected!r}",
          got == expected, f"got={got!r} stderr={r.stderr.strip()[:200]}")

# Suggestions: prefix matches first, then substring matches.
r = bash_lib('suggest_countries "unit"')
check('suggest "unit" lists the United* countries first',
      r.stdout.splitlines()[:3] == [
          "United Arab Emirates", "United Kingdom", "United States"],
      repr(r.stdout))
r = bash_lib('suggest_countries "turk"')
check('suggest "turk" finds Turkey + Turkmenistan',
      r.stdout.splitlines() == ["Turkey", "Turkmenistan"], repr(r.stdout))
r = bash_lib('suggest_countries "zzz-no-such"')
check('suggest unknown name prints nothing',
      r.stdout == "", repr(r.stdout))

# ------------------------------------------------------------------- languages

for code in UI_LANGUAGES:
    r = bash_lib(f'lang_known "{code}"')
    check(f"lang_known {code}", r.returncode == 0)
    r = bash_lib(f'lang_display "{code}"')
    check(f"lang_display {code} == {LANGUAGES[code]!r}",
          r.stdout == LANGUAGES[code], repr(r.stdout))
r = bash_lib('lang_known "xx"')
check("lang_known xx is false", r.returncode != 0)
r = bash_lib('lang_known "sq"')
check("lang_known sq is false (not a UI language)",
      r.returncode != 0)

# ------------------------------------------------------------------- unit file + sudoers

with tempfile.TemporaryDirectory() as tmp:
    unit_path = Path(tmp) / "vortex-bot.service"
    r = bash_lib(
        'INSTALL_DIR=/home/tester/vortex-bot\n'
        'INSTALL_USER=tester\n'
        f'_write_unit_file "{unit_path}" n\n'
    )
    check("_write_unit_file runs", r.returncode == 0, r.stderr)
    unit = unit_path.read_text(encoding="utf-8")
    check("unit WorkingDirectory",
          "WorkingDirectory=/home/tester/vortex-bot" in unit, unit)
    check("unit ExecStart runs python -m bot.main from the venv",
          "ExecStart=/home/tester/vortex-bot/.venv/bin/python -m bot.main" in unit, unit)
    check("unit EnvironmentFile points at .env",
          "EnvironmentFile=/home/tester/vortex-bot/.env" in unit, unit)
    check("unit Restart=always", "Restart=always" in unit, unit)
    check("unit User= for system services", "User=tester" in unit, unit)
    check("unit WantedBy=multi-user.target",
          "WantedBy=multi-user.target" in unit, unit)

    r = bash_lib(
        'INSTALL_USER=tester\n'
        '_sudoers_text /usr/bin/systemctl\n'
    )
    sudoers = r.stdout
    expected_rule = (
        "tester ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart vortex-bot, "
        "/usr/bin/systemctl stop vortex-bot, "
        "/usr/bin/systemctl start vortex-bot"
    )
    check("sudoers rule text (restart/stop/start)",
          expected_rule in sudoers, repr(sudoers))
    sudoers_file = Path(tmp) / "vortex-bot.sudoers"
    sudoers_file.write_text(sudoers, encoding="utf-8")
    visudo = subprocess.run(["which", "visudo"], capture_output=True, text=True)
    if visudo.returncode == 0:
        r = subprocess.run(["visudo", "-c", "-f", str(sudoers_file)],
                           capture_output=True, text=True, timeout=60)
        check("visudo -c passes on the generated sudoers rule",
              r.returncode == 0, r.stdout + r.stderr)
    else:
        print("  SKIP visudo check (not installed)")

# ------------------------------------------------------------------- .env merge

with tempfile.TemporaryDirectory() as tmp:
    env_file = Path(tmp) / ".env"
    env_file.write_text(
        "BOT_TOKEN=old-token-123\nBOT_NAME=OldName\n", encoding="utf-8")
    lib = (
        "export VORTEX_INSTALLER_LIB=1\n"
        f"source {INSTALL_SH}\n"
        f"INSTALL_DIR={tmp}\n"
        "BOT_TOKEN='123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'\n"
        "BOSS_ID=123456789\n"
        "BOT_NAME='New Name'\n"
        "COUNTRY_NAME='Turkey'\n"
        "BOT_LANGUAGE=tr\n"
        "LLM_BASE=https://example.com/v1\n"
        "LLM_KEY=sk-test-key-1234567890\n"
        "LLM_MODEL=some-model\n"
        "write_env\n"
    )
    # Answer "n": keep the existing .env, fill only missing values.
    r = subprocess.run(["bash", "-c", lib], input="n\n",
                       capture_output=True, text=True, timeout=60)
    check("write_env merge runs", r.returncode == 0, r.stderr)
    merged = env_file.read_text(encoding="utf-8")
    check("merge keeps existing BOT_TOKEN",
          "BOT_TOKEN=old-token-123" in merged, merged)
    check("merge keeps existing BOT_NAME",
          "BOT_NAME=OldName" in merged, merged)
    check("merge fills missing BOSS_ID",
          "BOSS_ID=123456789" in merged, merged)
    check("merge fills missing LLM_PROVIDERS",
          "LLM_PROVIDERS=" in merged and "some-model" in merged, merged)
    # Answer "y": overwrite with the new answers.
    r = subprocess.run(["bash", "-c", lib], input="y\n",
                       capture_output=True, text=True, timeout=60)
    check("write_env overwrite runs", r.returncode == 0, r.stderr)
    fresh = env_file.read_text(encoding="utf-8")
    check("overwrite replaces BOT_TOKEN",
          "BOT_TOKEN=123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" in fresh, fresh)
    check("overwrite replaces BOT_NAME (quoted, has a space)",
          'BOT_NAME="New Name"' in fresh, fresh)
    check("overwrite drops the old values",
          "old-token-123" not in fresh and "OldName" not in fresh, fresh)

# ------------------------------------------------------------------- header docs

check("header documents the one-command install line",
      "curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash" in text)
check("header documents VORTEX_DRY_RUN",
      "VORTEX_DRY_RUN=1" in text)
check("header documents VORTEX_TEST_MODE as test-only",
      "VORTEX_TEST_MODE=1" in text and "TEST ONLY" in text)

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
