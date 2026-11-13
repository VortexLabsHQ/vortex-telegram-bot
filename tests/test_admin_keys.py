"""Tests for /admin add/remove API keys (2026-11-13).

Run: /tmp/moztest-venv2/bin/python test_admin_keys.py
Covers:
  - TokenPool.add_entry / remove_entry (dedupe, empty guards, active re-pick)
  - TokenPool.probe_entry (stubbed httpx: 200 ok, 401/exception fail)
  - config.write_llm_providers (replaces line, preserves others, no dupes,
    appends when missing) + find_env_file via VORTEX_BOT_ENV
  - Handlers add-key flow: provider pick -> model -> key -> probe -> add +
    persist to .env + key message deleted; invalid/duplicate rejected;
    custom base URL validated; "لغو" cancels
  - Handlers remove-key flow: list -> confirm -> removed + .env updated;
    last key cannot be removed; stale index handled
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


def make_pool():
    return token_pool.TokenPool([
        token_pool.ProviderEntry(base_url="https://integrate.api.nvidia.com/v1",
                                 key="nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", model="m1"),
        token_pool.ProviderEntry(base_url="https://tokenharbor.ai/v1",
                                 key="thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", model="m2"),
    ])


# ---------- TokenPool.add_entry / remove_entry ----------
print("pool add/remove")


async def test_pool():
    pool = make_pool()
    n0 = len(pool.entries)
    # add new
    ok = await pool.add_entry(token_pool.ProviderEntry(
        base_url="https://api.hilinkup.com/v1",
        key="hlk_cccccccccccccccccccccccccccccccc", model="m3"))
    check("add_entry new returns True", ok is True)
    check("pool grew", len(pool.entries) == n0 + 1)
    check("new key healthy", "hlk_cccccccccccccccccccccccccccccccc" in pool.healthy_keys)
    # duplicate
    ok2 = await pool.add_entry(token_pool.ProviderEntry(
        base_url="https://api.hilinkup.com/v1",
        key="hlk_cccccccccccccccccccccccccccccccc", model="m3"))
    check("add_entry duplicate returns False", ok2 is False)
    check("pool unchanged on duplicate", len(pool.entries) == n0 + 1)
    # empty key/model rejected
    ok3 = await pool.add_entry(token_pool.ProviderEntry(
        base_url="https://x.example/v1", key="", model="m9"))
    check("add_entry empty key rejected", ok3 is False)
    # remove
    removed = await pool.remove_entry("hlk_cccccccccccccccccccccccccccccccc")
    check("remove_entry returns removed", len(removed) == 1 and removed[0].model == "m3")
    check("pool shrank", len(pool.entries) == n0)
    check("removed key not healthy", "hlk_cccccccccccccccccccccccccccccccc" not in pool.healthy_keys)
    # remove unknown
    removed2 = await pool.remove_entry("no-such-key")
    check("remove unknown returns []", removed2 == [])
    # remove active re-picks
    active_before = pool.active_entry
    await pool.remove_entry(active_before.key)
    check("active re-picked after removing active",
          len(pool.entries) == 1 and pool.active_entry.key != active_before.key)


asyncio.run(test_pool())

# ---------- probe_entry (stubbed httpx) ----------
print("probe_entry")


class FakeResp:
    def __init__(self, status):
        self.status_code = status


class FakeClient:
    def __init__(self, status=None, exc=None):
        self.status = status
        self.exc = exc

    async def __aenter__(self):
        return self

    async def __aexit__(self, *a):
        return False

    async def get(self, url, headers=None):
        if self.exc:
            raise self.exc
        return FakeResp(self.status)


import httpx as _httpx

_real_client = _httpx.AsyncClient


async def test_probe():
    _httpx.AsyncClient = lambda timeout=None: FakeClient(status=200)
    check("probe 200 -> True", await token_pool.TokenPool.probe_entry("https://x.example/v1", "k") is True)
    _httpx.AsyncClient = lambda timeout=None: FakeClient(status=401)
    check("probe 401 -> False", await token_pool.TokenPool.probe_entry("https://x.example/v1", "k") is False)
    _httpx.AsyncClient = lambda timeout=None: FakeClient(exc=RuntimeError("down"))
    check("probe exception -> False", await token_pool.TokenPool.probe_entry("https://x.example/v1", "k") is False)
    _httpx.AsyncClient = _real_client


asyncio.run(test_probe())

# ---------- config.write_llm_providers ----------
print("write_llm_providers")
tmpdir = Path(tempfile.mkdtemp())
env_path = tmpdir / ".env"
env_path.write_text(
    'BOT_TOKEN=xxx\nLLM_PROVIDERS=https://a.example/v1|key1|m1,https://b.example/v1|key2|m2\nOTHER=1\n',
    encoding="utf-8",
)
entries = [
    config.ProviderEntry(base_url="https://a.example/v1", key="key1", model="m1"),
    config.ProviderEntry(base_url="https://c.example/v1", key="key3", model="m3"),
]
config.write_llm_providers(env_path, entries)
text = env_path.read_text(encoding="utf-8")
check("LLM_PROVIDERS line replaced",
      "LLM_PROVIDERS=https://a.example/v1|key1|m1,https://c.example/v1|key3|m3" in text)
check("other lines preserved", "BOT_TOKEN=xxx" in text and "OTHER=1" in text)
check("no duplicate LLM_PROVIDERS lines", text.count("LLM_PROVIDERS=") == 1)
check(".env mode 0600", (env_path.stat().st_mode & 0o777) == 0o600)
# no LLM_PROVIDERS line -> appended
env2 = tmpdir / ".env2"
env2.write_text("BOT_TOKEN=yyy\n", encoding="utf-8")
config.write_llm_providers(env2, entries)
check("LLM_PROVIDERS appended when missing",
      "LLM_PROVIDERS=https://a.example/v1|key1|m1" in env2.read_text(encoding="utf-8"))
# find_env_file via override
os.environ["VORTEX_BOT_ENV"] = str(env_path)
check("find_env_file honors VORTEX_BOT_ENV", config.find_env_file() == env_path)

# ---------- handlers add/remove flows ----------
print("handlers add/remove")


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
    llm = SimpleNamespace(token_pool=pool, describe_active_model=lambda: "m1")
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
    env.write_text("LLM_PROVIDERS=https://integrate.api.nvidia.com/v1|nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa|m1,https://tokenharbor.ai/v1|thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb|m2\n", encoding="utf-8")
    os.environ["VORTEX_BOT_ENV"] = str(env)
    h = make_handlers(db, pool, env)

    # stub probe: only keys starting with "good-" pass
    real_probe = token_pool.TokenPool.probe_entry

    async def fake_probe(base_url, key):
        return key.startswith("good-")

    token_pool.TokenPool.probe_entry = staticmethod(fake_probe)

    # tokens view has add/remove buttons
    q = FakeQuery("admin:tokens", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    kb = q.edited[0][1]
    labels = [b.text for row in kb.inline_keyboard for b in row]
    check("tokens view has add button", any("Add a key" in t for t in labels))
    check("tokens view has remove button", any("Remove a key" in t for t in labels))

    # --- add flow: provider pick -> model -> key ---
    q_add = FakeQuery("admin:addkey", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_add), ctx)
    check("addkey shows providers", q_add.edited and "Which service" in q_add.edited[0][0])

    q_nv = FakeQuery("admin:addkey:nvidia", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_nv), ctx)
    check("nvidia pick asks for model", q_nv.edited and "model" in q_nv.edited[0][0])
    check("pending step=model", h._admin_pending.get(BOSS, {}).get("step") == "model")

    m_model = FakeMsg("nvidia/nemotron-3-ultra-550b-a55b", chat_type="private", user_id=BOSS, chat_id=BOSS)
    await h.handle_message(SimpleNamespace(effective_message=m_model, effective_chat=m_model.chat,
                                           effective_user=m_model.from_user, callback_query=None), ctx)
    check("model accepted, asks for key", m_model.sent and "API key" in m_model.sent[0][0])
    check("pending step=key", h._admin_pending.get(BOSS, {}).get("step") == "key")

    m_key = FakeMsg("good-nvapi-testkey-1234567890", chat_type="private", user_id=BOSS, chat_id=BOSS)
    await h.handle_message(SimpleNamespace(effective_message=m_key, effective_chat=m_key.chat,
                                           effective_user=m_key.from_user, callback_query=None), ctx)
    check("key message deleted", m_key.deleted is True)
    check("key added to pool", any(e.key == "good-nvapi-testkey-1234567890" for e in pool.entries))
    check("key persisted to .env", "good-nvapi-testkey-1234567890" in env.read_text(encoding="utf-8"))
    check("success message sent", m_key.sent and "added and saved" in m_key.sent[-1][0])
    check("pending cleared", BOSS not in h._admin_pending)

    # --- invalid key rejected ---
    q_nv2 = FakeQuery("admin:addkey:nvidia", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_nv2), ctx)
    m_m2 = FakeMsg("nvidia/nemotron-3-ultra-550b-a55b", chat_type="private", user_id=BOSS, chat_id=BOSS)
    await h.handle_message(SimpleNamespace(effective_message=m_m2, effective_chat=m_m2.chat,
                                           effective_user=m_m2.from_user, callback_query=None), ctx)
    m_bad = FakeMsg("bad-key-xyz", chat_type="private", user_id=BOSS, chat_id=BOSS)
    await h.handle_message(SimpleNamespace(effective_message=m_bad, effective_chat=m_bad.chat,
                                           effective_user=m_bad.from_user, callback_query=None), ctx)
    check("invalid key rejected", m_bad.sent and "isn't valid" in m_bad.sent[-1][0])
    check("invalid key not in pool", not any(e.key == "bad-key-xyz" for e in pool.entries))

    # --- duplicate rejected ---
    q_nv3 = FakeQuery("admin:addkey:nvidia", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_nv3), ctx)
    m_m3 = FakeMsg("nvidia/nemotron-3-ultra-550b-a55b", chat_type="private", user_id=BOSS, chat_id=BOSS)
    await h.handle_message(SimpleNamespace(effective_message=m_m3, effective_chat=m_m3.chat,
                                           effective_user=m_m3.from_user, callback_query=None), ctx)
    m_dup = FakeMsg("good-nvapi-testkey-1234567890", chat_type="private", user_id=BOSS, chat_id=BOSS)
    await h.handle_message(SimpleNamespace(effective_message=m_dup, effective_chat=m_dup.chat,
                                           effective_user=m_dup.from_user, callback_query=None), ctx)
    check("duplicate rejected", m_dup.sent and "already in the list" in m_dup.sent[-1][0])
    check("pool has no duplicate", sum(1 for e in pool.entries if e.key == "good-nvapi-testkey-1234567890") == 1)

    # --- custom base URL: bad then good ---
    q_c = FakeQuery("admin:addkey:custom", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_c), ctx)
    check("custom asks base URL", q_c.edited and "base URL" in q_c.edited[0][0])
    m_badurl = FakeMsg("not-a-url", chat_type="private", user_id=BOSS, chat_id=BOSS)
    await h.handle_message(SimpleNamespace(effective_message=m_badurl, effective_chat=m_badurl.chat,
                                           effective_user=m_badurl.from_user, callback_query=None), ctx)
    check("bad base URL rejected, stays in step", m_badurl.sent and "http://" in m_badurl.sent[0][0]
          and h._admin_pending.get(BOSS, {}).get("step") == "base_url")
    m_url = FakeMsg("https://custom.example/v1", chat_type="private", user_id=BOSS, chat_id=BOSS)
    await h.handle_message(SimpleNamespace(effective_message=m_url, effective_chat=m_url.chat,
                                           effective_user=m_url.from_user, callback_query=None), ctx)
    check("good base URL accepted", h._admin_pending.get(BOSS, {}).get("step") == "model"
          and h._admin_pending[BOSS].get("base_url") == "https://custom.example/v1")
    # cancel with لغو
    m_cancel = FakeMsg("لغو", chat_type="private", user_id=BOSS, chat_id=BOSS)
    await h.handle_message(SimpleNamespace(effective_message=m_cancel, effective_chat=m_cancel.chat,
                                           effective_user=m_cancel.from_user, callback_query=None), ctx)
    check("لغو cancels addkey", BOSS not in h._admin_pending)

    # --- remove flow: list -> confirm -> removed ---
    n_before = len(pool.entries)
    q_rm = FakeQuery("admin:removekey", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_rm), ctx)
    check("remove list shown", q_rm.edited and "Which key" in q_rm.edited[0][0])
    rm_kb = q_rm.edited[0][1]
    check("remove list has one button per entry",
          len(rm_kb.inline_keyboard) == n_before + 1)  # entries + back
    q_rm0 = FakeQuery("admin:rm:0", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_rm0), ctx)
    check("confirm screen shown", q_rm0.edited and "Remove this key" in q_rm0.edited[0][0])
    key0 = pool.entries[0].key
    q_conf = FakeQuery("admin:rmconfirm:0", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_conf), ctx)
    check("key removed from pool", not any(e.key == key0 for e in pool.entries))
    check("key removed from .env", key0 not in env.read_text(encoding="utf-8"))
    check("tokens view shown after remove", q_conf.edited and "Tokens & model" in q_conf.edited[0][0])

    # --- cannot remove the last key ---
    while len(pool.entries) > 1:
        await pool.remove_entry(pool.entries[0].key)
    q_last = FakeQuery("admin:removekey", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_last), ctx)
    check("last key removal refused", q_last.answered and "only one key" in q_last.answered[0]
          and not q_last.edited)
    # stale index
    q_stale = FakeQuery("admin:rm:99", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_stale), ctx)
    check("stale index handled", q_stale.answered and "no longer in the list" in q_stale.answered[0])

    token_pool.TokenPool.probe_entry = real_probe


asyncio.run(run_flows())
print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
