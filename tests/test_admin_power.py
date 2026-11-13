"""Tests for /admin power (/on /off + allowlist), managers, image-model
selection and the 'no model' pick (2026-11-13).

Run: /tmp/moztest-venv2/bin/python test_admin_power.py
Covers:
  - DB: bot_settings get/set/delete, bot_enabled, image_model, allowlist
    CRUD, managers CRUD + perms
  - TokenPool.set_pinned_model + config.write_llm_pinned_model
  - Handlers: /on / /off (boss + power-manager, refused otherwise),
    /admin for managers (filtered menu, no-perm refusal), private mode
    (PV refusal, group silence, allowlisted/manager/boss pass, /on//off
    exempt), power toggle button, allowlist add/remove via panel,
    managers section (add -> detail -> toggle perm -> remove),
    manager permission enforcement on callbacks, image section
    (duckai/none/HiLinkUp models fetch + pick), 'no model' pick
  - LLMClient.generate_image honoring the image-model choice
"""
import asyncio
import base64
import os
import sys
import tempfile
import types
from pathlib import Path
from types import SimpleNamespace

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


for _name in ("dollar", "downloader", "extras", "file_handler",
              "prices", "transcribe"):
    _mod = types.ModuleType(f"bot.{_name}")
    _mod.__getattr__ = lambda n: (lambda *a, **k: None)
    sys.modules[f"bot.{_name}"] = _mod

config = load("config")
security = load("security")
token_pool = load("token_pool")
database = load("database")
llm_client_mod = load("llm_client")
handlers_mod = load("handlers")

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
MGR = 222333444
MGR2 = 555666777
USER1 = 888999000
NV = "https://integrate.api.nvidia.com/v1"
TH = "https://tokenharbor.ai/v1"
HL = "https://api.hilinkup.com/v1"

# ---------- DB ----------
print("db settings / allowlist / managers")
db = database.Database(Path(tempfile.mkdtemp()) / "t.db")
check("setting default None", db.get_setting("nope") is None)
db.set_setting("k", "v")
check("setting set/get", db.get_setting("k") == "v")
db.set_setting("k", "v2")
check("setting overwrite", db.get_setting("k") == "v2")
db.delete_setting("k")
check("setting deleted", db.get_setting("k") is None)
check("bot enabled by default", db.is_bot_enabled() is True)
db.set_bot_enabled(False)
check("bot disabled", db.is_bot_enabled() is False)
db.set_bot_enabled(True)
check("bot re-enabled", db.is_bot_enabled() is True)
check("image model default duckai", db.get_image_model() == "duckai")
db.set_image_model("hilinkup:qwen-image-3.0-pro")
check("image model set", db.get_image_model() == "hilinkup:qwen-image-3.0-pro")
db.set_image_model("duckai")
check("allowlist add", db.add_to_allowlist(USER1, BOSS) is True)
check("allowlist add dup", db.add_to_allowlist(USER1, BOSS) is False)
check("allowlist is", db.is_user_allowlisted(USER1) is True)
check("allowlist list", len(db.list_allowlist()) == 1)
check("allowlist remove", db.remove_from_allowlist(USER1) is True)
check("allowlist remove again", db.remove_from_allowlist(USER1) is False)
check("allowlist gone", db.is_user_allowlisted(USER1) is False)
check("manager add", db.add_manager(MGR, BOSS) is True)
check("manager add dup", db.add_manager(MGR, BOSS) is False)
check("manager is", db.is_manager(MGR) is True)
check("manager perms empty", db.get_manager_perms(MGR) == set())
check("manager set perms", db.set_manager_perms(MGR, {"stats", "power"}) is True)
check("manager perms read", db.get_manager_perms(MGR) == {"stats", "power"})
check("manager list", len(db.list_managers()) == 1)
check("manager remove", db.remove_manager(MGR) is True)
check("manager gone", db.is_manager(MGR) is False)
check("manager perms of non-manager", db.get_manager_perms(MGR) == set())

# ---------- pool set_pinned_model + config write_llm_pinned_model ----------
print("pinned model")


async def test_pinned():
    pool = token_pool.TokenPool([
        token_pool.ProviderEntry(base_url=NV, key="nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", model="m-nv"),
        token_pool.ProviderEntry(base_url=TH, key="thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", model="m-th"),
    ], pinned_model="m-nv")
    check("pinned active", pool.active_entry.model == "m-nv")
    await pool.set_pinned_model("m-th")
    check("set pinned switches active", pool.active_entry.model == "m-th")
    await pool.set_pinned_model("")
    check("clear pinned -> free rotation", pool.active_entry.model in ("m-nv", "m-th"))


asyncio.run(test_pinned())
tmpdir = Path(tempfile.mkdtemp())
env_path = tmpdir / ".env"
env_path.write_text("BOT_TOKEN=xxx\nLLM_PINNED_MODEL=m-nv\nOTHER=1\n", encoding="utf-8")
config.write_llm_pinned_model(env_path, "m-th")
check("pinned line replaced", "LLM_PINNED_MODEL=m-th" in env_path.read_text(encoding="utf-8"))
config.write_llm_pinned_model(env_path, "")
check("pinned line cleared", "LLM_PINNED_MODEL=" not in env_path.read_text(encoding="utf-8"))
check("other lines kept", "BOT_TOKEN=xxx" in env_path.read_text(encoding="utf-8"))

# ---------- handlers ----------
print("handlers power / private / managers / image")


class FakeBot:
    def __init__(self):
        self.id = 999000111
        self.username = "vortex_test_bot"


class FakeMsg:
    def __init__(self, text, chat_type="private", user_id=BOSS, chat_id=BOSS, reply_to=None):
        self.text = text
        self.caption = None
        self.document = None
        self.photo = None
        self.voice = None
        self.video = None
        self.audio = None
        self.chat = SimpleNamespace(id=chat_id, type=chat_type)
        self.from_user = SimpleNamespace(id=user_id, is_bot=False, full_name="U", username="u")
        self.reply_to_message = reply_to
        self.sent = []
        self.message_id = 1
        self.deleted = False

    async def reply_text(self, text, **kwargs):
        self.sent.append((text, kwargs.get("reply_markup")))
        return SimpleNamespace(message_id=len(self.sent))

    async def delete(self):
        self.deleted = True


class FakeQuery:
    def __init__(self, data, user_id=BOSS, message=None):
        self.data = data
        self.from_user = SimpleNamespace(id=user_id, is_bot=False)
        self.message = message or FakeMsg("/admin", chat_type="private", user_id=user_id, chat_id=BOSS)
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
    def __init__(self, bot):
        self.bot = bot


def make_handlers(db, pool, env):
    settings = SimpleNamespace(
        boss_id=BOSS, daily_limit_messages=30,
        global_ban_default=False, ban_commands=["بن"], unban_commands=["انبن"],
    )
    llm = SimpleNamespace(token_pool=pool, describe_active_model=lambda: pool.active_entry.model)
    h = handlers_mod.VortexBotHandlers(
        settings=settings, db=db, dollar_service=None, workspace_mgr=None,
        file_processor=None, llm_client=llm,
        rate_limiter=SimpleNamespace(is_allowed=lambda c, u: True),
    )
    return h


def make_pool():
    return token_pool.TokenPool([
        token_pool.ProviderEntry(base_url=NV, key="nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", model="nvidia/nemotron-3-ultra-550b-a55b"),
        token_pool.ProviderEntry(base_url=TH, key="thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", model="deepseek-v4-flash:free"),
        token_pool.ProviderEntry(base_url=HL, key="hlk_cccccccccccccccccccccccccccccccc", model="kimi-k3.1-pro"),
    ], pinned_model="nvidia/nemotron-3-ultra-550b-a55b")


async def run_flows():
    bot = FakeBot()
    ctx = FakeContext(bot)
    db2 = database.Database(Path(tempfile.mkdtemp()) / "t2.db")
    pool = make_pool()
    env = Path(tempfile.mkdtemp()) / ".env"
    env.write_text(
        "LLM_PROVIDERS=https://integrate.api.nvidia.com/v1|nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa|nvidia/nemotron-3-ultra-550b-a55b,https://tokenharbor.ai/v1|thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb|deepseek-v4-flash:free,https://api.hilinkup.com/v1|hlk_cccccccccccccccccccccccccccccccc|kimi-k3.1-pro\nLLM_PINNED_MODEL=nvidia/nemotron-3-ultra-550b-a55b\n",
        encoding="utf-8")
    os.environ["VORTEX_BOT_ENV"] = str(env)
    h = make_handlers(db2, pool, env)

    def msg(text, user_id=BOSS, chat_type="private", chat_id=BOSS):
        m = FakeMsg(text, chat_type=chat_type, user_id=user_id, chat_id=chat_id)
        return m, SimpleNamespace(effective_message=m, effective_chat=m.chat,
                                   effective_user=m.from_user, callback_query=None)

    # --- /off and /on (boss) ---
    m, upd = msg("/off")
    await h.handle_message(upd, ctx)
    check("/off disables", db2.is_bot_enabled() is False)
    check("/off confirms", m.sent and "allowlisted users only" in m.sent[0][0])
    m, upd = msg("/on")
    await h.handle_message(upd, ctx)
    check("/on enables", db2.is_bot_enabled() is True)
    check("/on confirms", m.sent and "on for everyone" in m.sent[0][0])

    # --- /off by a non-boss -> refused ---
    m, upd = msg("/off", user_id=USER1)
    await h.handle_message(upd, ctx)
    check("/off by non-boss refused", db2.is_bot_enabled() is True
          and m.sent and "only for the boss" in m.sent[0][0])

    # --- private mode: non-allowed user in PV gets refusal, in group silence ---
    db2.set_bot_enabled(False)
    m, upd = msg("سلام", user_id=USER1, chat_type="private", chat_id=USER1)
    await h.handle_message(upd, ctx)
    check("private PV refusal", m.sent and "is off right now" in m.sent[0][0])
    m, upd = msg("ورتکس", user_id=USER1, chat_type="group", chat_id=-100123)
    await h.handle_message(upd, ctx)
    check("private group silence", m.sent == [])
    # allowlisted user passes (/start welcome)
    db2.add_to_allowlist(USER1, BOSS)
    m, upd = msg("/start", user_id=USER1, chat_type="private", chat_id=USER1)
    await h.handle_message(upd, ctx)
    check("allowlisted user passes", m.sent and "is off right now" not in m.sent[0][0])
    # /off still works for the boss in private mode (exempt)
    m, upd = msg("/on")
    await h.handle_message(upd, ctx)
    check("/on works in private mode", db2.is_bot_enabled() is True)
    db2.set_bot_enabled(False)

    # --- manager with power perm can /on and /off ---
    db2.add_manager(MGR, BOSS)
    db2.set_manager_perms(MGR, {"power"})
    m, upd = msg("/on", user_id=MGR, chat_type="private", chat_id=MGR)
    await h.handle_message(upd, ctx)
    check("power-manager /on works", db2.is_bot_enabled() is True)
    db2.set_bot_enabled(False)
    # manager without power perm cannot
    db2.set_manager_perms(MGR, {"stats"})
    m, upd = msg("/on", user_id=MGR, chat_type="private", chat_id=MGR)
    await h.handle_message(upd, ctx)
    check("manager without power cannot /on", db2.is_bot_enabled() is False
          and m.sent and "only for the boss" in m.sent[0][0])
    db2.set_bot_enabled(True)

    # --- /admin for managers: filtered menu ---
    db2.set_manager_perms(MGR, {"stats", "power"})
    m, upd = msg("/admin", user_id=MGR, chat_type="private", chat_id=MGR)
    await h.handle_message(upd, ctx)
    check("manager /admin opens", m.sent and m.sent[0][1] is not None)
    kb = m.sent[0][1]
    labels = [b.text for row in kb.inline_keyboard for b in row]
    check("manager menu has stats+power only",
          any("Stats" in t for t in labels) and any("Bot is on" in t or "Bot is off" in t for t in labels)
          and not any("Tokens" in t for t in labels) and not any("Managers" in t for t in labels))
    # manager with no perms -> refused
    db2.add_manager(MGR2, BOSS)
    m, upd = msg("/admin", user_id=MGR2, chat_type="private", chat_id=MGR2)
    await h.handle_message(upd, ctx)
    check("manager with no perms refused", m.sent and "permissions" in m.sent[0][0])
    # non-manager -> refused
    m, upd = msg("/admin", user_id=USER1, chat_type="private", chat_id=USER1)
    await h.handle_message(upd, ctx)
    check("non-manager /admin refused", m.sent and "only for the boss" in m.sent[0][0])
    db2.remove_manager(MGR2)

    # --- manager callback permission enforcement ---
    q = FakeQuery("admin:tokens", user_id=MGR)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("manager without tokens perm refused on tokens",
          q.answered and "don't have access" in q.answered[0] and not q.edited)
    q = FakeQuery("admin:stats", user_id=MGR)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("manager with stats perm can open stats", q.edited != [] or q.answered == [])

    # --- power toggle button ---
    db2.set_bot_enabled(True)
    q = FakeQuery("admin:power", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("power button turns off", db2.is_bot_enabled() is False)
    check("power button refreshes menu", q.edited and "Bot is off" in str(q.edited[0][1].inline_keyboard))
    q = FakeQuery("admin:power", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("power button turns on", db2.is_bot_enabled() is True)

    # --- allowlist via panel ---
    db2.remove_from_allowlist(USER1)
    q = FakeQuery("admin:allow", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("allow asks for id", q.edited and "numeric ID" in q.edited[0][0])
    m, upd = msg(str(USER1))
    await h.handle_message(upd, ctx)
    check("allowlist add via panel", db2.is_user_allowlisted(USER1) is True)
    q = FakeQuery("admin:unallow", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    m, upd = msg(str(USER1))
    await h.handle_message(upd, ctx)
    check("allowlist remove via panel", db2.is_user_allowlisted(USER1) is False)

    # --- managers section (boss) ---
    q = FakeQuery("admin:managers", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("managers list shown", q.edited and "Managers" in q.edited[0][0])
    q = FakeQuery("admin:mgradd", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    m, upd = msg(str(MGR2))
    await h.handle_message(upd, ctx)
    check("manager added via panel", db2.is_manager(MGR2) is True)
    check("detail view shown after add", m.sent and "Manager" in m.sent[-1][0])
    q = FakeQuery(f"admin:mgrtoggle:{MGR2}:tokens", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("perm toggled on", "tokens" in db2.get_manager_perms(MGR2))
    q = FakeQuery(f"admin:mgrtoggle:{MGR2}:tokens", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("perm toggled off", "tokens" not in db2.get_manager_perms(MGR2))
    q = FakeQuery(f"admin:mgrremove:{MGR2}", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("remove confirm shown", q.edited and "Remove manager" in q.edited[0][0])
    q = FakeQuery(f"admin:mgrremoveconfirm:{MGR2}", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("manager removed", db2.is_manager(MGR2) is False)
    # managers section is boss-only
    q = FakeQuery("admin:managers", user_id=MGR)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("managers section boss-only", q.answered and "only for the boss" in q.answered[0])

    # --- image section ---
    q = FakeQuery("admin:image", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("image view shows duckai", q.edited and "DuckAI" in q.edited[0][0])
    q = FakeQuery("admin:setimage:none", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("image set to none", db2.get_image_model() == "none")
    q = FakeQuery("admin:setimage:duckai", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("image set back to duckai", db2.get_image_model() == "duckai")
    # HiLinkUp image models (stubbed list_models)
    real_list = token_pool.TokenPool.list_models

    async def fake_list(base_url, key):
        return ["qwen-image-3.0", "qwen-image-3.0-pro", "some-chat-model", "aliyun/qwen-image-3.0-pro"]

    token_pool.TokenPool.list_models = staticmethod(fake_list)
    q = FakeQuery("admin:imagemodels", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("hilinkup image models listed", q.edited and "qwen-image-3.0-pro" in str(q.edited[0][1].inline_keyboard)
          and "some-chat-model" not in str(q.edited[0][1].inline_keyboard))
    q = FakeQuery("admin:setimage:hl:1", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("hilinkup image model picked", db2.get_image_model() == "hilinkup:qwen-image-3.0-pro")
    token_pool.TokenPool.list_models = real_list
    db2.set_image_model("duckai")

    # --- 'no model' pick ---
    q = FakeQuery("admin:setactive:none", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("no model clears manual+pinned",
          pool.manual_selection is None and pool._pinned_model == "")
    check("no model persisted",
          "LLM_MANUAL_SELECTION=" not in env.read_text(encoding="utf-8")
          and "LLM_PINNED_MODEL=" not in env.read_text(encoding="utf-8"))
    check("tokens view shows free rotation", q.edited and "free rotation" in q.edited[0][0])


asyncio.run(run_flows())

# ---------- LLMClient.generate_image honoring the choice ----------
print("llm generate_image choice")
import httpx as _httpx

_real_client = _httpx.AsyncClient


class FakeResp:
    def __init__(self, status, body=None):
        self.status_code = status
        self._body = body or {}

    def json(self):
        return self._body

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError("http error")

    @property
    def content(self):
        return b"img-bytes"


class FakeHLClient:
    """httpx client stub: POST /images/generations returns a b64 image."""

    def __init__(self, *a, **k):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, *a):
        return False

    async def post(self, url, headers=None, json=None):
        return FakeResp(200, {"data": [{"b64_json": base64.b64encode(b"hl-image").decode()}]})

    async def get(self, url, timeout=None):
        return FakeResp(200)


async def test_image_choice():
    db3 = database.Database(Path(tempfile.mkdtemp()) / "t3.db")
    settings = SimpleNamespace(
        llm_providers=[token_pool.ProviderEntry(base_url=NV, key="nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", model="m")],
        token_dead_path=None, llm_pinned_model="", llm_manual_selection="",
        hilinkup_api_key="hlk_test", hilinkup_base_url=HL,
        hilinkup_image_model="qwen-image-3.0",
        system_prompt_path=Path(tempfile.mkdtemp()) / "system_prompt.txt",
        bot_token="bot-token-test", llm_api_keys=[], search_api_key="",
        groq_api_key="", agy_enabled=False,
    )
    # LLMClient needs a web_toolkit stub and a workspace root; the tool
    # schemas come from the real modules.
    client = llm_client_mod.LLMClient(settings, db3, SimpleNamespace(), workspace_root=Path(tempfile.mkdtemp()))
    # 'none' -> disabled, DuckAI never called
    db3.set_image_model("none")
    duck_called = {"n": 0}

    async def fake_duckai(prompt):
        duck_called["n"] += 1
        return b"duck-image", None

    client.generate_image_duckai = fake_duckai
    out, err = await client.generate_image("a cat")
    check("image none -> disabled", (out, err) == (None, "disabled") and duck_called["n"] == 0)
    # 'hilinkup:model' -> HiLinkUp first (stubbed), DuckAI not called
    db3.set_image_model("hilinkup:qwen-image-3.0-pro")
    _httpx.AsyncClient = FakeHLClient
    out, err = await client.generate_image("a cat")
    check("image hilinkup model used", out == b"hl-image" and err is None and duck_called["n"] == 0)
    # 'duckai' -> DuckAI first
    db3.set_image_model("duckai")
    out, err = await client.generate_image("a cat")
    check("image duckai first", out == b"duck-image" and err is None and duck_called["n"] == 1)
    _httpx.AsyncClient = _real_client


asyncio.run(test_image_choice())
print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
