#!/usr/bin/env bash
# End-to-end dry-run test for install.sh.
#
# NOT part of the CI loop (tests/test_*.py): it builds real venvs and
# pip-installs requirements (~1 min per scenario, needs network).
# Run it by hand after changing install.sh:
#   bash tests/test_installer_e2e.sh
#
# What it does:
#   - Builds a LOCAL git repo from the working tree (the real repo is
#     not pushed yet, so raw.githubusercontent.com cannot serve it).
#   - Runs a stub HTTP server on 127.0.0.1:18080 answering both
#     /bot<token>/getMe and /models, so the live checks run for real
#     without touching Telegram or any LLM provider.
#   - Runs install.sh four times (VORTEX_DRY_RUN=1: no systemd
#     units, sudoers files or docker calls touch this machine):
#       A: invalid country -> suggestion -> valid country ("  turkey "),
#          default language (Enter), bad token -> good token (verified
#          by the stub getMe), bad boss id -> good one, custom bot
#          name with surrounding spaces, CUSTOM provider against the
#          stub /models server, pick model #2, SearXNG declined.
#       B: getMe unreachable (dead port) -> "continue anyway" branch,
#          /models unreachable -> manual model id entry.
#       C: like A but SearXNG accepted, with a fake `docker` shim in
#          PATH (logs its args, exits 0) — proves the secret is
#          generated, the port override file is written, and the
#          compose up is invoked; the health check then warns (no
#          real SearXNG) and the install continues.
#       D: preset provider + Anthropic warning: pick Anthropic
#          (warns: not OpenAI-compatible) -> decline -> back to the
#          menu -> pick OpenAI (preset) -> override its base URL with
#          the stub server -> pick model #1. Country Belgium (default
#          language en), default bot name.
#   - Asserts .env contents (loaded back through python-dotenv, so
#     quoting is verified for real), the venv + installed packages,
#     the dry-run unit file and sudoers file (visudo -c), and key
#     lines of the installer's output.
#
# Nothing in this script touches the live bot, systemd, /etc, or any
# real Telegram/LLM account. The only real network use is pip
# installing requirements from PyPI.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# Workdir: under $HOME by default (NOT /tmp: /tmp is often a small
# tmpfs, and four full installs with venvs need ~500 MB). Override
# with VORTEX_E2E_WORK. Wiped at the start of every run.
WORK="${VORTEX_E2E_WORK:-$HOME/vortex-e2e-test}"
STUB_PORT=18080
rm -rf "$WORK"
mkdir -p "$WORK/repo-src" "$WORK/logs"

# ---------------------------------------------------------------- stub server
cat > "$WORK/stub_server.py" <<'PYEOF'
"""Stub for api.telegram.org getMe + any provider's /models."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/getMe"):
            body = {"ok": True, "result": {"id": 123,
                                           "username": "vortex_test_bot",
                                           "first_name": "Vortex Test"}}
        elif self.path.endswith("/models"):
            body = {"data": [{"id": "stub-model-a"},
                             {"id": "stub-model-b"},
                             {"id": "stub-model-c"}]}
        else:
            self.send_response(404)
            self.end_headers()
            return
        data = json.dumps(body).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


ThreadingHTTPServer(("127.0.0.1", 18080), H).serve_forever()
PYEOF
python3 "$WORK/stub_server.py" &
STUB_PID=$!
trap 'kill $STUB_PID 2>/dev/null || true' EXIT
sleep 1
curl -sS -m 5 "http://127.0.0.1:$STUB_PORT/models" >/dev/null \
    || { echo "stub server did not start"; exit 1; }

# ---------------------------------------------------------------- local repo
cp -r "$REPO_ROOT/." "$WORK/repo-src/"
rm -rf "$WORK/repo-src/.git"
git -C "$WORK/repo-src" init -q -b main
git -C "$WORK/repo-src" config user.email "test@example.com"
git -C "$WORK/repo-src" config user.name "e2e"
git -C "$WORK/repo-src" add -A
git -C "$WORK/repo-src" commit -qm "e2e snapshot"

TOKEN="123456789:$(python3 -c "print('A' * 35)")"
KEY="sk-test-key-1234567890"

pass=0; fail=0
check() { # check NAME CONDITION...
    local name="$1"; shift
    if "$@"; then pass=$((pass + 1)); echo "  PASS $name";
    else fail=$((fail + 1)); echo "  FAIL $name"; fi
}
check_grep() { # check_grep NAME FILE PATTERN
    grep -qF "$3" "$2" && { pass=$((pass + 1)); echo "  PASS $1"; } \
        || { fail=$((fail + 1)); echo "  FAIL $1 (missing: $3)"; }
}

run_install() { # run_install SCENARIO ANSWERS_FILE [extra env...]
    local scenario="$1" answers="$2"; shift 2
    local rc=0
    echo "== scenario $scenario =="
    # setsid: no controlling terminal, so the installer reads answers
    # from stdin (exactly like a piped curl|bash run would read them
    # from /dev/tty — here there is no tty, so stdin is the fallback).
    setsid env \
        VORTEX_REPO_URL="$WORK/repo-src" \
        VORTEX_DRY_RUN=1 \
        VORTEX_DRY_RUN_DIR="$WORK/dry-run-$scenario" \
        VORTEX_INSTALL_USER=tester \
        "$@" \
        bash "$REPO_ROOT/install.sh" < "$answers" \
        > "$WORK/logs/$scenario.log" 2>&1 || rc=$?
    echo "   exit=$rc log=$WORK/logs/$scenario.log"
    # Record the exit code for the assertions below.
    printf '%s' "$rc" > "$WORK/logs/$scenario.rc"
}

# ---------------------------------------------------------------- scenario A
cat > "$WORK/answers-a.txt" <<EOF
Turke
  turkey
<blank>
badtoken
$TOKEN
abc
123456789
  Vortex Test
11
http://127.0.0.1:$STUB_PORT
$KEY
2
$WORK/install-a
n
EOF
# The language step takes Enter (default). Replace the <blank> marker
# with a truly empty line (heredoc cannot express it otherwise).
sed -i 's/^<blank>$//' "$WORK/answers-a.txt"
run_install a "$WORK/answers-a.txt" \
    VORTEX_TELEGRAM_API_BASE="http://127.0.0.1:$STUB_PORT"

# ---------------------------------------------------------------- scenario B
cat > "$WORK/answers-b.txt" <<EOF
Iran

$TOKEN
y
123456789

11
http://127.0.0.1:9
$KEY
gpt-4o-mini
$WORK/install-b
n
EOF
run_install b "$WORK/answers-b.txt" \
    VORTEX_TELEGRAM_API_BASE="http://127.0.0.1:9"

# ---------------------------------------------------------------- scenario C
mkdir -p "$WORK/fakebin"
cat > "$WORK/fakebin/docker" <<'EOF'
#!/usr/bin/env bash
# Fake docker: log the call, succeed. Used to test the SearXNG path
# without Docker installed.
echo "docker $*" >> "$VORTEX_E2E_DOCKER_LOG"
if [[ "$1" == "compose" && "$2" == "version" ]]; then exit 0; fi
exit 0
EOF
chmod +x "$WORK/fakebin/docker"
cp "$WORK/answers-a.txt" "$WORK/answers-c.txt"
sed -i "s|$WORK/install-a|$WORK/install-c|; \$s/^n\$/y/" "$WORK/answers-c.txt"
run_install c "$WORK/answers-c.txt" \
    VORTEX_TELEGRAM_API_BASE="http://127.0.0.1:$STUB_PORT" \
    VORTEX_E2E_DOCKER_LOG="$WORK/logs/docker-c.log" \
    PATH="$WORK/fakebin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# ---------------------------------------------------------------- scenario D
# Preset provider + Anthropic warning: pick Anthropic (warns: not
# OpenAI-compatible) -> decline -> back to menu -> pick OpenAI (preset)
# -> override its base URL with the stub server -> pick model #1.
cat > "$WORK/answers-d.txt" <<EOF
Belgium

$TOKEN
123456789

2
n
1
http://127.0.0.1:$STUB_PORT
$KEY
1
$WORK/install-d
n
EOF
run_install d "$WORK/answers-d.txt" \
    VORTEX_TELEGRAM_API_BASE="http://127.0.0.1:$STUB_PORT"

# ---------------------------------------------------------------- assertions
echo "== assertions =="

# --- exit codes first: a failed install makes the rest meaningless
check "A installer exited 0" test "$(cat "$WORK/logs/a.rc")" = "0"
check "B installer exited 0" test "$(cat "$WORK/logs/b.rc")" = "0"
check "C installer exited 0" test "$(cat "$WORK/logs/c.rc")" = "0"

# --- scenario A: .env (loaded back via python-dotenv = quoting verified)
# The venv python (with python-dotenv) is used; override with
# VORTEX_TEST_PY if yours lives elsewhere.
VENV_PY="${VORTEX_TEST_PY:-$HOME/workspace/.venvs/vortex-test/bin/python}"
"$VENV_PY" - "$WORK/install-a/.env" <<'PYEOF' > "$WORK/logs/env-a.txt" 2>&1
import os, sys
from dotenv import load_dotenv
load_dotenv(sys.argv[1], override=True)
for k in ("BOT_TOKEN", "BOSS_ID", "BOT_NAME", "BOT_COUNTRY",
          "BOT_LANGUAGE", "LLM_PROVIDERS", "DATABASE_PATH",
          "UPDATE_CHECK_ENABLED", "UPDATE_REPO"):
    print(f"{k}={os.environ.get(k)}")
PYEOF
check_grep "A .env BOT_COUNTRY=Turkey" "$WORK/logs/env-a.txt" "BOT_COUNTRY=Turkey"
check_grep "A .env BOT_LANGUAGE=tr (default for Turkey)" "$WORK/logs/env-a.txt" "BOT_LANGUAGE=tr"
check_grep "A .env BOSS_ID" "$WORK/logs/env-a.txt" "BOSS_ID=123456789"
check_grep "A .env BOT_NAME trimmed" "$WORK/logs/env-a.txt" "BOT_NAME=Vortex Test"
check_grep "A .env LLM_PROVIDERS pipe format, model #2" "$WORK/logs/env-a.txt" \
    "LLM_PROVIDERS=http://127.0.0.1:18080|sk-test-key-1234567890|stub-model-b"
check_grep "A .env defaults" "$WORK/logs/env-a.txt" "UPDATE_REPO=VortexLabsHQ/vortex-telegram-bot"
check "A .env mode is 0600" test "$(stat -c %a "$WORK/install-a/.env")" = "600"

# --- scenario A: clone + venv + deps
check "A repo cloned (bot/main.py present)" test -f "$WORK/install-a/bot/main.py"
check "A venv created" test -x "$WORK/install-a/.venv/bin/python"
"$WORK/install-a/.venv/bin/pip" show python-telegram-bot > "$WORK/logs/pip-a.txt" 2>&1
check_grep "A python-telegram-bot installed" "$WORK/logs/pip-a.txt" "Name: python-telegram-bot"
"$WORK/install-a/.venv/bin/python" -c "import sys; sys.path.insert(0, '$WORK/install-a'); import bot.countries; print(len(bot.countries.COUNTRIES))" > "$WORK/logs/import-a.txt" 2>&1
check_grep "A installed bot package imports (195 countries)" "$WORK/logs/import-a.txt" "195"

# --- scenario A: dry-run unit + sudoers
check_grep "A unit WorkingDirectory" "$WORK/dry-run-a/vortex-bot.service" "WorkingDirectory=$WORK/install-a"
check_grep "A unit ExecStart" "$WORK/dry-run-a/vortex-bot.service" "ExecStart=$WORK/install-a/.venv/bin/python -m bot.main"
check_grep "A unit User=tester" "$WORK/dry-run-a/vortex-bot.service" "User=tester"
check_grep "A unit Restart=always" "$WORK/dry-run-a/vortex-bot.service" "Restart=always"
check_grep "A sudoers rule" "$WORK/dry-run-a/vortex-bot.sudoers" \
    "tester ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart vortex-bot, /usr/bin/systemctl stop vortex-bot, /usr/bin/systemctl start vortex-bot"
check "A visudo -c passes on sudoers file" visudo -c -f "$WORK/dry-run-a/vortex-bot.sudoers"
check_grep "A installer verified sudoers with visudo" "$WORK/logs/a.log" "Sudoers rule verified with visudo -c."

# --- scenario A: output lines
check_grep "A invalid country suggested Turkey" "$WORK/logs/a.log" "Did you mean one of these?"
check_grep "A country accepted" "$WORK/logs/a.log" "Country: Turkey"
check_grep "A language default accepted" "$WORK/logs/a.log" "Language: tr (Turkish)"
check_grep "A getMe verified bot username" "$WORK/logs/a.log" "Bot username: @vortex_test_bot"
check_grep "A LLM picked from stub list" "$WORK/logs/a.log" "LLM: Custom provider — stub-model-b"
check_grep "A install finished" "$WORK/logs/a.log" "Vortex installed."

# --- scenario B: continue-anyway + manual model id
check_grep "B getMe network failure noted" "$WORK/logs/b.log" "Could not reach Telegram"
check_grep "B continued with unverified token" "$WORK/logs/b.log" "Continue with this unverified token?"
check_grep "B manual model id used" "$WORK/logs/b.log" "LLM: Custom provider — gpt-4o-mini"
check_grep "B .env has manual model" "$WORK/install-b/.env" "gpt-4o-mini"
check_grep "B .env country Iran, language fa" "$WORK/install-b/.env" "BOT_COUNTRY=Iran"
check_grep "B install finished" "$WORK/logs/b.log" "Vortex installed."

# --- scenario D: preset provider + Anthropic warning
check "D installer exited 0" test "$(cat "$WORK/logs/d.rc")" = "0"
check_grep "D Anthropic warning shown" "$WORK/logs/d.log" "NOT OpenAI-compatible"
check_grep "D preset OpenAI picked after declining Anthropic" "$WORK/logs/d.log" "LLM: OpenAI — stub-model-a"
check_grep "D .env has stub model a via OpenAI preset" "$WORK/install-d/.env" "stub-model-a"
check_grep "D .env country Belgium, language en" "$WORK/install-d/.env" "BOT_COUNTRY=Belgium"
check_grep "D .env default bot name Vortex" "$WORK/install-d/.env" "BOT_NAME=Vortex"
check_grep "D install finished" "$WORK/logs/d.log" "Vortex installed."

# --- scenario C: SearXNG with fake docker
# (dry run: the real compose up is skipped, but the installer prints
# the exact command it would run, and the fake docker proves the
# version probe happened.)
check_grep "C docker compose version probed" "$WORK/logs/docker-c.log" "docker compose version"
check_grep "C docker compose up would run" "$WORK/logs/c.log" "Would run: docker compose -f docker-compose.yml -f docker-compose.searxng-only.yml up -d searxng"
check_grep "C override publishes 8080 on loopback" "$WORK/install-c/docker-compose.searxng-only.yml" "127.0.0.1:8080:8080"
SECRET="$(grep -E '^\s*secret:' "$WORK/install-c/searxng/settings.yml" | sed 's/.*secret: *"//; s/"$//')"
check "C SearXNG secret is 64 hex chars" test "${#SECRET}" = 64
check "C SearXNG secret is not the placeholder" test "$SECRET" != "change-me-to-a-random-secret"
check_grep "C dry-run SearXNG status in summary" "$WORK/logs/c.log" "SearXNG     : dry run — compose files written, container not started"
check_grep "C install finished" "$WORK/logs/c.log" "Vortex installed."

echo ""
echo "$pass passed, $fail failed"
exit $(( fail > 0 ? 1 : 0 ))
