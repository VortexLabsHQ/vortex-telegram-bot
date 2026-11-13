"""Tests for /admin pick-active-key + browse-key-models (2026-11-13).

Run: /tmp/moztest-venv2/bin/python test_admin_select.py
Covers:
  - TokenPool manual selection: constructor, set/clear, pick_active priority
    (manual > pinned > random), fallback when the manual entry is unhealthy
  - TokenPool.list_models (stubbed httpx: parses ids, dedupes, [] on failure)
  - TokenPool.probe_model (stubbed httpx: True on 200+content, False on
    empty content / non-200 / exception)
  - config.write_llm_manual_selection (set / clear / append)
  - Handlers: pickkey list (⭐ on active), setactive (persist to .env),
    setactive:auto (clears), models keys list (distinct keys),
    models browser (filtering + pagination), model pick (live validation,
    add-when-new, activate), probe-fail -> force-activate, stale indices
"""
import asyncio
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


for _name in ("dollar", "downloader", "extras", "file_handler", "llm_client",
              "prices", "transcribe"):
    _mod = types.ModuleType(f"bot.{_name}")
    _mod.__getattr__ = lambda n: (lambda *a, **k: None)
    sys.modules[f"bot.{_name}"] = _mod

config = load("config")
security = load("security")
token_pool = load("token_pool")
database = load("database")
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
NV = "https://integrate.api.nvidia.com/v1"
TH = "https://tokenharbor.ai/v1"
HL = "https://api.hilinkup.com/v1"


def make_pool(**kw):
    return token_pool.TokenPool([
        token_pool.ProviderEntry(base_url=NV, key="nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", model="nvidia/nemotron-3-ultra-550b-a55b"),
        token_pool.ProviderEntry(base_url=TH, key="thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", model="deepseek-v4-flash:free"),
        token_pool.ProviderEntry(base_url=HL, key="hlk_cccccccccccccccccccccccccccccccc", model="kimi-k3.1-pro"),
    ], pinned_model="nvidia/nemotron-3-ultra-550b-a55b", **kw)


# ---------- manual selection (pool) ----------
print("manual selection")


async def test_manual():
    pool = make_pool()
    check("default active is pinned", pool.active_entry.model == "nvidia/nemotron-3-ultra-550b-a55b")
    # set manual to kimi
    active = await pool.set_manual_selection(HL, "kimi-k3.1-pro")
    check("set_manual returns the chosen entry", active is not None and active.model == "kimi-k3.1-pro")
    check("active is now kimi", pool.active_entry.model == "kimi-k3.1-pro")
    check("manual_selection property", pool.manual_selection == (HL, "kimi-k3.1-pro"))
    # pick_active prefers manual over pinned
    check("pick_active returns manual", pool.pick_active().model == "kimi-k3.1-pro")
    # clear -> back to pinned
    active2 = await pool.clear_manual_selection()
    check("clear returns pinned", active2 is not None and active2.model == "nvidia/nemotron-3-ultra-550b-a55b")
    check("manual cleared", pool.manual_selection is None)
    # constructor with manual selection
    pool2 = make_pool(manual_selection=f"{TH}|deepseek-v4-flash:free")
    check("constructor manual selection active", pool2.active_entry.model == "deepseek-v4-flash:free")
    # manual entry unhealthy -> falls back, but remembered
    pool3 = make_pool(manual_selection=f"{HL}|kimi-k3.1-pro")
    pool3._healthy.discard("hlk_cccccccccccccccccccccccccccccccc")
    check("unhealthy manual falls back", pool3.pick_active().model == "nvidia/nemotron-3-ultra-550b-a55b")
    check("manual still remembered", pool3.manual_selection == (HL, "kimi-k3.1-pro"))
    pool3._healthy.add("hlk_cccccccccccccccccccccccccccccccc")
    check("manual recovers when healthy again", pool3.pick_active().model == "kimi-k3.1-pro")
    # bad manual selection string ignored
    pool4 = make_pool(manual_selection="not-a-pair")
    check("bad manual string ignored", pool4.manual_selection is None)


asyncio.run(test_manual())

# ---------- list_models / probe_model (stubbed httpx) ----------
print("list_models / probe_model")
import httpx as _httpx

_real_client = _httpx.AsyncClient


class FakeResp:
    def __init__(self, status, body=None):
        self.status_code = status
        self._body = body or {}

    def json(self):
        return self._body


class FakeClient:
    def __init__(self, resp=None, exc=None):
        self.resp = resp
        self.exc = exc

    async def __aenter__(self):
        return self

    async def __aexit__(self, *a):
        return False

    async def get(self, url, headers=None):
        if self.exc:
            raise self.exc
        return self.resp

    async def post(self, url, headers=None, json=None):
        if self.exc:
            raise self.exc
        return self.resp


async def test_list_probe():
    _httpx.AsyncClient = lambda timeout=None: FakeClient(
        resp=FakeResp(200, {"data": [{"id": "a"}, {"id": "b"}, {"id": "a"}, {"id": ""}, {"id": "c"}]}))
    check("list_models parses + dedupes",
          await token_pool.TokenPool.list_models(NV, "k") == ["a", "b", "c"])
    _httpx.AsyncClient = lambda timeout=None: FakeClient(resp=FakeResp(401))
    check("list_models non-200 -> []", await token_pool.TokenPool.list_models(NV, "k") == [])
    _httpx.AsyncClient = lambda timeout=None: FakeClient(exc=RuntimeError("down"))
    check("list_models exception -> []", await token_pool.TokenPool.list_models(NV, "k") == [])
    _httpx.AsyncClient = lambda timeout=None: FakeClient(
        resp=FakeResp(200, {"choices": [{"message": {"content": "hi"}}]}))
    check("probe_model 200+content -> True",
          await token_pool.TokenPool.probe_model(NV, "k", "m") is True)
    _httpx.AsyncClient = lambda timeout=None: FakeClient(
        resp=FakeResp(200, {"choices": [{"message": {"content": "  "}}]}))
    check("probe_model empty content -> False",
          await token_pool.TokenPool.probe_model(NV, "k", "m") is False)
    _httpx.AsyncClient = lambda timeout=None: FakeClient(resp=FakeResp(404))
    check("probe_model 404 -> False",
          await token_pool.TokenPool.probe_model(NV, "k", "m") is False)
    _httpx.AsyncClient = lambda timeout=None: FakeClient(exc=RuntimeError("down"))
    check("probe_model exception -> False",
          await token_pool.TokenPool.probe_model(NV, "k", "m") is False)
    _httpx.AsyncClient = _real_client


asyncio.run(test_list_probe())

# ---------- config.write_llm_manual_selection ----------
print("write_llm_manual_selection")
tmpdir = Path(tempfile.mkdtemp())
env_path = tmpdir / ".env"
env_path.write_text("BOT_TOKEN=xxx\nLLM_PROVIDERS=a|b|c\nOTHER=1\n", encoding="utf-8")
config.write_llm_manual_selection(env_path, NV, "nvidia/nemotron-3-ultra-550b-a55b")
text = env_path.read_text(encoding="utf-8")
check("manual line set",
      f"LLM_MANUAL_SELECTION={NV}|nvidia/nemotron-3-ultra-550b-a55b" in text)
check("other lines preserved", "BOT_TOKEN=xxx" in text and "OTHER=1" in text)
check("no duplicate manual lines", text.count("LLM_MANUAL_SELECTION=") == 1)
config.write_llm_manual_selection(env_path, HL, "kimi-k3.1-pro")
check("manual line replaced",
      f"LLM_MANUAL_SELECTION={HL}|kimi-k3.1-pro" in env_path.read_text(encoding="utf-8")
      and env_path.read_text(encoding="utf-8").count("LLM_MANUAL_SELECTION=") == 1)
config.write_llm_manual_selection(env_path, "", "")
check("manual line cleared", "LLM_MANUAL_SELECTION=" not in env_path.read_text(encoding="utf-8"))

# ---------- handlers: pick + models ----------
print("handlers pick + models")


class FakeBot:
    def __init__(self):
        self.id = 999000111
        self.username = "vortex_test_bot"


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


async def run_flows():
    bot = FakeBot()
    ctx = FakeContext(bot)
    db = database.Database(Path(tempfile.mkdtemp()) / "t.db")
    pool = make_pool()
    env = Path(tempfile.mkdtemp()) / ".env"
    env.write_text(
        "LLM_PROVIDERS=https://integrate.api.nvidia.com/v1|nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa|nvidia/nemotron-3-ultra-550b-a55b,https://tokenharbor.ai/v1|thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb|deepseek-v4-flash:free,https://api.hilinkup.com/v1|hlk_cccccccccccccccccccccccccccccccc|kimi-k3.1-pro\n",
        encoding="utf-8")
    os.environ["VORTEX_BOT_ENV"] = str(env)
    h = make_handlers(db, pool, env)

    # stub list_models / probe_model
    real_list = token_pool.TokenPool.list_models
    real_probe = token_pool.TokenPool.probe_model

    async def fake_list(base_url, key):
        return ["good-chat-a", "bad-image-b", "good-embed-c", "good-chat-d",
                "good-chat-e", "good-chat-f", "good-chat-g", "good-chat-h",
                "good-chat-i", "good-chat-j", "good-chat-k", "good-chat-l"]

    async def fake_probe(base_url, key, model):
        return model.startswith("good-chat-a") or model.startswith("good-chat-d")

    token_pool.TokenPool.list_models = staticmethod(fake_list)
    token_pool.TokenPool.probe_model = staticmethod(fake_probe)

    # tokens view has pick + models buttons
    q = FakeQuery("admin:tokens", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    labels = [b.text for row in q.edited[0][1].inline_keyboard for b in row]
    check("tokens view has pick button", any("Pick the active key" in t for t in labels))
    check("tokens view has models button", any("Models of a key" in t for t in labels))

    # --- pick active key ---
    q_pick = FakeQuery("admin:pickkey", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_pick), ctx)
    check("pick list shown", q_pick.edited and "Which key" in q_pick.edited[0][0])
    pick_kb = q_pick.edited[0][1]
    pick_labels = [b.text for row in pick_kb.inline_keyboard for b in row]
    check("pick list has 3 entries + auto + none + back", len(pick_labels) == 6)
    check("active marked with ⭐", any(t.startswith("⭐") and "nemotron" in t for t in pick_labels))

    q_set = FakeQuery("admin:setactive:2", user_id=BOSS)  # kimi
    await h.handle_callback_query(SimpleNamespace(callback_query=q_set), ctx)
    check("setactive switches active", pool.active_entry.model == "kimi-k3.1-pro")
    check("manual persisted to .env",
          f"LLM_MANUAL_SELECTION={HL}|kimi-k3.1-pro" in env.read_text(encoding="utf-8"))
    check("tokens view shown after pick", q_set.edited and "Tokens & model" in q_set.edited[0][0])

    # auto: back to pinned
    q_auto = FakeQuery("admin:setactive:auto", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_auto), ctx)
    check("auto clears manual", pool.manual_selection is None
          and pool.active_entry.model == "nvidia/nemotron-3-ultra-550b-a55b")
    check("manual line cleared from .env", "LLM_MANUAL_SELECTION=" not in env.read_text(encoding="utf-8"))

    # stale pick index
    q_stale = FakeQuery("admin:setactive:99", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_stale), ctx)
    check("stale pick index handled", q_stale.answered and "no longer in the list" in q_stale.answered[0])

    # --- models browser ---
    q_keys = FakeQuery("admin:models", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_keys), ctx)
    check("models keys list shown", q_keys.edited and "models of which key" in q_keys.edited[0][0])
    keys_kb = q_keys.edited[0][1]
    check("3 distinct keys listed", len(keys_kb.inline_keyboard) == 4)  # 3 keys + back

    q_m0 = FakeQuery("admin:models:0", user_id=BOSS)  # NVIDIA key
    await h.handle_callback_query(SimpleNamespace(callback_query=q_m0), ctx)
    check("models page 0 shown", q_m0.edited and "Models of" in q_m0.edited[0][0] and "Page 1" in q_m0.edited[0][0])
    state = h._admin_models.get(BOSS, {})
    check("image/embed models filtered out",
          "bad-image-b" not in state.get("models", []) and "good-embed-c" not in state.get("models", []))
    check("10 chat models kept", len(state.get("models", [])) == 10)
    # page 1 has the remaining... 10 models, 10 per page -> 1 page only. Use a bigger list for pagination:
    # (pagination is exercised below with a longer fake list)

    # --- pick a model that validates -> activates, adds entry ---
    q_pick_model = FakeQuery("admin:model:0", user_id=BOSS)  # good-chat-a
    await h.handle_callback_query(SimpleNamespace(callback_query=q_pick_model), ctx)
    check("model validated + activated", pool.active_entry.model == "good-chat-a")
    check("new entry added to pool",
          any(e.model == "good-chat-a" and e.base_url == NV for e in pool.entries))
    check("new entry persisted to .env", "good-chat-a" in env.read_text(encoding="utf-8"))
    check("manual selection persisted", f"LLM_MANUAL_SELECTION={NV}|good-chat-a" in env.read_text(encoding="utf-8"))

    # --- pick a model that fails validation -> force option ---
    q_keys2 = FakeQuery("admin:models", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_keys2), ctx)
    q_m0b = FakeQuery("admin:models:0", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_m0b), ctx)
    # good-chat-e is index 3 in the filtered list (a,d,e,f,...) -> probe returns False
    q_bad = FakeQuery("admin:model:3", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_bad), ctx)
    check("failed model shows force prompt", q_bad.edited and "did not answer" in q_bad.edited[0][0])
    check("failed model not activated", pool.active_entry.model == "good-chat-a")
    q_force = FakeQuery("admin:modelforce", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_force), ctx)
    check("force-activate works", pool.active_entry.model == "good-chat-f")

    # --- pagination with a longer list ---
    async def fake_list_long(base_url, key):
        return [f"chat-{i:02d}" for i in range(25)]

    token_pool.TokenPool.list_models = staticmethod(fake_list_long)
    q_keys3 = FakeQuery("admin:models", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_keys3), ctx)
    q_m1 = FakeQuery("admin:models:1", user_id=BOSS)  # TokenHarbor key
    await h.handle_callback_query(SimpleNamespace(callback_query=q_m1), ctx)
    check("25 models, page 1 of 3", q_m1.edited and "Page 1 of 3" in q_m1.edited[0][0])
    q_next = FakeQuery("admin:models:next", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_next), ctx)
    check("next page shown", q_next.edited and "Page 2 of 3" in q_next.edited[0][0])
    q_next2 = FakeQuery("admin:models:next", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_next2), ctx)
    check("page 3 shown", q_next2.edited and "Page 3 of 3" in q_next2.edited[0][0])
    q_prev = FakeQuery("admin:models:prev", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_prev), ctx)
    check("prev page shown", q_prev.edited and "Page 2 of 3" in q_prev.edited[0][0])

    # empty models list
    async def fake_list_empty(base_url, key):
        return []

    token_pool.TokenPool.list_models = staticmethod(fake_list_empty)
    q_keys4 = FakeQuery("admin:models", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_keys4), ctx)
    q_m2 = FakeQuery("admin:models:2", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_m2), ctx)
    check("empty models handled", q_m2.edited and "No models" in q_m2.edited[0][0])

    token_pool.TokenPool.list_models = real_list
    token_pool.TokenPool.probe_model = real_probe


asyncio.run(run_flows())
print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
