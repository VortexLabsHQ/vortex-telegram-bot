# Contributing to Vortex

Thanks for wanting to help make Vortex better! This guide is short on
purpose — if anything here is unclear, just open an issue and ask.

## Setting up a dev environment

```bash
git clone https://github.com/VortexLabsHQ/vortex-telegram-bot.git
cd vortex-telegram-bot

python3.11 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install ruff

cp .env.example .env   # then fill in your own BOT_TOKEN and LLM key(s)
```

You need a Telegram bot token (from [@BotFather](https://t.me/BotFather))
and at least one OpenAI-compatible LLM API key. Everything else in
`.env.example` has a sane default. **Never commit your real `.env`.**

To run the bot locally:

```bash
python -m bot.main
```

## Running the tests

The test suites are plain Python scripts (not pytest). Run each one
from the repo root:

```bash
python tests/test_admin.py
python tests/test_admin_keys.py
python tests/test_admin_select.py
python tests/test_admin_power.py
python tests/test_admin_image.py
python tests/test_fixes.py
python tests/test_installer.py
python tests/test_locale.py
python tests/test_updater.py
```

All nine must pass before you open a PR. CI runs the same nine suites on
Python 3.11 and 3.12. (`tests/test_installer_e2e.sh` is an end-to-end
installer run — it needs a throwaway VM/container, so it is not part of
the normal suite run.)

## Code style

We use [ruff](https://docs.astral.sh/ruff/) with the config in
`pyproject.toml` (line length 100, Python 3.11 target). Before
committing, run:

```bash
ruff check bot/
ruff format --check bot/   # or: ruff format bot/
```

Keep changes focused: one feature or fix per PR, with a short
description of what changed and why.

## Submitting a PR

1. Fork the repo and create a branch from `main`
   (`git checkout -b fix/short-description`).
2. Make your change, add or update tests where it makes sense.
3. Run `ruff check bot/` and all nine test suites.
4. Open a pull request against `main` and describe what you changed
   and how you tested it.

Two generated files to know about:

- `install.sh` embeds generated data (the 195-country table and the
  bot UI language list). Never hand-edit that block — regenerate it with
  `python3 scripts/generate_install_data.py` and check the result with
  `python tests/test_installer.py`.
- The country table in `README.md` (and every `README.<lang>.md`) is
  generated from `bot/countries.py`. Regenerate it with
  `python3 scripts/generate_readme_country_table.py --write` and verify
  with `--check` — never hand-edit country names.

Be kind in reviews — most contributors are here to learn. If a PR
needs changes, say what and why, and offer to help.
