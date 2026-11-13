"""Tests for the hidden /admin panel (2026-11-13) + the _admin_pending
regression found while building it.

Run: /tmp/moztest-venv2/bin/python test_admin.py
Covers:
  - _admin_pending is initialized in __init__ (regression: an M2 edit
    left an in-memory dict as dead code after a `return`, so the first
    use would raise AttributeError)
  - is_user_banned_globally exists and works
  - /admin is routable via parse_slash_command but NOT in BOT_COMMANDS
    (hidden: never in a command menu or /help)
  - /admin: boss in PV gets the menu; non-boss refused; group refused
  - admin callbacks: menu/tokens/users/stats/chats/health/recover/close
  - non-boss pressing an admin button is refused
  - ban/unban by id pending flow (digit -> global ban/unban, "لغو" cancels)
  - token pool describe_entries masks keys and reports status
"""
import asyncio
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


# Stub the heavy modules handlers imports but we do not test.
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
OTHER = 111222333


class FakeBot:
    def __init__(self):
        self.id = 999000111
        self.username = "vortex_test_bot"
        self.deleted = []

    async def delete_message(self, chat_id, message_id):
        self.deleted.append((chat_id, message_id))

    async def get_chat(self, chat_id):
        return SimpleNamespace(title="TestGroup", first_name="")

    async def get_chat_member_count(self, chat_id):
        return 3


class FakeMsg:
    def __init__(self, text, chat_type="private", user_id=BOSS, chat_id=-100123):
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
        self.sent = []          # (text, reply_markup)
        self.message_id = 1

    async def reply_text(self, text, **kwargs):
        self.sent.append((text, kwargs.get("reply_markup")))
        return SimpleNamespace(message_id=len(self.sent))


class FakeQuery:
    def __init__(self, data, user_id=BOSS, message=None):
        self.data = data
        self.from_user = SimpleNamespace(id=user_id, is_bot=False)
        self.message = message or FakeMsg("/admin", chat_type="private", user_id=user_id, chat_id=BOSS)
        self.answered = []
        self.edited = []        # (text, reply_markup)
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
        token_pool.ProviderEntry(base_url="https://api.tokenharbor.example/v1",
                                 key="thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", model="m2"),
    ])
    async def _fake_generate_reply(*args, **kwargs):
        return SimpleNamespace(text="سلام رئیس", files_to_create=[],
                               images_to_create=[], downloads_to_create=[])

    llm = SimpleNamespace(
        token_pool=pool,
        describe_active_model=lambda: "nemotron-3-ultra",
        generate_reply=_fake_generate_reply,
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
    return h, pool


# ---------- regression: _admin_pending init ----------
print("regression _admin_pending")
db = database.Database(Path(tempfile.mkdtemp()) / "t.db")
h, pool = make_handlers(db)
check("_admin_pending initialized in __init__", hasattr(h, "_admin_pending") and h._admin_pending == {})

# ---------- is_user_banned_globally ----------
print("is_user_banned_globally")
db.ban_user(0, 555, BOSS, global_ban=True)
check("global ban detected", db.is_user_banned_globally(555) is True)
check("non-banned user not flagged", db.is_user_banned_globally(556) is False)
check("list_banned_users finds it", any(b["user_id"] == 555 for b in db.list_banned_users()))
db.unban_user(0, 555, BOSS, global_ban=True)
check("global unban clears", db.is_user_banned_globally(555) is False)

# ---------- /admin hidden ----------
print("/admin hidden")
check("parse /admin routable", security.parse_slash_command("/admin") == ("admin", ""))
check("admin NOT in BOT_COMMANDS", "admin" not in [c for c, _ in security.BOT_COMMANDS])
src = (audit_dir / "handlers.py").read_text(encoding="utf-8")
import re as _re
_help = _re.search(r"_HELP_TEXT = \((.*?)\)\n", src, _re.S).group(1)
check("/admin NOT in _HELP_TEXT", "/admin" not in _help)

# ---------- /admin command ----------
print("/admin command")


async def run_admin_cmd():
    bot = FakeBot()
    ctx = FakeContext(bot)
    # boss in PV
    msg = FakeMsg("/admin", chat_type="private", user_id=BOSS, chat_id=BOSS)
    upd = SimpleNamespace(effective_message=msg, effective_chat=msg.chat,
                          effective_user=msg.from_user, callback_query=None)
    await h.handle_message(upd, ctx)
    check("boss PV gets menu", len(msg.sent) == 1 and "admin panel" in msg.sent[0][0],
          repr(msg.sent[0][0][:60]) if msg.sent else "no reply")
    check("menu has 10 rows (boss: tokens, users, stats, chats, image, locale, managers, power, health, close)",
          msg.sent and len(msg.sent[0][1].inline_keyboard) == 10)
    # non-boss
    msg2 = FakeMsg("/admin", chat_type="private", user_id=OTHER, chat_id=OTHER)
    upd2 = SimpleNamespace(effective_message=msg2, effective_chat=msg2.chat,
                           effective_user=msg2.from_user, callback_query=None)
    await h.handle_message(upd2, ctx)
    check("non-boss refused", msg2.sent and "only for the boss" in msg2.sent[0][0])
    # boss in group
    msg3 = FakeMsg("/admin", chat_type="supergroup", user_id=BOSS, chat_id=-100123)
    upd3 = SimpleNamespace(effective_message=msg3, effective_chat=msg3.chat,
                           effective_user=msg3.from_user, callback_query=None)
    await h.handle_message(upd3, ctx)
    check("group -> PV-only message", msg3.sent and "private chat" in msg3.sent[0][0])

    # ---------- admin callbacks ----------
    print("admin callbacks")
    q = FakeQuery("admin:tokens", user_id=BOSS)
    upd_q = SimpleNamespace(callback_query=q, effective_message=None,
                            effective_chat=None, effective_user=q.from_user)
    await h.handle_callback_query(upd_q, ctx)
    check("tokens view shows model", q.edited and "nemotron-3-ultra" in q.edited[0][0])
    check("tokens view masks keys (no full key)",
          q.edited and "nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" not in q.edited[0][0]
          and "thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" not in q.edited[0][0])
    check("tokens view shows fingerprint", q.edited and "…" in q.edited[0][0])
    check("tokens view shows both providers",
          q.edited and "nvidia.com" in q.edited[0][0] and "tokenharbor" in q.edited[0][0])

    q2 = FakeQuery("admin:users", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q2), ctx)
    check("users view renders", q2.edited and "Users" in q2.edited[0][0])

    q3 = FakeQuery("admin:menu", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q3), ctx)
    check("back to menu", q3.edited and "admin panel" in q3.edited[0][0])

    # non-boss pressing an admin button
    q4 = FakeQuery("admin:tokens", user_id=OTHER)
    await h.handle_callback_query(SimpleNamespace(callback_query=q4), ctx)
    check("non-boss button refused", q4.answered and "only for the boss" in q4.answered[0]
          and not q4.edited)

    # health check runs and returns to tokens view (stub the real network
    # health check so the test does not call the providers)
    async def _fake_health_check():
        return {"k1": True, "k2": True}

    async def _fake_retry_dead():
        return {}

    pool.health_check = _fake_health_check
    pool.retry_dead = _fake_retry_dead
    q5 = FakeQuery("admin:health", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q5), ctx)
    check("health runs, tokens view shown", q5.edited and "Tokens & model" in q5.edited[0][0])

    # close deletes the menu message
    q6 = FakeQuery("admin:close", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=q6), ctx)
    check("close deletes message", q6.deleted is True)

    # ---------- ban/unban by id ----------
    print("ban/unban by id")
    qb = FakeQuery("admin:ban", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=qb), ctx)
    check("ban tap asks for id", qb.edited and "numeric ID" in qb.edited[0][0])
    check("pending state set", h._admin_pending.get(BOSS, {}).get("action") == "ban")
    msg_ban = FakeMsg("777888999", chat_type="private", user_id=BOSS, chat_id=BOSS)
    upd_ban = SimpleNamespace(effective_message=msg_ban, effective_chat=msg_ban.chat,
                              effective_user=msg_ban.from_user, callback_query=None)
    await h.handle_message(upd_ban, ctx)
    check("id banned globally", db.is_user_banned_globally(777888999) is True)
    check("ban confirmed to boss", msg_ban.sent and "global" in msg_ban.sent[0][0])
    check("pending cleared after ban", BOSS not in h._admin_pending)

    qu = FakeQuery("admin:unban", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=qu), ctx)
    msg_unban = FakeMsg("777888999", chat_type="private", user_id=BOSS, chat_id=BOSS)
    upd_unban = SimpleNamespace(effective_message=msg_unban, effective_chat=msg_unban.chat,
                                effective_user=msg_unban.from_user, callback_query=None)
    await h.handle_message(upd_unban, ctx)
    check("id unbanned globally", db.is_user_banned_globally(777888999) is False)

    # cancel with "لغو"
    qb2 = FakeQuery("admin:ban", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=qb2), ctx)
    msg_cancel = FakeMsg("لغو", chat_type="private", user_id=BOSS, chat_id=BOSS)
    upd_cancel = SimpleNamespace(effective_message=msg_cancel, effective_chat=msg_cancel.chat,
                                 effective_user=msg_cancel.from_user, callback_query=None)
    await h.handle_message(upd_cancel, ctx)
    check("لغو cancels pending", BOSS not in h._admin_pending
          and msg_cancel.sent and "Cancelled" in msg_cancel.sent[0][0])

    # non-digit input drops pending and falls through (no crash, no ban)
    qb3 = FakeQuery("admin:ban", user_id=BOSS)
    await h.handle_callback_query(SimpleNamespace(callback_query=qb3), ctx)
    msg_chat = FakeMsg("سلام ورتکس", chat_type="private", user_id=BOSS, chat_id=BOSS)
    upd_chat = SimpleNamespace(effective_message=msg_chat, effective_chat=msg_chat.chat,
                               effective_user=msg_chat.from_user, callback_query=None)
    await h.handle_message(upd_chat, ctx)
    check("non-digit drops pending, no crash", BOSS not in h._admin_pending)

    # ---------- describe_entries ----------
    print("describe_entries")
    entries = pool.describe_entries()
    check("2 entries described", len(entries) == 2)
    check("status healthy", all(e["status"] == "healthy" for e in entries))
    check("no full key in describe",
          all(e["key_fp"] != "nvapi-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
              and e["key_fp"] != "thk_live_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
              and len(e["key_fp"]) < 20 for e in entries))


asyncio.run(run_admin_cmd())
print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
