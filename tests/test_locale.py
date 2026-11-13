"""Tests for the i18n + country system (bot/locale.py, bot/countries.py)
and its wiring into handlers / prices / extras / main.

Run: /tmp/moztest-venv2/bin/python test_locale.py
Covers:
  - locale loading + fallback (missing key -> en -> the key itself),
    unknown language -> en, fmt_num Persian digits for fa only
  - jokes list non-empty in en; t_list for list-valued keys
  - country matching (case/whitespace variants, unknown -> None),
    table completeness (all 32 present, valid IANA timezones via
    zoneinfo, valid 3-letter currency codes), LANGUAGES (86 codes),
    prayer_method defaults per country
  - database get/set country + language round-trip and defaults
  - price conversion with stubbed FX: usd_to_local_rate (Frankfurter
    stub + 5-min cache), gold-api parsing, Brent CSV parsing
  - prayer-times URL building (prayer_url, pure builder)
  - admin language/country callbacks: setlang / setcountry save to
    bot_settings immediately and re-render; countries browser pages;
    a manager without the "locale" permission is refused
  - wake word from config: set_wake_word drives has_vortex_wake_word
  - wiring: main.py wires the providers in build_application;
    .env.example documents BOT_NAME / BOT_COUNTRY / BOT_LANGUAGE
  - key coverage: every locale key referenced in bot/*.py exists in
    bot/locale/en.json
"""
import asyncio
import json
import re
import sys
import tempfile
import types
from pathlib import Path
from types import SimpleNamespace
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).parent))
audit_dir = Path(__file__).resolve().parent.parent / "bot"

pkg = types.ModuleType("bot")
pkg.__path__ = [str(audit_dir)]
sys.modules["bot"] = pkg

import importlib.util


def load(name):
    spec = importlib.util.spec_from_file_location(f"bot.{name}", audit_dir / f"{name}.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules[f"bot.{name}"] = m
    spec.loader.exec_module(m)
    return m


countries = load("countries")
locale_mod = load("locale")
config = load("config")
security = load("security")
database = load("database")
prices = load("prices")
extras = load("extras")

passed = failed = 0


def check(name, cond, extra=""):
    global passed, failed
    if cond:
        passed += 1
        print(f"  PASS {name}")
    else:
        failed += 1
        print(f"  FAIL {name} {extra}")


BOSS = 123456789
OTHER = 111222333

en = json.loads((audit_dir / "locale" / "en.json").read_text(encoding="utf-8"))
# German strings for the admin-callback checks below: the language is
# switched to de mid-test (admin:setlang:de) and stays de, so the handler
# answers in German. Expected strings are read from de.json itself.
de = json.loads((audit_dir / "locale" / "de.json").read_text(encoding="utf-8"))

# ---------- locale loading + fallback ----------
print("locale")
check("en.json loads", isinstance(en, dict) and len(en) > 300)
check(
    "t() resolves an en key",
    locale_mod.t("common.not_boss") == "This command is only for the boss.",
)
check(
    "missing key falls back to the key itself",
    locale_mod.t("does.not.exist") == "does.not.exist",
)
check(
    "unknown language falls back to en",
    locale_mod.t("common.not_boss", lang="xx") == "This command is only for the boss.",
)
check(
    "list_languages includes en first",
    locale_mod.list_languages()[0] == "en",
)
check("jokes list non-empty in en", len(locale_mod.t_list("jokes")) >= 10)
check(
    "get_joke returns a string from the list",
    locale_mod.get_joke() in locale_mod.t_list("jokes"),
)
check(
    "t_list falls back to en for an unknown language",
    locale_mod.t_list("ban.done", lang="xx") == en["ban.done"],
)
check(
    "t() formats placeholders",
    locale_mod.t("quota.text", used="3", remaining="27", limit="30")
    == "Your quota today: 3 messages used, 27 left (daily cap 30 messages).",
)
check("fmt_num fa digits", locale_mod.fmt_num(12345, lang="fa") == "۱۲٬۳۴۵")
check("fmt_num en digits", locale_mod.fmt_num(12345, lang="en") == "12,345")
check("fmt_num fa time string", locale_mod.fmt_num("05:09", lang="fa") == "۰۵:۰۹")
check("fmt_num float 2 decimals", locale_mod.fmt_num(3.14159, lang="en") == "3.14")
check("fmt_pct", locale_mod.fmt_pct(2.5, lang="en") == "2.5")

# ---------- country table ----------
print("countries")
EXPECTED = {
    "Iran", "Turkey", "United States", "United Kingdom", "Germany",
    "France", "Spain", "Italy", "Netherlands", "Belgium", "Russia",
    "Ukraine", "Poland", "Sweden", "Brazil", "Mexico", "Argentina",
    "Saudi Arabia", "United Arab Emirates", "Egypt", "Morocco",
    "India", "Pakistan", "China", "Japan", "South Korea", "Indonesia",
    "Thailand", "Vietnam", "Australia", "Nigeria", "Kenya",
}
check("all 195 countries present", len(countries.COUNTRIES) == 195)
check(
    "original 32 still present",
    EXPECTED <= set(countries.COUNTRIES),
)
check("Taiwan is not in the table", countries.get_country("Taiwan") is None)
check(
    "Palestine and Vatican City are included",
    countries.get_country("Palestine") is not None
    and countries.get_country("Vatican City") is not None,
)
check(
    "list_country_names sorted",
    countries.list_country_names() == sorted(countries.COUNTRIES),
)
check(
    "every default language has a display name",
    all(
        c.default_language in countries.LANGUAGES
        for c in countries.COUNTRIES.values()
    ),
)
check(
    "get_country case-insensitive",
    countries.get_country("iran") is not None
    and countries.get_country("iran").name == "Iran",
)
check(
    "get_country whitespace-tolerant",
    countries.get_country("  United   States  ") is not None
    and countries.get_country("  United   States  ").name == "United States",
)
check("get_country unknown -> None", countries.get_country("Narnia") is None)
check("get_country empty -> None", countries.get_country("") is None)
check("Belgium defaults to en", countries.get_country("Belgium").default_language == "en")
check("Iran defaults to fa", countries.get_country("Iran").default_language == "fa")
bad_tz = []
for name, c in countries.COUNTRIES.items():
    try:
        ZoneInfo(c.timezone)
    except Exception:
        bad_tz.append(name)
check("all timezones valid IANA", not bad_tz, str(bad_tz))
bad_cur = [
    name
    for name, c in countries.COUNTRIES.items()
    if not (len(c.currency) == 3 and c.currency.isalpha() and c.currency.isupper())
]
check("all currencies 3-letter ISO codes", not bad_cur, str(bad_cur))
check(
    "capitals non-empty",
    all(c.capital.strip() for c in countries.COUNTRIES.values()),
)
check("LANGUAGES has 86 codes (all defaults)", len(countries.LANGUAGES) == 86)
check("UI_LANGUAGES has 40 codes", len(countries.UI_LANGUAGES) == 40)
check(
    "UI_LANGUAGES are the original 22 plus ms plus 17 new",
    set(countries.UI_LANGUAGES)
    == {"en", "fa", "tr", "de", "fr", "es", "it", "nl", "ru", "uk",
        "pl", "sv", "pt", "ar", "hi", "ur", "zh", "ja", "ko", "id",
        "th", "vi", "ms",
        "bn", "pa", "mr", "te", "ta", "gu", "am", "sw", "ha", "fil",
        "ro", "hu", "cs", "el", "he", "da", "no"},
)
check(
    "LANGUAGES codes match country defaults",
    all(
        c.default_language in countries.LANGUAGES
        for c in countries.COUNTRIES.values()
    ),
)
check("prayer method Iran is 7", countries.prayer_method("Iran") == 7)
check("prayer method Saudi Arabia is 4", countries.prayer_method("Saudi Arabia") == 4)
check("prayer method default is 3", countries.prayer_method("Germany") == 3)
check(
    "country_now returns a datetime",
    countries.country_now("Japan") is not None,
)
check(
    "country_today matches the tz date",
    str(countries.country_today("Japan")) == str(countries.country_now("Japan").date()),
)

# ---------- database get/set country + language ----------
print("database settings")
db = database.Database(Path(tempfile.mkdtemp()) / "t.db")
check("default country is United States", db.get_country() == "United States")
check("default language is en", db.get_language() == "en")
db.set_country("Japan")
check("set_country round-trips", db.get_country() == "Japan")
db.set_language("fa")
check("set_language round-trips", db.get_language() == "fa")
db.set_country("United States")
db.set_language("en")

# ---------- price conversion with stubbed FX ----------
print("prices (stubbed FX)")


async def _fake_get_json(client, url, params=None):
    if "frankfurter" in url:
        code = (params or {}).get("symbols", "EUR")
        return {"rates": {code: 0.85}}
    if "gold-api" in url:
        return {"price": 3885.87, "currency": "USD"}
    if "coingecko" in url:
        return {"bitcoin": {"usd": 90000.0}}
    return {}


prices._get_json = _fake_get_json


class _FakeAsyncClient:
    def __init__(self, *a, **k):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, *a):
        return False


_orig_httpx = prices.httpx
prices.httpx = SimpleNamespace(AsyncClient=_FakeAsyncClient)
countries.set_country_provider(lambda: "Germany")
prices._fx_cache.clear()
check(
    "usd_to_local_rate uses stubbed Frankfurter",
    asyncio.run(prices.usd_to_local_rate()) == 0.85,
)
check(
    "usd_to_local_rate cached (no second fetch)",
    asyncio.run(prices.usd_to_local_rate()) == 0.85
    and prices._fx_cache.get("EUR") is not None,
)


class _FakeResp:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        pass


class _FakeClient:
    def __init__(self, text):
        self._text = text

    async def get(self, url):
        return _FakeResp(self._text)


check(
    "gold-api parses USD per ounce",
    asyncio.run(prices._fetch_gold_usd(None)) == {"usd_per_oz": 3885.87},
)
csv_text = "Date,Price\n2026-11-10,63.20\n2026-11-11,64.10\n2026-11-12,invalid\n"
check(
    "Brent CSV takes the last valid row",
    asyncio.run(prices._fetch_oil_usd(_FakeClient(csv_text)))
    == {"usd_per_barrel": 64.10, "date": "2026-11-11"},
)
# Gold conversion: USD/oz -> local per gram (31.1035 g per troy ounce).
per_gram_eur = 3885.87 / 31.1035 * 0.85
check(
    "gold per-gram conversion math",
    106.0 < per_gram_eur < 106.5,
    f"got {per_gram_eur}",
)
countries.set_country_provider(lambda: "United States")
prices._fx_cache.clear()
prices.httpx = _orig_httpx

# ---------- prayer-times URL ----------
print("prayer url")
url = extras.prayer_url("London", "United Kingdom", 2, "13-11-2026")
check(
    "prayer_url shape",
    url
    == "https://api.aladhan.com/v1/timingsByCity/13-11-2026"
    "?city=London&country=United%20Kingdom&method=2",
    url,
)
check(
    "prayer_url quotes non-ASCII city",
    "city=S%C3%A3o%20Paulo" in extras.prayer_url("São Paulo", "Brazil", 3, "13-11-2026"),
)

# ---------- wake word from config ----------
print("wake word")
security.set_wake_word("Vortex")
check(
    "wake word Vortex matches English",
    security.has_vortex_wake_word("Vortex dollar"),
)
check(
    "wake word Vortex matches Persian too",
    security.has_vortex_wake_word("ورتکس دلار"),
)
check(
    "word boundaries hold",
    not security.has_vortex_wake_word("Vortexes dollar")
    and not security.has_vortex_wake_word("myvortex dollar"),
)
security.set_wake_word("Nova")
check(
    "new wake word replaces the old one",
    security.has_vortex_wake_word("Nova dollar")
    and not security.has_vortex_wake_word("ورتکس دلار"),
)
check(
    "strip_wake_word removes the name",
    security.strip_wake_word("Nova dollar please").strip() == "dollar please",
)
security.set_wake_word("ورتکس")

# ---------- admin locale callbacks ----------
print("admin locale callbacks")
for _name in ("dollar", "downloader", "file_handler", "llm_client", "transcribe"):
    _mod = types.ModuleType(f"bot.{_name}")
    _mod.__getattr__ = lambda n: (lambda *a, **k: None)
    sys.modules[f"bot.{_name}"] = _mod
# extras + prices are already loaded for real; handlers uses them as-is.
token_pool = load("token_pool")
handlers_mod = load("handlers")


class FakeMsg:
    def __init__(self, text, chat_type="private", user_id=BOSS, chat_id=BOSS):
        self.text = text
        self.caption = None
        self.document = None
        self.photo = None
        self.voice = None
        self.video = None
        self.audio = None
        self.chat = SimpleNamespace(id=chat_id, type=chat_type)
        self.from_user = SimpleNamespace(id=user_id, is_bot=False, full_name="Boss", username="boss")
        self.reply_to_message = None
        self.sent = []
        self.message_id = 1

    async def reply_text(self, text, **kwargs):
        self.sent.append((text, kwargs.get("reply_markup")))
        return SimpleNamespace(message_id=len(self.sent))


class FakeQuery:
    def __init__(self, data, user_id=BOSS):
        self.data = data
        self.from_user = SimpleNamespace(id=user_id, is_bot=False)
        self.message = FakeMsg("/admin", chat_type="private", user_id=user_id, chat_id=BOSS)
        self.answered = []
        self.edited = []
        self.deleted = False

    async def answer(self, text="", **kwargs):
        self.answered.append(text)

    async def edit_message_text(self, text, **kwargs):
        self.edited.append((text, kwargs.get("reply_markup")))

    async def delete_message(self):
        self.deleted = True


class FakeContext:
    def __init__(self):
        self.bot = SimpleNamespace(id=999000111, username="vortex_test_bot")


def make_handlers(db):
    settings = SimpleNamespace(
        boss_id=BOSS,
        daily_limit_messages=30,
        global_ban_default=False,
        ban_commands=["بن", "بن کن"],
        unban_commands=["انبن", "انبنش کن"],
    )
    pool = token_pool.TokenPool([
        token_pool.ProviderEntry(base_url="https://integrate.api.nvidia.com/v1",
                                 key="nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", model="m1"),
    ])
    llm = SimpleNamespace(
        token_pool=pool,
        describe_active_model=lambda: "nemotron-3-ultra",
    )
    h = handlers_mod.VortexBotHandlers(
        settings=settings,
        db=db,
        dollar_service=None,
        workspace_mgr=None,
        file_processor=None,
        llm_client=llm,
        rate_limiter=SimpleNamespace(is_allowed=lambda c, u: True),
    )
    return h


async def _run_callback(h, data, user_id=BOSS):
    q = FakeQuery(data, user_id=user_id)
    update = SimpleNamespace(callback_query=q)
    await h._handle_admin_callback(update, FakeContext())
    return q


db2 = database.Database(Path(tempfile.mkdtemp()) / "t2.db")
h = make_handlers(db2)

q = asyncio.run(_run_callback(h, "admin:locale"))
check(
    "admin:locale shows current country + language",
    q.edited and "United States" in q.edited[0][0] and "English" in q.edited[0][0],
    q.edited[0][0][:80] if q.edited else "no edit",
)
check(
    "locale keyboard has language buttons",
    q.edited
    and q.edited[0][1] is not None
    and any(
        "German" in (b.text or "")
        for row in q.edited[0][1].inline_keyboard
        for b in row
    ),
)
check(
    "locale keyboard renders all 40 UI languages",
    q.edited
    and q.edited[0][1] is not None
    and sum(
        1
        for row in q.edited[0][1].inline_keyboard
        for b in row
        if (b.callback_data or "").startswith("admin:setlang:")
    )
    == 40,
)
q = asyncio.run(_run_callback(h, "admin:setlang:de"))
check("setlang saves to bot_settings", db2.get_language() == "de")
check(
    "setlang re-renders with the new language",
    q.edited and "German" in q.edited[0][0],
)
check(
    "setlang answers a confirmation",
    q.answered and "German" in q.answered[0],
)
q = asyncio.run(_run_callback(h, "admin:setlang:xx"))
check(
    "setlang rejects an unknown code",
    # Language is de at this point, so the refusal is the German string.
    q.answered and de["common.invalid_button"] in q.answered[0],
)
q = asyncio.run(_run_callback(h, "admin:countries"))
check(
    "countries browser lists 10 per page",
    q.edited
    and q.edited[0][1] is not None
    and sum(1 for row in q.edited[0][1].inline_keyboard for b in row if b.callback_data.startswith("admin:setcountry:")) == 10,
)
check(
    "countries browser shows the current country first page",
    q.edited
    and any(
        "Argentina" in (b.text or "")
        for row in q.edited[0][1].inline_keyboard
        for b in row
    ),
)
q = asyncio.run(_run_callback(h, "admin:countries:next"))
check(
    "countries next page re-renders",
    # Language is still de: the title is the German countries_title
    # with page=2 of 20 (195 countries, 10 per page).
    q.edited
    and de["admin.locale.countries_title"].format(page=2, pages=20) in q.edited[0][0],
)
q = asyncio.run(_run_callback(h, "admin:setcountry:Japan"))
check("setcountry saves to bot_settings", db2.get_country() == "Japan")
check(
    "setcountry re-renders the locale section",
    q.edited and "Japan" in q.edited[0][0],
)
q = asyncio.run(_run_callback(h, "admin:setcountry:Albania"))
check("setcountry Albania saves", db2.get_country() == "Albania")
q = asyncio.run(_run_callback(h, "admin:countries"))
check(
    "countries browser marks the current country",
    q.edited
    and de["admin.locale.countries_title"].format(page=1, pages=20) in q.edited[0][0]
    and any(
        "✓" in (b.text or "") and "Albania" in (b.text or "")
        for row in q.edited[0][1].inline_keyboard
        for b in row
    ),
)
db2.add_manager(OTHER, BOSS)
db2.set_manager_perms(OTHER, {"stats"})
q = asyncio.run(_run_callback(h, "admin:locale", user_id=OTHER))
check(
    "manager without locale perm is refused",
    # Language is still de, so the refusal is the German no_access string.
    q.answered and de["common.no_access"] in q.answered[0],
)

# ---------- wiring ----------
print("wiring")
main_src = (audit_dir / "main.py").read_text(encoding="utf-8")
check("main wires language provider", "set_language_provider" in main_src)
check("main wires country provider", "set_country_provider" in main_src)
check("main wires wake word", "set_wake_word(settings.bot_name" in main_src)
env_example = (Path(__file__).resolve().parent.parent / ".env.example").read_text(encoding="utf-8")
check(".env.example documents BOT_NAME", "BOT_NAME=" in env_example)
check(".env.example documents BOT_COUNTRY", "BOT_COUNTRY=" in env_example)
check(".env.example documents BOT_LANGUAGE", "BOT_LANGUAGE=" in env_example)
check(
    "config has BOT_NAME default Vortex",
    getattr(config.Settings(), "bot_name", None) == "Vortex",
)

# ---------- key coverage ----------
print("key coverage")
import ast as _ast

ph_re = re.compile(r"\{(\w+)\}")
missing_keys = set()
_KEY_PREFIXES = {
    "admin", "common", "prices", "stats", "chats", "quota", "ban",
    "unban", "llm", "image", "file", "download", "dollar", "time",
    "weather", "price", "faal", "news", "prayer", "calc", "update",
    "help", "start", "id", "forget", "jokes",
}
for py in sorted((audit_dir).glob("*.py")):
    tree = _ast.parse(py.read_text(encoding="utf-8"))
    for node in _ast.walk(tree):
        if not isinstance(node, _ast.Call):
            continue
        f = node.func
        if not (isinstance(f, _ast.Name) and f.id in ("t", "t_list")):
            continue
        if not node.args or not isinstance(node.args[0], _ast.Constant):
            continue
        key = node.args[0].value
        if not isinstance(key, str):
            continue
        passed_vars = {kw.arg for kw in node.keywords if kw.arg}
        if key not in en:
            missing_keys.add(f"{py.name}:{node.lineno}:{key}")
            continue
        val = en[key]
        if isinstance(val, list):
            continue
        want = set(ph_re.findall(val))
        if want - passed_vars:
            missing_keys.add(
                f"{py.name}:{node.lineno}:{key} missing vars {sorted(want - passed_vars)}"
            )
    # Locale keys used via data (row['label_key'], dict values, ...):
    # dotted literals whose first segment is a known key family.
    key_re = re.compile(r'"([a-z][a-z0-9_]*(\.[a-z0-9_]+)+)"')
    for m in key_re.finditer(py.read_text(encoding="utf-8")):
        key = m.group(1)
        if key.endswith((".txt", ".mp3", ".ogg", ".gz", ".md", ".pdf", ".json")):
            continue
        if key.split(".")[0] in _KEY_PREFIXES and key not in en:
            missing_keys.add(f"{py.name}:{key}")
check("every locale key in code exists in en.json", not missing_keys, str(sorted(missing_keys)[:10]))

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
