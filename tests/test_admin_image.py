"""Tests for /admin add-image-provider (base URL + API key + model)
(2026-11-13).

Run: /tmp/moztest-venv2/bin/python test_admin_image.py
Covers:
  - DB: image_provider get/set/clear, malformed -> None, db file 0600
  - LLMClient.probe_image (stubbed httpx: b64 ok, url ok, non-200/empty/
    exception -> None)
  - LLMClient.generate_image with choice 'custom' (custom first, DuckAI
    fallback) and 'custom' with no provider (falls back to DuckAI)
  - Handlers: addimage flow (base_url -> model -> key, live probe,
    key message deleted, provider saved, choice custom, test photo sent),
    invalid base/model/key rejected, 'لغو' cancels, setimage:custom,
    removeimage, image view shows custom provider masked, permission
    enforcement for managers without the 'image' perm
"""
import asyncio
import base64
import os
import stat
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
NV = "https://integrate.api.nvidia.com/v1"
TH = "https://tokenharbor.ai/v1"
HL = "https://api.hilinkup.com/v1"

# ---------- DB ----------
print("db image_provider")
db = database.Database(Path(tempfile.mkdtemp()) / "t.db")
check("db file mode 0600", (db.db_path.stat().st_mode & 0o777) == 0o600)
check("image provider default None", db.get_image_provider() is None)
db.set_image_provider("https://img.example/v1", "sk-test-key-1234567890", "img-model-1")
check("image provider round-trip",
      db.get_image_provider() == ("https://img.example/v1", "sk-test-key-1234567890", "img-model-1"))
db.set_setting("image_provider", "bad-value")
check("malformed provider -> None", db.get_image_provider() is None)
db.clear_image_provider()
check("image provider cleared", db.get_image_provider() is None)

# ---------- LLMClient probe_image / generate_image custom ----------
print("llm probe_image / custom")
import httpx as _httpx

_real_client = _httpx.AsyncClient


class FakeResp:
    def __init__(self, status, body=None, content=b""):
        self.status_code = status
        self._body = body or {}
        self.content = content

    def json(self):
        return self._body

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError("http error")


class FakeImgClient:
    """httpx stub: POST returns b64 image or url; GET returns bytes."""

    def __init__(self, post_resp=None, exc=None):
        self.post_resp = post_resp
        self.exc = exc

    async def __aenter__(self):
        return self

    async def __aexit__(self, *a):
        return False

    async def post(self, url, headers=None, json=None):
        if self.exc:
            raise self.exc
        return self.post_resp

    async def get(self, url, timeout=None):
        return FakeResp(200, content=b"url-image-bytes")


async def test_probe():
    _httpx.AsyncClient = lambda timeout=None: FakeImgClient(
        post_resp=FakeResp(200, {"data": [{"b64_json": base64.b64encode(b"probe-img").decode()}]}))
    out = await llm_client_mod.LLMClient.probe_image("https://img.example/v1", "k", "m")
    check("probe_image b64 ok", out == b"probe-img")
    _httpx.AsyncClient = lambda timeout=None: FakeImgClient(
        post_resp=FakeResp(200, {"data": [{"url": "https://img.example/x.png"}]}))
    out = await llm_client_mod.LLMClient.probe_image("https://img.example/v1", "k", "m")
    check("probe_image url ok", out == b"url-image-bytes")
    _httpx.AsyncClient = lambda timeout=None: FakeImgClient(post_resp=FakeResp(401))
    check("probe_image 401 -> None",
          await llm_client_mod.LLMClient.probe_image("https://img.example/v1", "k", "m") is None)
    _httpx.AsyncClient = lambda timeout=None: FakeImgClient(post_resp=FakeResp(200, {"data": []}))
    check("probe_image empty -> None",
          await llm_client_mod.LLMClient.probe_image("https://img.example/v1", "k", "m") is None)
    _httpx.AsyncClient = lambda timeout=None: FakeImgClient(exc=RuntimeError("down"))
    check("probe_image exception -> None",
          await llm_client_mod.LLMClient.probe_image("https://img.example/v1", "k", "m") is None)
    _httpx.AsyncClient = _real_client


asyncio.run(test_probe())


async def test_custom_choice():
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
    client = llm_client_mod.LLMClient(settings, db3, SimpleNamespace(), workspace_root=Path(tempfile.mkdtemp()))
    duck_called = {"n": 0}

    async def fake_duckai(prompt):
        duck_called["n"] += 1
        return b"duck-image", None

    client.generate_image_duckai = fake_duckai
    _httpx.AsyncClient = lambda timeout=None: FakeImgClient(
        post_resp=FakeResp(200, {"data": [{"b64_json": base64.b64encode(b"custom-img").decode()}]}))
    db3.set_image_provider("https://img.example/v1", "sk-custom-key", "img-model-1")
    db3.set_image_model("custom")
    out, err = await client.generate_image("a cat")
    check("custom provider used first", out == b"custom-img" and err is None and duck_called["n"] == 0)
    # custom chosen but no provider -> falls back to DuckAI
    db3.clear_image_provider()
    out, err = await client.generate_image("a cat")
    check("custom without provider falls back to DuckAI", out == b"duck-image" and duck_called["n"] == 1)
    _httpx.AsyncClient = _real_client


asyncio.run(test_custom_choice())

# ---------- handlers addimage flow ----------
print("handlers addimage")


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
        self.photos = []
        self.message_id = 1
        self.deleted = False

    async def reply_text(self, text, **kwargs):
        self.sent.append((text, kwargs.get("reply_markup")))
        return SimpleNamespace(message_id=len(self.sent))

    async def reply_photo(self, photo, caption=None, **kwargs):
        self.photos.append((photo, caption))
        return SimpleNamespace(message_id=100 + len(self.photos))

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


def make_handlers(db, pool):
    settings = SimpleNamespace(
        boss_id=BOSS, daily_limit_messages=30,
        global_ban_default=False, ban_commands=["بن"], unban_commands=["انبن"],
    )
    llm = SimpleNamespace(token_pool=pool, describe_active_model=lambda: pool.active_entry.model)
    return handlers_mod.VortexBotHandlers(
        settings=settings, db=db, dollar_service=None, workspace_mgr=None,
        file_processor=None, llm_client=llm,
        rate_limiter=SimpleNamespace(is_allowed=lambda c, u: True),
    )


async def run_flows():
    bot = FakeBot()
    ctx = FakeContext(bot)
    db2 = database.Database(Path(tempfile.mkdtemp()) / "t2.db")
    pool = token_pool.TokenPool([
        token_pool.ProviderEntry(base_url=NV, key="nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", model="nvidia/nemotron-3-ultra-550b-a55b"),
        token_pool.ProviderEntry(base_url=TH, key="thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", model="deepseek-v4-flash:free"),
        token_pool.ProviderEntry(base_url=HL, key="hlk_cccccccccccccccccccccccccccccccc", model="kimi-k3.1-pro"),
    ], pinned_model="nvidia/nemotron-3-ultra-550b-a55b")
    h = make_handlers(db2, pool)

    def msg(text, user_id=BOSS):
        m = FakeMsg(text, chat_type="private", user_id=user_id, chat_id=BOSS)
        return m, SimpleNamespace(effective_message=m, effective_chat=m.chat,
                                   effective_user=m.from_user, callback_query=None)

    # stub probe_image: only keys starting with "good-" pass
    real_probe = llm_client_mod.LLMClient.probe_image

    async def fake_probe(base_url, key, model):
        return b"test-image-bytes" if key.startswith("good-") else None

    llm_client_mod.LLMClient.probe_image = staticmethod(fake_probe)

    # image view has the add button
    q = FakeQuery("admin:image", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    labels = [b.text for row in q.edited[0][1].inline_keyboard for b in row]
    check("image view has add button", any("Add an image service" in t for t in labels))

    # --- add flow ---
    q_add = FakeQuery("admin:addimage", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_add), ctx)
    check("addimage asks base URL", q_add.edited and "base URL" in q_add.edited[0][0])
    check("pending step=base_url", h._admin_pending.get(BOSS, {}).get("step") == "base_url")

    m, upd = msg("not-a-url")
    await h.handle_message(upd, ctx)
    check("bad base URL rejected", m.sent and "http://" in m.sent[0][0]
          and h._admin_pending.get(BOSS, {}).get("step") == "base_url")
    m, upd = msg("https://img.example/v1")
    await h.handle_message(upd, ctx)
    check("good base URL accepted", h._admin_pending.get(BOSS, {}).get("step") == "model")

    m, upd = msg("bad model with space")
    await h.handle_message(upd, ctx)
    check("bad model rejected", m.sent and "Not a valid model" in m.sent[0][0])
    m, upd = msg("img-model-1")
    await h.handle_message(upd, ctx)
    check("good model accepted", h._admin_pending.get(BOSS, {}).get("step") == "key")

    m, upd = msg("short")
    await h.handle_message(upd, ctx)
    check("short key rejected", m.sent and "too short" in m.sent[0][0])
    m, upd = msg("good-sk-test-key-1234567890")
    await h.handle_message(upd, ctx)
    check("key message deleted", m.deleted is True)
    check("provider saved", db2.get_image_provider() == ("https://img.example/v1", "good-sk-test-key-1234567890", "img-model-1"))
    check("choice set to custom", db2.get_image_model() == "custom")
    check("success message sent", m.sent and "added and activated" in m.sent[-1][0])
    check("test photo sent as proof", m.photos and m.photos[0][0] == b"test-image-bytes")
    check("pending cleared", BOSS not in h._admin_pending)

    # image view now shows the custom provider (masked) + select/remove buttons
    q = FakeQuery("admin:image", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("image view shows custom provider masked",
          q.edited and "img.example" in q.edited[0][0] and "img-model-1" in q.edited[0][0]
          and "good-sk-test-key-1234567890" not in q.edited[0][0])
    labels = [b.text for row in q.edited[0][1].inline_keyboard for b in row]
    check("image view has custom select + remove buttons",
          any("Custom service" in t for t in labels) and any("Remove custom service" in t for t in labels))

    # --- invalid provider rejected ---
    q_add2 = FakeQuery("admin:addimage", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_add2), ctx)
    m, upd = msg("https://bad.example/v1")
    await h.handle_message(upd, ctx)
    m, upd = msg("img-model-2")
    await h.handle_message(upd, ctx)
    m, upd = msg("bad-key-xyz-1234567890")
    await h.handle_message(upd, ctx)
    check("invalid provider rejected", m.sent and "did not answer" in m.sent[-1][0])
    check("old provider kept", db2.get_image_provider()[2] == "img-model-1")

    # --- cancel with لغو ---
    q_add3 = FakeQuery("admin:addimage", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q_add3), ctx)
    m, upd = msg("لغو")
    await h.handle_message(upd, ctx)
    check("لغو cancels addimage", BOSS not in h._admin_pending)

    # --- select custom / remove custom ---
    db2.set_image_model("duckai")
    q = FakeQuery("admin:setimage:custom", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("setimage:custom selects custom", db2.get_image_model() == "custom")
    q = FakeQuery("admin:removeimage", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("removeimage clears provider", db2.get_image_provider() is None)
    check("removeimage reverts choice to duckai", db2.get_image_model() == "duckai")

    # --- permission: manager without 'image' perm cannot addimage ---
    db2.add_manager(MGR, BOSS)
    db2.set_manager_perms(MGR, {"stats"})
    q = FakeQuery("admin:addimage", user_id=MGR)
    await h.handle_callback_query(SimpleNamespace(callback_query=q), ctx)
    check("manager without image perm refused", q.answered and "don't have access" in q.answered[0])

    llm_client_mod.LLMClient.probe_image = real_probe


asyncio.run(run_flows())
print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
