#!/usr/bin/env bash
# Vortex Telegram Bot — interactive installer.
#
# The ONE install command (see the README):
#   curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
#
# What it does, in order:
#   1. Checks prerequisites (python3 >= 3.11, venv/pip, git, curl,
#      systemd) and offers to install missing ones with apt.
#   2. Asks: country, bot language, Telegram bot token (verified live
#      against api.telegram.org), boss numeric ID, bot name / wake
#      word, first LLM provider + model (picked from the provider's
#      live /models list).
#   3. Clones the repo, builds a venv, installs requirements, writes .env.
#   4. Creates a systemd service named `vortex-bot` plus the sudoers
#      rule the bot's self-updater needs (NOPASSWD systemctl restart).
#   5. Optionally installs SearXNG (Docker) for web search.
#   6. Verifies the service is active and prints a summary.
#
# Environment overrides (all optional; mainly for testing):
#   VORTEX_REPO_URL       git URL to clone (default: the GitHub repo)
#   VORTEX_REPO_BRANCH    branch to clone (default: main)
#   VORTEX_TELEGRAM_API_BASE
#                         base URL for the getMe check
#                         (default: https://api.telegram.org)
#   VORTEX_TEST_MODE=1    TEST ONLY: stub the Telegram getMe check
#                         (pretends the token is valid, bot
#                         @vortex_test_bot). Never set this for a
#                         real install.
#   VORTEX_DRY_RUN=1      TEST ONLY: do everything except touching
#                         systemd/sudoers/docker — unit + sudoers
#                         files are written under $VORTEX_DRY_RUN_DIR
#                         (default: a fresh dir under /tmp) and
#                         systemctl/docker calls are only printed.
#   VORTEX_INSTALL_USER   TEST ONLY: pretend the installing user is
#                         this name (exercises the non-root sudoers
#                         path when the test runs as root).
#
# Exit codes: 0 = installed (or dry-run complete), 1 = failed or
# refused (message explains why), 130 = interrupted with Ctrl-C.
#
# The country/language tables below are GENERATED from
# bot/countries.py — never edit them by hand; run:
#   python3 scripts/generate_install_data.py

set -euo pipefail

REPO_URL_DEFAULT="https://github.com/VortexLabsHQ/vortex-telegram-bot.git"
REPO_URL="${VORTEX_REPO_URL:-$REPO_URL_DEFAULT}"
REPO_BRANCH="${VORTEX_REPO_BRANCH:-main}"
UPDATE_REPO="VortexLabsHQ/vortex-telegram-bot"
SERVICE_NAME="vortex-bot"
TELEGRAM_API_BASE="${VORTEX_TELEGRAM_API_BASE:-https://api.telegram.org}"

# ---------------------------------------------------------------- helpers

say()  { printf '%s\n' "$*"; }
note() { printf '  %s\n' "$*"; }
warn() { printf 'Warning: %s\n' "$*" >&2; }
die()  { printf '\nError: %s\n' "$*" >&2; exit 1; }

trap 'printf "\nAborted.\n" >&2; exit 130' INT

# Interactive input: the documented install pipes this script through
# stdin (curl ... | bash), so stdin is the script itself and CANNOT be
# used for answers. Read from the terminal (/dev/tty) when there is
# one; otherwise fall back to stdin (script run as `bash install.sh`
# with answers piped in, or tests).
if [[ -t 0 ]]; then
    INPUT_FD=0
elif { exec 3</dev/tty; } 2>/dev/null; then
    # Brace group: the failed open's error goes to /dev/null, while
    # fd 3 (opened by the bare `exec`) stays open in this shell.
    INPUT_FD=3
else
    INPUT_FD=0
fi

# _read_answer VAR [silent] — read one line into $VAR from $INPUT_FD.
# "silent" hides typing (API keys). Dies on EOF with no input.
_read_answer() {
    local _var="$1" _silent="${2:-}" _line="" _rc=0
    if [[ "$_silent" == "silent" ]]; then
        IFS= read -r -s _line <&"$INPUT_FD" || _rc=$?
        printf '\n'
    else
        IFS= read -r _line <&"$INPUT_FD" || _rc=$?
    fi
    if [[ $_rc -ne 0 && -z "$_line" ]]; then
        die "Input closed (EOF). Aborted."
    fi
    printf -v "$_var" '%s' "$_line"
}

# ask_yes_no PROMPT DEFAULT(y|n) — returns 0 for yes, 1 for no.
ask_yes_no() {
    local _prompt="$1" _default="${2:-n}" _hint _ans
    if [[ "$_default" == "y" ]]; then _hint="[Y/n]"; else _hint="[y/N]"; fi
    while true; do
        printf '%s %s ' "$_prompt" "$_hint"
        _read_answer _ans
        _ans="$(trim "$_ans")"
        _ans="${_ans,,}"
        case "$_ans" in
            "") [[ "$_default" == "y" ]] && return 0 || return 1 ;;
            y|yes) return 0 ;;
            n|no)  return 1 ;;
            *) warn "Please answer y or n." ;;
        esac
    done
}

trim() { # strip leading/trailing whitespace
    local s="$1"
    s="${s#"${s%%[![:space:]]*}"}"
    s="${s%"${s##*[![:space:]]}"}"
    printf '%s' "$s"
}

# norm_name — the same matching rule as bot/countries.py::get_country:
# lowercase, collapse runs of whitespace to one space, trim.
norm_name() {
    local s="${1,,}"
    local -a words=()
    read -ra words <<< "$s" || true
    printf '%s' "${words[*]:-}"
}

# mask_key — first 4 + ... + last 4 chars; never print a key in full.
mask_key() {
    local k="$1"
    if [[ ${#k} -lt 8 ]]; then printf '********'; else printf '%s...%s' "${k:0:4}" "${k: -4}"; fi
}

# env_quote VALUE — a .env-safe rendering. Bare when the value is
# plain; double-quoted otherwise, escaping \ and ". NOTE: python-dotenv
# interpolates ${...} in values, so callers must reject a value
# containing '${' before it gets here (see _no_dollar_brace).
env_quote() {
    local v="$1"
    if [[ "$v" =~ ^[A-Za-z0-9_./:,@%+=\~-]+$ ]]; then
        printf '%s' "$v"
        return 0
    fi
    local e="${v//\\/\\\\}"
    e="${e//\"/\\\"}"
    printf '"%s"' "$e"
}

# _no_dollar_brace VALUE WHAT — die-message helper: '${' in a value
# would be silently rewritten by python-dotenv's ${VAR} interpolation.
_no_dollar_brace() {
    # shellcheck disable=SC2016
    # (the literal '${' pattern is intentional here)
    if [[ "$1" == *'${'* ]]; then
        warn "'$2' must not contain '\${' — it would be rewritten when the bot reads .env. Please enter it without that sequence."
        return 1
    fi
    return 0
}

# ---------------------------------------------------------------- generated data

# BEGIN GENERATED INSTALL DATA — do not edit by hand.
# Regenerate with: python3 scripts/generate_install_data.py
# Source: bot/countries.py (195 countries, 40 UI languages).
# shellcheck disable=SC1112
COUNTRY_DATA='Afghanistan|fa
Albania|sq
Algeria|ar
Andorra|ca
Angola|pt
Antigua & Barbuda|en
Argentina|es
Armenia|hy
Australia|en
Austria|de
Azerbaijan|az
Bahamas|en
Bahrain|ar
Bangladesh|bn
Barbados|en
Belarus|be
Belgium|en
Belize|en
Benin|fr
Bhutan|dz
Bolivia|es
Bosnia & Herzegovina|bs
Botswana|en
Brazil|pt
Brunei|ms
Bulgaria|bg
Burkina Faso|fr
Burundi|fr
Cambodia|km
Cameroon|en
Canada|en
Cape Verde|pt
Central African Republic|fr
Chad|fr
Chile|es
China|zh
Colombia|es
Comoros|ar
Congo - Brazzaville|fr
Congo - Kinshasa|fr
Costa Rica|es
Croatia|hr
Cuba|es
Cyprus|el
Czechia|cs
Côte d’Ivoire|fr
Denmark|da
Djibouti|fr
Dominica|en
Dominican Republic|es
Ecuador|es
Egypt|ar
El Salvador|es
Equatorial Guinea|es
Eritrea|ti
Estonia|et
Eswatini|en
Ethiopia|am
Fiji|en
Finland|fi
France|fr
Gabon|fr
Gambia|en
Georgia|ka
Germany|de
Ghana|en
Greece|el
Grenada|en
Guatemala|es
Guinea|fr
Guinea-Bissau|pt
Guyana|en
Haiti|ht
Honduras|es
Hungary|hu
Iceland|is
India|hi
Indonesia|id
Iran|fa
Iraq|ar
Ireland|en
Israel|he
Italy|it
Jamaica|en
Japan|ja
Jordan|ar
Kazakhstan|kk
Kenya|en
Kiribati|en
Kuwait|ar
Kyrgyzstan|ky
Laos|lo
Latvia|lv
Lebanon|ar
Lesotho|en
Liberia|en
Libya|ar
Liechtenstein|de
Lithuania|lt
Luxembourg|lb
Madagascar|fr
Malawi|ny
Malaysia|ms
Maldives|dv
Mali|fr
Malta|mt
Marshall Islands|mh
Mauritania|ar
Mauritius|en
Mexico|es
Micronesia|en
Moldova|ro
Monaco|fr
Mongolia|mn
Montenegro|sr
Morocco|ar
Mozambique|pt
Myanmar|my
Namibia|en
Nauru|na
Nepal|ne
Netherlands|nl
New Zealand|en
Nicaragua|es
Niger|fr
Nigeria|en
North Korea|ko
North Macedonia|mk
Norway|no
Oman|ar
Pakistan|ur
Palau|en
Palestine|ar
Panama|es
Papua New Guinea|en
Paraguay|es
Peru|es
Philippines|tl
Poland|pl
Portugal|pt
Qatar|ar
Romania|ro
Russia|ru
Rwanda|rw
Samoa|sm
San Marino|it
Saudi Arabia|ar
Senegal|fr
Serbia|sr
Seychelles|en
Sierra Leone|en
Singapore|en
Slovakia|sk
Slovenia|sl
Solomon Islands|en
Somalia|so
South Africa|zu
South Korea|ko
South Sudan|en
Spain|es
Sri Lanka|si
St. Kitts & Nevis|en
St. Lucia|en
St. Vincent & Grenadines|en
Sudan|ar
Suriname|nl
Sweden|sv
Switzerland|de
Syria|ar
São Tomé & Príncipe|pt
Tajikistan|tg
Tanzania|sw
Thailand|th
Timor-Leste|pt
Togo|fr
Tonga|to
Trinidad & Tobago|en
Tunisia|ar
Turkey|tr
Turkmenistan|tk
Tuvalu|en
Uganda|en
Ukraine|uk
United Arab Emirates|ar
United Kingdom|en
United States|en
Uruguay|es
Uzbekistan|uz
Vanuatu|bi
Vatican City|la
Venezuela|es
Vietnam|vi
Yemen|ar
Zambia|en
Zimbabwe|en'
LANG_DATA='en|English
fa|Persian (Farsi)
tr|Turkish
de|German
fr|French
es|Spanish
it|Italian
nl|Dutch
ru|Russian
uk|Ukrainian
pl|Polish
sv|Swedish
pt|Portuguese
ar|Arabic
hi|Hindi
ur|Urdu
zh|Chinese
ja|Japanese
ko|Korean
id|Indonesian
th|Thai
vi|Vietnamese
ms|Malay
bn|Bengali
pa|Punjabi
mr|Marathi
te|Telugu
ta|Tamil
gu|Gujarati
am|Amharic
sw|Swahili
ha|Hausa
fil|Filipino
ro|Romanian
hu|Hungarian
cs|Czech
el|Greek
he|Hebrew
da|Danish
no|Norwegian'
# END GENERATED INSTALL DATA

# find_country INPUT — prints "Name|default_lang" on exact match
# (case/whitespace-insensitive), returns 1 when unknown.
find_country() {
    local want
    want="$(norm_name "$1")"
    [[ -n "$want" ]] || return 1
    local name lang
    while IFS='|' read -r name lang; do
        [[ "$(norm_name "$name")" == "$want" ]] || continue
        printf '%s|%s\n' "$name" "$lang"
        return 0
    done <<< "$COUNTRY_DATA"
    return 1
}

# suggest_countries INPUT — up to 8 names, prefix matches first,
# then substring matches (both case-insensitive).
suggest_countries() {
    local want
    want="$(norm_name "$1")"
    [[ -n "$want" ]] || return 0
    local count=0 name lang lname
    while IFS='|' read -r name lang; do
        lname="$(norm_name "$name")"
        if [[ "$lname" == "$want"* ]]; then
            printf '%s\n' "$name"
            count=$((count + 1))
            [[ $count -ge 8 ]] && return 0
        fi
    done <<< "$COUNTRY_DATA"
    while IFS='|' read -r name lang; do
        lname="$(norm_name "$name")"
        if [[ "$lname" == *"$want"* && "$lname" != "$want"* ]]; then
            printf '%s\n' "$name"
            count=$((count + 1))
            [[ $count -ge 8 ]] && return 0
        fi
    done <<< "$COUNTRY_DATA"
    return 0
}

# lang_known CODE — true when CODE is one of the 22 bot UI languages.
lang_known() {
    local want="${1,,}" code _name
    while IFS='|' read -r code _name; do
        [[ "$code" == "$want" ]] && return 0
    done <<< "$LANG_DATA"
    return 1
}

# lang_display CODE — English display name for a UI language code.
lang_display() {
    local want="${1,,}" code name
    while IFS='|' read -r code name; do
        [[ "$code" == "$want" ]] && { printf '%s' "$name"; return 0; }
    done <<< "$LANG_DATA"
    return 1
}

# ---------------------------------------------------------------- prerequisites

check_prereqs() {
    say "Checking prerequisites..."
    local missing=() missing_pkgs=() warnings=()
    local pyver=""

    if ! command -v python3 >/dev/null 2>&1; then
        say "  [missing] python3 (>= 3.11)"
        missing+=("python3 (>= 3.11)"); missing_pkgs+=("python3")
    elif ! python3 -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)' 2>/dev/null; then
        pyver="$(python3 --version 2>&1)"
        say "  [missing] python3 >= 3.11 (found $pyver)"
        missing+=("python3 >= 3.11 (found $pyver)"); missing_pkgs+=("python3")
    else
        pyver="$(python3 --version 2>&1)"
        say "  [ok] $pyver"
    fi

    if ! python3 -c 'import venv, ensurepip' 2>/dev/null; then
        say "  [missing] python3 venv support (python3 -m venv)"
        missing+=("python3 venv support"); missing_pkgs+=("python3-venv")
    else
        say "  [ok] python3 venv"
    fi

    if ! python3 -m pip --version >/dev/null 2>&1; then
        say "  [missing] pip (python3 -m pip)"
        missing+=("pip"); missing_pkgs+=("python3-pip")
    else
        say "  [ok] pip"
    fi

    local cmd pkg
    for cmd in git curl systemctl; do
        if command -v "$cmd" >/dev/null 2>&1; then
            say "  [ok] $cmd"
        else
            say "  [missing] $cmd"
            missing+=("$cmd")
            # apt package name differs for systemctl.
            if [[ "$cmd" == "systemctl" ]]; then pkg="systemd"; else pkg="$cmd"; fi
            missing_pkgs+=("$pkg")
        fi
    done

    if [[ ! -d /run/systemd/system ]]; then
        warnings+=("systemd does not appear to be running as PID 1 on this machine — the bot service cannot be enabled here; the installer will write the unit file into the install directory for manual setup instead.")
    fi
    if ! command -v docker >/dev/null 2>&1; then
        warnings+=("Docker is not installed — the optional SearXNG step will be skipped (web search falls back to Wikipedia).")
    fi
    if ! command -v openssl >/dev/null 2>&1; then
        warnings+=("openssl is not installed — the SearXNG secret will be generated from /dev/urandom instead.")
    fi

    local w
    for w in "${warnings[@]}"; do warn "$w"; done

    if [[ ${#missing[@]} -eq 0 ]]; then
        say "All prerequisites are present."
        return 0
    fi

    say ""
    say "Missing: ${missing[*]}"
    if command -v apt-get >/dev/null 2>&1; then
        # De-duplicate the package list (python3 may appear twice).
        local -a pkgs_arr=() _p=""
        while IFS= read -r _p; do pkgs_arr+=("$_p"); done < <(printf '%s\n' "${missing_pkgs[@]}" | sort -u)
        local pkgs_display="${pkgs_arr[*]}"
        local apt_failed="apt install failed — install ${missing[*]} by hand and re-run this installer."
        if [[ $EUID -eq 0 ]]; then
            if ask_yes_no "Install the missing packages with apt (apt-get install -y $pkgs_display)?" "y"; then
                if ! apt-get update -qq; then die "$apt_failed"; fi
                if ! apt-get install -y "${pkgs_arr[@]}"; then die "$apt_failed"; fi
                say "Re-checking prerequisites..."
                check_prereqs
                return 0
            fi
        elif command -v sudo >/dev/null 2>&1; then
            if ask_yes_no "Install the missing packages with sudo apt (sudo apt-get install -y $pkgs_display)?" "y"; then
                if ! sudo apt-get update -qq; then die "$apt_failed"; fi
                if ! sudo apt-get install -y "${pkgs_arr[@]}"; then die "$apt_failed"; fi
                say "Re-checking prerequisites..."
                check_prereqs
                return 0
            fi
        else
            warn "No sudo available to install packages automatically."
        fi
        die "Cannot continue without: ${missing[*]}. On Debian/Ubuntu run: sudo apt-get update && sudo apt-get install -y $pkgs_display — then re-run this installer. On other systems install python3 (>= 3.11) with venv + pip, git, curl and systemd, then re-run."
    fi
    die "Cannot continue without: ${missing[*]}. Install python3 (>= 3.11) with venv + pip, git, curl and systemd for your system, then re-run this installer."
}

# ---------------------------------------------------------------- questions

ask_country() {
    say ""
    say "Step 1/6 — Country"
    note "The country sets the timezone, the local currency for prices,"
    note "prayer times and local content. Paste the English name exactly"
    note "as listed in the README (e.g. Turkey)."
    local ans found
    while true; do
        printf 'Country: '
        _read_answer ans
        ans="$(trim "$ans")"
        if [[ -z "$ans" ]]; then warn "Please enter a country name."; continue; fi
        if found="$(find_country "$ans")"; then
            COUNTRY_NAME="${found%%|*}"
            COUNTRY_LANG="${found##*|}"
            say "Country: $COUNTRY_NAME"
            return 0
        fi
        warn "No match for '$ans'."
        local sugg
        sugg="$(suggest_countries "$ans")"
        if [[ -n "$sugg" ]]; then
            say "  Did you mean one of these?"
            printf '%s\n' "$sugg" | sed 's/^/    - /'
        else
            say "  Check the spelling against the country list in the README."
        fi
    done
}

ask_language() {
    say ""
    say "Step 2/6 — Bot language"
    note "Language is separate from country: it only changes what the"
    note "bot says. Press Enter to accept the default for your country."
    local code name
    while IFS='|' read -r code name; do
        printf '  %s — %s\n' "$code" "$name"
    done <<< "$LANG_DATA"
    local ans default="$COUNTRY_LANG"
    while true; do
        printf 'Language [%s]: ' "$default"
        _read_answer ans
        ans="$(trim "$ans")"
        ans="${ans,,}"
        [[ -z "$ans" ]] && ans="$default"
        if [[ "$ans" == "$default" ]]; then
            BOT_LANGUAGE="$ans"
            if ! lang_known "$ans"; then
                warn "The bot has no full translation for '$ans' yet — it will answer in English until one ships. You can change the language later from the hidden /admin panel."
            else
                say "Language: $ans ($(lang_display "$ans"))"
            fi
            return 0
        fi
        if lang_known "$ans"; then
            BOT_LANGUAGE="$ans"
            say "Language: $ans ($(lang_display "$ans"))"
            return 0
        fi
        warn "'$ans' is not one of the bot languages above. Type a code from the list, or press Enter for the default ($default)."
    done
}

# telegram_getme TOKEN — 0 = token valid (sets TG_USERNAME),
# 1 = Telegram rejected the token, 2 = network error.
telegram_getme() {
    local token="$1"
    if [[ -n "${VORTEX_TEST_MODE:-}" ]]; then
        TG_USERNAME="vortex_test_bot"
        return 0
    fi
    local url="${TELEGRAM_API_BASE}/bot${token}/getMe"
    local body http_code
    body="$(curl -sS -m 15 -w '\n%{http_code}' "$url" 2>/dev/null)" || return 2
    [[ -n "$body" ]] || return 2
    http_code="${body##*$'\n'}"
    body="${body%$'\n'*}"
    case "$http_code" in
        401|403|404) return 1 ;;  # bad token
        200) ;;
        *) return 2 ;;            # 5xx / 429 / odd status: network-side
    esac
    TG_USERNAME="$(printf '%s' "$body" | python3 -c 'import json,sys
try:
    d = json.load(sys.stdin)
except Exception:
    print("")
else:
    print(d.get("result", {}).get("username", "") if d.get("ok") else "")' 2>/dev/null)"
    [[ -n "$TG_USERNAME" ]] && return 0 || return 1
}

ask_token() {
    say ""
    say "Step 3/6 — Telegram bot token"
    note "Create the bot with @BotFather on Telegram and paste its token here."
    local tok rc=0
    while true; do
        printf 'Bot token: '
        _read_answer tok silent
        tok="$(trim "$tok")"
        if [[ ! "$tok" =~ ^[0-9]+:[A-Za-z0-9_-]{35,}$ ]]; then
            warn "That doesn't look like a bot token (expected digits, a colon, then 35+ characters)."
            continue
        fi
        rc=0
        telegram_getme "$tok" || rc=$?
        if [[ $rc -eq 0 ]]; then
            say "Bot username: @$TG_USERNAME"
            if [[ -n "${VORTEX_TEST_MODE:-}" ]]; then
                note "(test mode — Telegram was not contacted)"
            fi
            BOT_TOKEN="$tok"
            return 0
        fi
        if [[ $rc -eq 2 ]]; then
            warn "Could not reach Telegram (network error) — the token format looks valid but could not be verified."
            if ask_yes_no "Continue with this unverified token?" "n"; then
                BOT_TOKEN="$tok"
                return 0
            fi
            continue
        fi
        warn "Telegram rejected this token (getMe failed). Double-check it in @BotFather and try again."
    done
}

ask_boss_id() {
    say ""
    say "Step 4/6 — Boss (owner) Telegram ID"
    note "Your numeric Telegram user ID — find it with @userinfobot."
    note "Only this account can use the hidden /admin panel."
    local ans
    while true; do
        printf 'Boss numeric ID: '
        _read_answer ans
        ans="$(trim "$ans")"
        if [[ "$ans" =~ ^[0-9]{5,20}$ ]]; then
            BOSS_ID="$ans"
            return 0
        fi
        warn "Enter digits only (your numeric Telegram user ID, e.g. 123456789)."
    done
}

ask_bot_name() {
    say ""
    say "Step 5/6 — Bot name / wake word"
    note "This is the bot's name AND its wake word in groups: users say"
    note "this name to talk to it. Any language is fine, e.g. Vortex or ورتکس."
    local ans
    while true; do
        printf 'Bot name [Vortex]: '
        _read_answer ans
        ans="$(trim "$ans")"
        [[ -z "$ans" ]] && ans="Vortex"
        if _no_dollar_brace "$ans" "bot name"; then
            BOT_NAME="$ans"
            say "Bot name: $BOT_NAME"
            return 0
        fi
    done
}

# Preset LLM providers (OpenAI-compatible endpoints — that is what the
# bot's chat client speaks). Anthropic's native API is NOT
# OpenAI-compatible, so picking it prints a warning and asks again.
PROVIDER_NAMES=(
    "OpenAI" "Anthropic" "OpenRouter" "Google AI (Gemini)" "DeepSeek"
    "Groq" "Together AI" "Mistral AI" "xAI (Grok)" "Cohere"
)
PROVIDER_BASES=(
    "https://api.openai.com/v1"
    "https://api.anthropic.com/v1"
    "https://openrouter.ai/api/v1"
    "https://generativelanguage.googleapis.com/v1beta/openai/"
    "https://api.deepseek.com/v1"
    "https://api.groq.com/openai/v1"
    "https://api.together.xyz/v1"
    "https://api.mistral.ai/v1"
    "https://api.x.ai/v1"
    "https://api.cohere.com/compatibility/v1"
)
PROVIDER_IDS=(
    "openai" "anthropic" "openrouter" "google" "deepseek"
    "groq" "together" "mistral" "xai" "cohere"
)

# fetch_models BASE_URL API_KEY PROVIDER_ID — prints one model id per
# line from GET {base_url}/models; returns 1 when the list cannot be
# fetched or parsed. Anthropic's /models needs its own headers.
fetch_models() {
    local base="$1" key="$2" prov="${3:-}"
    local url="${base%/}/models" body=""
    if [[ "$prov" == "anthropic" ]]; then
        body="$(curl -sS -m 20 -H "x-api-key: $key" -H "anthropic-version: 2023-06-01" "$url" 2>/dev/null)" || return 1
    else
        body="$(curl -sS -m 20 -H "Authorization: Bearer $key" "$url" 2>/dev/null)" || return 1
    fi
    [[ -n "$body" ]] || return 1
    printf '%s' "$body" | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
except Exception:
    raise SystemExit(1)
ids = []
for m in d.get("data", []) or []:
    i = m.get("id") if isinstance(m, dict) else None
    if i:
        ids.append(str(i))
if not ids:
    raise SystemExit(1)
print("\n".join(ids))
' 2>/dev/null
}

# _pick_model MODEL_LIST — numbered pick (or a typed model id).
# The list and prompts go to stderr; ONLY the chosen model id goes to
# stdout (callers capture it with $(...)).
_pick_model() {
    local -a models=()
    mapfile -t models <<< "$1"
    local total=${#models[@]}
    local shown=$(( total > 50 ? 50 : total ))
    say "Models available ($total):" >&2
    local i
    for ((i = 0; i < shown; i++)); do
        printf '  %s) %s\n' "$((i + 1))" "${models[$i]}" >&2
    done
    if [[ $total -gt $shown ]]; then
        note "... and $((total - shown)) more — type any model id directly to pick one not shown." >&2
    fi
    local ans
    while true; do
        printf 'Pick a model by number, or type a model id: ' >&2
        _read_answer ans
        ans="$(trim "$ans")"
        if [[ "$ans" =~ ^[0-9]+$ ]] && (( ans >= 1 && ans <= total )); then
            printf '%s\n' "${models[$((ans - 1))]}"
            return 0
        fi
        if [[ -n "$ans" ]] && _no_dollar_brace "$ans" "model id"; then
            printf '%s\n' "$ans"
            return 0
        fi
    done
}

ask_llm() {
    say ""
    say "Step 6/6 — First LLM provider"
    note "The bot chats through an OpenAI-compatible API. Pick a provider,"
    note "paste its API key, then pick a model from its live model list."
    local choice prov_name prov_base prov_id base key models model ans
    while true; do
        local i
        for ((i = 0; i < ${#PROVIDER_NAMES[@]}; i++)); do
            printf '  %s) %s\n' "$((i + 1))" "${PROVIDER_NAMES[$i]}"
        done
        printf '  %s) %s\n' "$(( ${#PROVIDER_NAMES[@]} + 1 ))" "Custom provider"
        printf 'Choose [1-%s]: ' "$(( ${#PROVIDER_NAMES[@]} + 1 ))"
        _read_answer choice
        choice="$(trim "$choice")"
        if [[ ! "$choice" =~ ^[0-9]+$ ]] || (( choice < 1 || choice > ${#PROVIDER_NAMES[@]} + 1 )); then
            warn "Enter a number 1-$(( ${#PROVIDER_NAMES[@]} + 1 ))."
            continue
        fi
        if (( choice == ${#PROVIDER_NAMES[@]} + 1 )); then
            prov_name="Custom provider"; prov_base=""; prov_id="custom"
        else
            prov_name="${PROVIDER_NAMES[$((choice - 1))]}"
            prov_base="${PROVIDER_BASES[$((choice - 1))]}"
            prov_id="${PROVIDER_IDS[$((choice - 1))]}"
        fi

        # Anthropic's native API is not OpenAI-compatible: the bot's
        # chat client cannot talk to it directly. Say so plainly and
        # let the user go back (or continue via a compatible gateway).
        if [[ "$prov_id" == "anthropic" ]]; then
            warn "Anthropic's native API is NOT OpenAI-compatible, so this bot cannot chat with it directly — the key would only work through an OpenAI-compatible gateway (paste the gateway's base URL below)."
            ask_yes_no "Continue with Anthropic anyway?" "n" || continue
        fi

        # Base URL (editable; empty for custom = must type one).
        while true; do
            if [[ -n "$prov_base" ]]; then
                printf 'Base URL [%s]: ' "$prov_base"
            else
                printf 'Base URL (e.g. https://api.example.com/v1): '
            fi
            _read_answer ans
            ans="$(trim "$ans")"
            [[ -z "$ans" ]] && ans="$prov_base"
            if [[ "$ans" == http://* || "$ans" == https://* ]]; then
                base="$ans"
                break
            fi
            warn "Enter a base URL starting with http:// or https://"
        done

        # API key (typed blind; only a masked fingerprint is ever shown).
        while true; do
            printf 'API key for %s: ' "$prov_name"
            _read_answer key silent
            key="$(trim "$key")"
            if [[ ${#key} -lt 8 ]]; then
                warn "That key looks too short — paste the full API key."
                continue
            fi
            if ! _no_dollar_brace "$key" "API key"; then
                continue
            fi
            break
        done
        say "Key saved (fingerprint $(mask_key "$key"))."

        # Model: live /models list when possible, manual id otherwise.
        if models="$(fetch_models "$base" "$key" "$prov_id")"; then
            model="$(_pick_model "$models")"
        else
            warn "Could not list models from $base — check the key and base URL, or type the model id manually."
            while true; do
                printf 'Model id: '
                _read_answer model
                model="$(trim "$model")"
                if [[ -n "$model" ]] && _no_dollar_brace "$model" "model id"; then
                    break
                fi
                [[ -n "$model" ]] || warn "Enter a model id."
            done
        fi

        LLM_PROVIDER_NAME="$prov_name"
        LLM_BASE="$base"
        LLM_KEY="$key"
        LLM_MODEL="$model"
        say "LLM: $prov_name — $model"
        return 0
    done
}

# ---------------------------------------------------------------- install

ask_install_dir() {
    say ""
    local default
    if [[ $EUID -eq 0 ]]; then default="/opt/vortex-bot"; else default="$HOME/vortex-bot"; fi
    local ans
    while true; do
        printf 'Install directory [%s]: ' "$default"
        _read_answer ans
        ans="$(trim "$ans")"
        [[ -z "$ans" ]] && ans="$default"
        if [[ "$ans" == "~"* ]]; then
            ans="$HOME${ans:1}"
        fi
        if [[ "$ans" == /* ]]; then
            INSTALL_DIR="$ans"
            return 0
        fi
        warn "Enter an absolute path (e.g. $default)."
    done
}

# _tarball_url — codeload URL for the repo, or nothing when the repo
# URL is not a github.com URL (local test repos, SSH URLs, other hosts).
_tarball_url() {
    local u="${REPO_URL%.git}"
    case "$u" in
        https://github.com/*) u="${u#https://github.com/}" ;;
        http://github.com/*)  u="${u#http://github.com/}" ;;
        git@github.com:*)     u="${u#git@github.com:}" ;;
        *) return 1 ;;
    esac
    printf 'https://codeload.github.com/%s/tarball/refs/heads/%s' "$u" "$REPO_BRANCH"
}

clone_repo() {
    say ""
    say "Fetching the code..."
    if [[ -d "$INSTALL_DIR/.git" ]]; then
        say "Install directory already holds a git checkout — updating it."
        if ! git -C "$INSTALL_DIR" pull --ff-only 2>/dev/null; then
            warn "git pull failed — continuing with the existing checkout."
        fi
        return 0
    fi
    if [[ -e "$INSTALL_DIR" ]] && [[ -n "$(ls -A "$INSTALL_DIR" 2>/dev/null)" ]]; then
        die "Install directory $INSTALL_DIR already exists and is not empty. Move it aside or pick another directory."
    fi
    mkdir -p "$(dirname "$INSTALL_DIR")"
    local clone_err
    clone_err="$(mktemp)"
    if git clone --branch "$REPO_BRANCH" "$REPO_URL" "$INSTALL_DIR" 2>"$clone_err"; then
        rm -f "$clone_err"
        say "Cloned $REPO_URL (branch $REPO_BRANCH) into $INSTALL_DIR."
        return 0
    fi
    warn "git clone failed:"
    sed 's/^/  /' "$clone_err" | tail -5 >&2
    rm -f "$clone_err"
    say "Trying the release tarball instead..."
    local tarball_url tmpdir
    tarball_url="$(_tarball_url)" || die "Clone failed and no tarball fallback exists for this repo URL. If the repo is still private, make it public (or run this installer from a machine with git access to it) and try again."
    tmpdir="$(mktemp -d)"
    if curl -sSL -m 120 "$tarball_url" -o "$tmpdir/vortex.tar.gz" 2>/dev/null \
        && mkdir -p "$tmpdir/extract" \
        && tar -xzf "$tmpdir/vortex.tar.gz" -C "$tmpdir/extract" 2>/dev/null \
        && mkdir -p "$INSTALL_DIR"; then
        local topdir
        topdir="$(find "$tmpdir/extract" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
        if [[ -n "$topdir" ]]; then
            cp -a "$topdir/." "$INSTALL_DIR/"
            rm -rf "$tmpdir"
            say "Downloaded the tarball into $INSTALL_DIR."
            return 0
        fi
    fi
    rm -rf "$tmpdir"
    die "Could not fetch the code (clone and tarball both failed). If the repo is still private, make it public (or run this installer from a machine with git access to it) and try again."
}

install_deps() {
    say ""
    say "Creating the Python virtual environment..."
    python3 -m venv "$INSTALL_DIR/.venv" || die "python3 -m venv failed — is the python3-venv package installed?"
    say "Installing dependencies (this takes a minute or two)..."
    "$INSTALL_DIR/.venv/bin/pip" install --quiet --upgrade pip \
        || die "pip upgrade failed — check your network and re-run the installer."
    "$INSTALL_DIR/.venv/bin/pip" install --quiet -r "$INSTALL_DIR/requirements.txt" \
        || die "pip install -r requirements.txt failed — check your network and re-run the installer."
    say "Dependencies installed."
}

# _env_line KEY VALUE — prints "KEY=<quoted value>".
_env_line() {
    printf '%s=%s\n' "$1" "$(env_quote "$2")"
}

write_env() {
    say ""
    local env_file="$INSTALL_DIR/.env"
    local llm_providers="${LLM_BASE}|${LLM_KEY}|${LLM_MODEL}"
    if [[ -f "$env_file" ]]; then
        if ask_yes_no "A .env already exists in $INSTALL_DIR. Overwrite it with the new answers?" "n"; then
            say "Overwriting the existing .env."
        else
            say "Keeping the existing .env — filling in only values that are missing."
            # Append each of our keys only when it is absent.
            local -a pairs=(
                "BOT_TOKEN|$BOT_TOKEN" "BOSS_ID|$BOSS_ID"
                "BOT_NAME|$BOT_NAME" "BOT_COUNTRY|$COUNTRY_NAME"
                "BOT_LANGUAGE|$BOT_LANGUAGE" "LLM_PROVIDERS|$llm_providers"
                "DATABASE_PATH|data/vortex_bot.db"
                "UPDATE_CHECK_ENABLED|1"
                "UPDATE_REPO|$UPDATE_REPO"
            )
            local pair k v
            for pair in "${pairs[@]}"; do
                k="${pair%%|*}"; v="${pair#*|}"
                if grep -q "^${k}=" "$env_file"; then
                    note "  $k already set — kept."
                else
                    _env_line "$k" "$v" >> "$env_file"
                    note "  $k added."
                fi
            done
            chmod 600 "$env_file"
            return 0
        fi
    fi
    {
        say "# Vortex Telegram Bot — generated by install.sh. Keep this file secret."
        say "# See .env.example for every available setting."
        _env_line "BOT_TOKEN" "$BOT_TOKEN"
        _env_line "BOSS_ID" "$BOSS_ID"
        _env_line "BOT_NAME" "$BOT_NAME"
        _env_line "BOT_COUNTRY" "$COUNTRY_NAME"
        _env_line "BOT_LANGUAGE" "$BOT_LANGUAGE"
        _env_line "LLM_PROVIDERS" "$llm_providers"
        _env_line "DATABASE_PATH" "data/vortex_bot.db"
        _env_line "UPDATE_CHECK_ENABLED" "1"
        _env_line "UPDATE_REPO" "$UPDATE_REPO"
    } > "$env_file"
    chmod 600 "$env_file"
    say "Wrote $env_file (mode 0600)."
}

# ---------------------------------------------------------------- systemd + sudoers

# _write_unit_file PATH USER_MODE(y|n) — writes vortex-bot.service.
_write_unit_file() {
    local path="$1" user_mode="$2"
    local wanted_by="multi-user.target"
    [[ "$user_mode" == "y" ]] && wanted_by="default.target"
    {
        printf '[Unit]\n'
        printf 'Description=Vortex Telegram Bot\n'
        printf 'After=network-online.target\n'
        printf 'Wants=network-online.target\n\n'
        printf '[Service]\n'
        printf 'Type=simple\n'
        printf 'WorkingDirectory=%s\n' "$INSTALL_DIR"
        printf 'ExecStart=%s/.venv/bin/python -m bot.main\n' "$INSTALL_DIR"
        printf 'EnvironmentFile=%s/.env\n' "$INSTALL_DIR"
        if [[ "$user_mode" == "n" && -n "${INSTALL_USER:-}" ]]; then
            printf 'User=%s\n' "$INSTALL_USER"
        fi
        printf 'Restart=always\n'
        printf 'RestartSec=5\n\n'
        printf '[Install]\n'
        printf 'WantedBy=%s\n' "$wanted_by"
    } > "$path"
}

# _sudoers_text — the exact rule the self-updater needs (updater.py
# runs `sudo systemctl restart vortex-bot`).
_sudoers_text() {
    local bin="$1"
    printf '# Vortex Telegram Bot — lets the bot user restart its own service.\n'
    printf '# Required by the bot self-updater (bot/updater.py). Installed by install.sh.\n'
    printf '%s ALL=(ALL) NOPASSWD: %s restart %s, %s stop %s, %s start %s\n' \
        "$INSTALL_USER" "$bin" "$SERVICE_NAME" "$bin" "$SERVICE_NAME" "$bin" "$SERVICE_NAME"
}

setup_systemd() {
    say ""
    say "Setting up the systemd service ($SERVICE_NAME)..."
    local dry_run="${VORTEX_DRY_RUN:-}"
    local out_dir="${VORTEX_DRY_RUN_DIR:-}"
    if [[ -n "$dry_run" ]]; then
        [[ -n "$out_dir" ]] || out_dir="$(mktemp -d /tmp/vortex-dry-run.XXXXXX)"
        mkdir -p "$out_dir"
        VORTEX_DRY_RUN_DIR="$out_dir"
        say "(dry run — unit + sudoers files go to $out_dir; no systemctl calls)"
    fi

    # Who the service runs as: the real user behind sudo, else the caller.
    # VORTEX_INSTALL_USER overrides this (test-only: lets a root-run
    # dry run exercise the non-root sudoers path).
    if [[ -n "${VORTEX_INSTALL_USER:-}" ]]; then
        INSTALL_USER="$VORTEX_INSTALL_USER"
    elif [[ -n "${SUDO_USER:-}" ]]; then
        INSTALL_USER="$SUDO_USER"
    else
        INSTALL_USER="$(id -un)"
    fi
    # Root-owned install dir must be usable by the service user.
    if [[ $EUID -eq 0 && "$INSTALL_USER" != "root" ]]; then
        chown -R "$INSTALL_USER" "$INSTALL_DIR" 2>/dev/null || warn "Could not chown $INSTALL_DIR to $INSTALL_USER."
    fi

    local mode="system" unit_path="" sudoers_path="" sysctl_bin=""
    sysctl_bin="$(command -v systemctl)"
    if [[ -n "$dry_run" ]]; then
        mode="system"
        unit_path="$VORTEX_DRY_RUN_DIR/$SERVICE_NAME.service"
        sudoers_path="$VORTEX_DRY_RUN_DIR/$SERVICE_NAME.sudoers"
    elif [[ ! -d /run/systemd/system ]]; then
        mode="none"
        unit_path="$INSTALL_DIR/$SERVICE_NAME.service"
    elif [[ $EUID -eq 0 ]]; then
        mode="system"
        unit_path="/etc/systemd/system/$SERVICE_NAME.service"
        sudoers_path="/etc/sudoers.d/$SERVICE_NAME"
    elif sudo -n true 2>/dev/null; then
        mode="system"
        unit_path="/etc/systemd/system/$SERVICE_NAME.service"
        sudoers_path="/etc/sudoers.d/$SERVICE_NAME"
    elif command -v sudo >/dev/null 2>&1 && ask_yes_no "Install as a system service (needs sudo)?" "y"; then
        mode="system"
        unit_path="/etc/systemd/system/$SERVICE_NAME.service"
        sudoers_path="/etc/sudoers.d/$SERVICE_NAME"
    else
        mode="user"
        unit_path="$HOME/.config/systemd/user/$SERVICE_NAME.service"
    fi

    if [[ "$mode" == "none" ]]; then
        local unit_tmp
        unit_tmp="$(mktemp)"
        _write_unit_file "$unit_tmp" "n"
        cp "$unit_tmp" "$unit_path"
        rm -f "$unit_tmp"
        warn "systemd is not running as PID 1 here, so the service cannot be enabled."
        say "The unit file was written to $unit_path — copy it to /etc/systemd/system/ on the target server, then run: sudo systemctl daemon-reload && sudo systemctl enable --now $SERVICE_NAME"
        say "Note: the self-updater's restart will not work until the service is installed that way."
        SYSTEMD_MODE="none"
        return 0
    fi

    # Write the unit to a temp file first, then install it with the
    # right privileges (a non-root user cannot write /etc directly).
    local unit_tmp
    unit_tmp="$(mktemp)"
    _write_unit_file "$unit_tmp" "$([[ "$mode" == "user" ]] && printf 'y' || printf 'n')"
    if [[ "$mode" == "system" ]]; then
        if [[ -n "$dry_run" ]]; then
            cp "$unit_tmp" "$unit_path"
            say "Would run: sudo systemctl daemon-reload && sudo systemctl enable --now $SERVICE_NAME (skipped in dry run)"
        elif [[ $EUID -eq 0 ]]; then
            install -m 0644 "$unit_tmp" "/etc/systemd/system/$SERVICE_NAME.service"
            systemctl daemon-reload
            unit_path="/etc/systemd/system/$SERVICE_NAME.service"
        else
            sudo install -m 0644 "$unit_tmp" "/etc/systemd/system/$SERVICE_NAME.service"
            sudo systemctl daemon-reload
            unit_path="/etc/systemd/system/$SERVICE_NAME.service"
        fi
    else
        mkdir -p "$(dirname "$unit_path")"
        install -m 0644 "$unit_tmp" "$unit_path"
        systemctl --user daemon-reload
    fi
    rm -f "$unit_tmp"
    say "Service file: $unit_path"

    # Sudoers rule (system services only; root needs none; user
    # services are restarted by the user, not by sudo systemctl).
    if [[ "$mode" == "system" && "$INSTALL_USER" != "root" ]]; then
        local tmp_sudoers
        tmp_sudoers="$(mktemp)"
        _sudoers_text "$sysctl_bin" > "$tmp_sudoers"
        if [[ -n "$dry_run" ]]; then
            cp "$tmp_sudoers" "$sudoers_path"
            say "Would install sudoers rule at /etc/sudoers.d/$SERVICE_NAME (dry-run copy: $sudoers_path)"
        else
            if [[ $EUID -eq 0 ]]; then
                install -m 0440 "$tmp_sudoers" "/etc/sudoers.d/$SERVICE_NAME"
            else
                sudo install -m 0440 "$tmp_sudoers" "/etc/sudoers.d/$SERVICE_NAME"
            fi
            say "Sudoers rule installed at /etc/sudoers.d/$SERVICE_NAME"
        fi
        if command -v visudo >/dev/null 2>&1; then
            if ! visudo -c -f "${sudoers_path:-/etc/sudoers.d/$SERVICE_NAME}" >/dev/null 2>&1; then
                warn "visudo check FAILED for the sudoers rule — the self-updater's restart will not work until this is fixed by hand."
            else
                say "Sudoers rule verified with visudo -c."
            fi
        else
            note "visudo not found — the sudoers rule was not syntax-checked."
        fi
        rm -f "$tmp_sudoers"
    fi

    # Enable + start (skipped in dry-run).
    if [[ -n "$dry_run" ]]; then
        say "Would run: systemctl enable --now $SERVICE_NAME (skipped in dry run)"
        SYSTEMD_MODE="dry-run"
        return 0
    fi
    if [[ "$mode" == "system" ]]; then
        if [[ $EUID -eq 0 ]]; then
            systemctl enable --now "$SERVICE_NAME"
        else
            sudo systemctl enable --now "$SERVICE_NAME"
        fi
    else
        systemctl --user enable --now "$SERVICE_NAME"
        if command -v loginctl >/dev/null 2>&1; then
            loginctl enable-linger "$INSTALL_USER" 2>/dev/null || true
        fi
        warn "User service installed: the self-updater runs 'sudo systemctl restart $SERVICE_NAME' (system scope), which will NOT restart a user service — automatic restarts after updates will not work. Prefer a system service when possible."
    fi
    SYSTEMD_MODE="$mode"
}

# ---------------------------------------------------------------- searxng

setup_searxng() {
    say ""
    if ! ask_yes_no "Install SearXNG for web search? (needs Docker)" "n"; then
        note "Skipped — web search will fall back to Wikipedia."
        SEARXNG_STATUS="skipped (web search falls back to Wikipedia)"
        return 0
    fi
    local compose_cmd=""
    if command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
        compose_cmd="docker compose"
    elif command -v docker-compose >/dev/null 2>&1; then
        compose_cmd="docker-compose"
    else
        warn "Docker (with Compose) was not found — skipping SearXNG. Web search will fall back to Wikipedia."
        SEARXNG_STATUS="skipped — Docker not found (web search falls back to Wikipedia)"
        return 0
    fi
    if [[ ! -f "$INSTALL_DIR/searxng/settings.yml" ]]; then
        warn "searxng/settings.yml is missing from the install — skipping SearXNG. Web search will fall back to Wikipedia."
        SEARXNG_STATUS="skipped — settings.yml missing (web search falls back to Wikipedia)"
        return 0
    fi
    # Random server secret (SearXNG refuses to start with the default).
    local secret=""
    if command -v openssl >/dev/null 2>&1; then
        secret="$(openssl rand -hex 32 2>/dev/null || true)"
    fi
    if [[ -z "$secret" ]]; then
        secret="$(head -c 32 /dev/urandom | od -An -tx1 | tr -d ' \n')"
    fi
    python3 - "$INSTALL_DIR/searxng/settings.yml" "$secret" <<'PYEOF'
import re, sys
path, secret = sys.argv[1], sys.argv[2]
text = open(path, encoding="utf-8").read()
new, n = re.subn(r'^(\s*secret:\s*).*$', r'\g<1>"' + secret + '"', text,
                 count=1, flags=re.M)
if n != 1:
    raise SystemExit("could not find the 'secret:' line in settings.yml")
open(path, "w", encoding="utf-8").write(new)
PYEOF
    say "SearXNG secret generated."
    # The bot runs under systemd on the host and reaches SearXNG at
    # http://127.0.0.1:8080 (bot/web_tools.py), so the container must
    # publish 8080 on the host loopback. The stock docker-compose.yml
    # does not publish it (its bot service shares the searxng network
    # namespace instead), so this override adds the port mapping.
    # It is a separate file (not docker-compose.override.yml) so plain
    # `docker compose up` behaviour is unchanged.
    cat > "$INSTALL_DIR/docker-compose.searxng-only.yml" <<'EOF'
# Generated by install.sh: publish SearXNG on the host loopback so the
# systemd bot (which calls http://127.0.0.1:8080) can reach it.
services:
  searxng:
    ports:
      - "127.0.0.1:8080:8080"
EOF
    if [[ -n "${VORTEX_DRY_RUN:-}" ]]; then
        say "Would run: $compose_cmd -f docker-compose.yml -f docker-compose.searxng-only.yml up -d searxng (skipped in dry run)"
        SEARXNG_STATUS="dry run — compose files written, container not started"
        return 0
    fi
    (cd "$INSTALL_DIR" && $compose_cmd -f docker-compose.yml -f docker-compose.searxng-only.yml up -d searxng) \
        || { warn "Failed to start SearXNG — web search will fall back to Wikipedia."; SEARXNG_STATUS="failed to start (web search falls back to Wikipedia)"; return 0; }
    (cd "$INSTALL_DIR" && $compose_cmd -f docker-compose.yml -f docker-compose.searxng-only.yml restart searxng) >/dev/null 2>&1 || true
    sleep 3
    if curl -sS -m 5 "http://127.0.0.1:8080/search?q=test&format=json" >/dev/null 2>&1; then
        say "SearXNG is up at http://127.0.0.1:8080."
        SEARXNG_STATUS="running at http://127.0.0.1:8080"
    else
        warn "SearXNG started but did not answer yet — give it a few seconds; web search falls back to Wikipedia until it does."
        SEARXNG_STATUS="started, not answering yet (web search falls back to Wikipedia)"
    fi
}

# ---------------------------------------------------------------- finish

finish() {
    say ""
    local active="unknown"
    if [[ -n "${VORTEX_DRY_RUN:-}" ]]; then
        active="not checked (dry run)"
    elif [[ "${SYSTEMD_MODE:-}" == "user" ]]; then
        systemctl --user is-active --quiet "$SERVICE_NAME" && active="active" || active="NOT active — check: systemctl --user status $SERVICE_NAME"
    elif [[ "${SYSTEMD_MODE:-}" == "system" ]]; then
        if [[ $EUID -eq 0 ]]; then
            systemctl is-active --quiet "$SERVICE_NAME" && active="active" || active="NOT active — check: systemctl status $SERVICE_NAME"
        else
            sudo systemctl is-active --quiet "$SERVICE_NAME" && active="active" || active="NOT active — check: systemctl status $SERVICE_NAME"
        fi
    fi

    say "================================================================"
    say "Vortex installed."
    say "================================================================"
    say "  Install dir : $INSTALL_DIR"
    say "  Service     : $SERVICE_NAME ($active)"
    say "  Bot         : $BOT_NAME — country $COUNTRY_NAME, language $BOT_LANGUAGE"
    say "  LLM         : $LLM_PROVIDER_NAME — $LLM_MODEL"
    say "  SearXNG     : ${SEARXNG_STATUS:-unknown}"
    say ""
    say "Logs:"
    if [[ "${SYSTEMD_MODE:-}" == "user" ]]; then
        say "  journalctl --user -u $SERVICE_NAME -f"
    else
        say "  journalctl -u $SERVICE_NAME -f"
    fi
    say ""
    say "Open Telegram, message your bot (@${TG_USERNAME:-your bot}) and send /admin"
    say "to open the hidden admin panel."
    say ""
    say "Updates are automatic: once a day the bot checks for a new release"
    say "and asks you in private chat whether to update."
    say "================================================================"
}

main() {
    say "Vortex Telegram Bot — installer"
    say "================================"
    check_prereqs
    ask_country
    ask_language
    ask_token
    ask_boss_id
    ask_bot_name
    ask_llm
    ask_install_dir
    clone_repo
    install_deps
    write_env
    setup_systemd
    setup_searxng
    finish
    exit 0
}

# When sourced (VORTEX_INSTALLER_LIB=1) only the functions above are
# defined, so tests can call them directly without running main().
if [[ "${VORTEX_INSTALLER_LIB:-}" != "1" ]]; then
    main "$@"
fi
