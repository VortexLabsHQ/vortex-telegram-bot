"""Tests for the self-updater (bot/updater.py) + its wiring.

Run: /tmp/moztest-venv2/bin/python test_updater.py
Covers:
  - is_newer: v-prefix, equal, newer, older, different lengths
  - fetch_latest_release with a stubbed httpx client:
    200 with tag, 404 -> None, exception -> None, missing tag -> None
  - check_for_update: notifies once per version, never re-notifies the
    same version, honors dismiss + disabled flag + fetch failure
  - notify_after_restart: pending-notify flag round-trip (fake DB and
    the real Database), no message when the flag is unset
  - handle_update_callback: boss-only, update:no dismisses, update:yes
    with stubbed perform/restart steps (git/systemctl NEVER run here)
  - config defaults for UPDATE_CHECK_ENABLED / UPDATE_REPO
  - wiring: main.py schedules the daily job + post-restart notify,
    handlers.py routes "update:" callbacks before the admin branch
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


updater = load("updater")
database = load("database")
config = load("config")

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
REPO = "VortexLabsHQ/vortex-telegram-bot"


# ------------------------------------------------------------------ fakes

class FakeDB:
    """Dict-backed stand-in for Database bot_settings access."""

    def __init__(self):
        self.store: dict[str, str] = {}

    def get_setting(self, key, default=None):
        return self.store.get(key, default)

    def set_setting(self, key, value):
        self.store[key] = value

    def delete_setting(self, key):
        self.store.pop(key, None)


class FakeBot:
    def __init__(self):
        self.sent: list[dict] = []

    async def send_message(self, chat_id, text, reply_markup=None):
        self.sent.append(
            {"chat_id": chat_id, "text": text, "reply_markup": reply_markup}
        )


class FakeResponse:
    def __init__(self, status_code, payload=None):
        self.status_code = status_code
        self._payload = payload or {}

    def json(self):
        return self._payload


class FakeHTTPClient:
    """Stub httpx.AsyncClient: get() returns a canned response or raises."""

    def __init__(self, response=None, exc=None):
        self.response = response
        self.exc = exc
        self.urls: list[str] = []

    async def get(self, url):
        self.urls.append(url)
        if self.exc is not None:
            raise self.exc
        return self.response


class FakeQuery:
    def __init__(self, user_id, data):
        self.from_user = SimpleNamespace(id=user_id)
        self.data = data
        self.answers: list = []
        self.edits: list = []

    async def answer(self, text=None, **kwargs):
        self.answers.append(text)

    async def edit_message_text(self, text, **kwargs):
        self.edits.append(text)


async def _fake_perform_ok(repo=""):
    return True


async def _fake_perform_fail(repo=""):
    return False


def _fake_restart_ok():
    return True


def _fake_restart_fail():
    return False


# ------------------------------------------------------------------ is_newer

check("is_newer v-prefix newer", updater.is_newer("v1.2.0", "1.0.0"))
check("is_newer equal", not updater.is_newer("1.0.0", "1.0.0"))
check("is_newer equal with v", not updater.is_newer("v1.0.0", "1.0.0"))
check("is_newer older", not updater.is_newer("1.0.0", "1.2.0"))
check("is_newer different lengths equal", not updater.is_newer("1.2", "1.2.0"))
check("is_newer different lengths newer", updater.is_newer("1.2.1", "1.2"))
check("is_newer 1.10 > 1.9", updater.is_newer("1.10.0", "1.9.9"))
check("is_newer major bump", updater.is_newer("2.0", "1.9.9"))
check("is_newer empty latest", not updater.is_newer("", "1.0.0"))


# ------------------------------------------------------- fetch_latest_release

async def _fetch_tests():
    tag = await updater.fetch_latest_release(
        REPO, client=FakeHTTPClient(FakeResponse(200, {"tag_name": "v1.2.0"}))
    )
    check("fetch 200 returns tag", tag == "v1.2.0", repr(tag))
    none404 = await updater.fetch_latest_release(
        REPO, client=FakeHTTPClient(FakeResponse(404, {"message": "Not Found"}))
    )
    check("fetch 404 -> None", none404 is None, repr(none404))
    none500 = await updater.fetch_latest_release(
        REPO, client=FakeHTTPClient(FakeResponse(500, {}))
    )
    check("fetch 500 -> None", none500 is None, repr(none500))
    none_exc = await updater.fetch_latest_release(
        REPO, client=FakeHTTPClient(exc=RuntimeError("boom"))
    )
    check("fetch exception -> None", none_exc is None, repr(none_exc))
    none_tag = await updater.fetch_latest_release(
        REPO, client=FakeHTTPClient(FakeResponse(200, {}))
    )
    check("fetch 200 no tag -> None", none_tag is None, repr(none_tag))


asyncio.run(_fetch_tests())


# ------------------------------------------------------------ check_for_update

async def _check_tests():
    # Newer version -> one PV message to the boss, version recorded.
    # (fetch hits the real GitHub API, so stub it instead:)
    orig_fetch = updater.fetch_latest_release

    async def _fake_fetch(repo, client=None):
        return "v1.2.0"

    updater.fetch_latest_release = _fake_fetch
    try:
        bot, db = FakeBot(), FakeDB()
        await updater.check_for_update(bot, db, REPO, "1.0.0", boss_id=BOSS)
        check("check notifies boss once",
              len(bot.sent) == 1 and bot.sent[0]["chat_id"] == BOSS
              and "1.2.0" in bot.sent[0]["text"], repr(bot.sent))
        check("check stores available version",
              db.get_setting(updater.SETTING_AVAILABLE) == "v1.2.0")
        check("check message has yes/no keyboard",
              bot.sent[0]["reply_markup"] is not None
              and "update:yes" in str(bot.sent[0]["reply_markup"].to_dict())
              and "update:no" in str(bot.sent[0]["reply_markup"].to_dict()))

        # Same version again -> no re-notify (already notified).
        await updater.check_for_update(bot, db, REPO, "1.0.0", boss_id=BOSS)
        check("check does not re-notify same version", len(bot.sent) == 1)

        # Dismissed version -> no notify even with a fresh DB flag.
        bot2, db2 = FakeBot(), FakeDB()
        db2.set_setting(updater.SETTING_DISMISSED, "v1.2.0")
        await updater.check_for_update(bot2, db2, REPO, "1.0.0", boss_id=BOSS)
        check("check honors dismissed version", len(bot2.sent) == 0)

        # A different newer version than the dismissed one -> notify.
        async def _fake_fetch2(repo, client=None):
            return "v1.3.0"

        updater.fetch_latest_release = _fake_fetch2
        bot3, db3 = FakeBot(), FakeDB()
        db3.set_setting(updater.SETTING_DISMISSED, "v1.2.0")
        await updater.check_for_update(bot3, db3, REPO, "1.0.0", boss_id=BOSS)
        check("check notifies a newer-than-dismissed version",
              len(bot3.sent) == 1, repr(bot3.sent))

        # Disabled -> no notify.
        updater.fetch_latest_release = _fake_fetch
        bot4, db4 = FakeBot(), FakeDB()
        await updater.check_for_update(
            bot4, db4, REPO, "1.0.0", boss_id=BOSS, enabled=False
        )
        check("check disabled -> silent", len(bot4.sent) == 0)

        # Same version as current -> no notify.
        bot5, db5 = FakeBot(), FakeDB()
        await updater.check_for_update(bot5, db5, REPO, "v1.2.0", boss_id=BOSS)
        check("check current version -> silent", len(bot5.sent) == 0)

        # Fetch failure -> no notify, no raise.
        async def _fake_fetch_none(repo, client=None):
            return None

        updater.fetch_latest_release = _fake_fetch_none
        bot6, db6 = FakeBot(), FakeDB()
        await updater.check_for_update(bot6, db6, REPO, "1.0.0", boss_id=BOSS)
        check("check fetch None -> silent", len(bot6.sent) == 0)
    finally:
        updater.fetch_latest_release = orig_fetch


asyncio.run(_check_tests())


# ------------------------------------------------------- notify_after_restart

async def _notify_tests():
    bot, db = FakeBot(), FakeDB()
    await updater.notify_after_restart(bot, db, BOSS)
    check("notify no flag -> silent", len(bot.sent) == 0)

    bot, db = FakeBot(), FakeDB()
    db.set_setting(updater.SETTING_PENDING_NOTIFY, "1")
    await updater.notify_after_restart(bot, db, BOSS)
    check("notify flag set -> message sent",
          len(bot.sent) == 1 and bot.sent[0]["chat_id"] == BOSS
          and bot.sent[0]["text"] == updater.MSG_UPDATED, repr(bot.sent))
    check("notify clears pending flag",
          db.get_setting(updater.SETTING_PENDING_NOTIFY) is None)

    # Real Database round-trip for the pending flag.
    with tempfile.TemporaryDirectory() as tmp:
        real_db = database.Database(Path(tmp) / "vortex_bot.db")
        real_db.set_setting(updater.SETTING_PENDING_NOTIFY, "1")
        bot2 = FakeBot()
        await updater.notify_after_restart(bot2, real_db, BOSS)
        check("notify real DB round-trip",
              len(bot2.sent) == 1
              and real_db.get_setting(updater.SETTING_PENDING_NOTIFY) is None)


asyncio.run(_notify_tests())


# ----------------------------------------------------- handle_update_callback

async def _callback_tests():
    # Non-boss tap -> refused, nothing else happens.
    db = FakeDB()
    db.set_setting(updater.SETTING_AVAILABLE, "v1.2.0")
    q = FakeQuery(OTHER, "update:yes")
    await updater.handle_update_callback(q, db, BOSS, REPO)
    check("callback non-boss refused",
          len(q.edits) == 0 and q.answers == [updater.MSG_NOT_BOSS]
          and db.get_setting(updater.SETTING_AVAILABLE) == "v1.2.0",
          repr((q.answers, q.edits)))

    # Boss "update:no" -> dismissed, available cleared, ack edited.
    db = FakeDB()
    db.set_setting(updater.SETTING_AVAILABLE, "v1.2.0")
    q = FakeQuery(BOSS, "update:no")
    await updater.handle_update_callback(q, db, BOSS, REPO)
    check("callback no dismisses version",
          db.get_setting(updater.SETTING_DISMISSED) == "v1.2.0"
          and db.get_setting(updater.SETTING_AVAILABLE) is None)
    check("callback no edits ack",
          q.edits == [updater.MSG_UPDATE_LATER], repr(q.edits))

    # Boss "update:yes", perform + restart OK -> pending flag set.
    db = FakeDB()
    db.set_setting(updater.SETTING_AVAILABLE, "v1.2.0")
    q = FakeQuery(BOSS, "update:yes")
    await updater.handle_update_callback(
        q, db, BOSS, REPO,
        perform_update_fn=_fake_perform_ok, restart_fn=_fake_restart_ok,
    )
    check("callback yes sets pending flag",
          db.get_setting(updater.SETTING_PENDING_NOTIFY) == "1")
    check("callback yes edits updating",
          q.edits == [updater.MSG_UPDATING], repr(q.edits))

    # Boss "update:yes", perform fails -> failure text, flags cleared.
    db = FakeDB()
    db.set_setting(updater.SETTING_AVAILABLE, "v1.2.0")
    q = FakeQuery(BOSS, "update:yes")
    await updater.handle_update_callback(
        q, db, BOSS, REPO,
        perform_update_fn=_fake_perform_fail, restart_fn=_fake_restart_ok,
    )
    check("callback yes perform fail -> failure text",
          q.edits == [updater.MSG_UPDATING, updater.MSG_UPDATE_FAILED],
          repr(q.edits))
    check("callback yes perform fail clears flags",
          db.get_setting(updater.SETTING_AVAILABLE) is None
          and db.get_setting(updater.SETTING_PENDING_NOTIFY) is None)

    # Boss "update:yes", restart fails -> failure text, pending cleared.
    db = FakeDB()
    db.set_setting(updater.SETTING_AVAILABLE, "v1.2.0")
    q = FakeQuery(BOSS, "update:yes")
    await updater.handle_update_callback(
        q, db, BOSS, REPO,
        perform_update_fn=_fake_perform_ok, restart_fn=_fake_restart_fail,
    )
    check("callback yes restart fail -> failure text",
          q.edits == [updater.MSG_UPDATING, updater.MSG_UPDATE_FAILED],
          repr(q.edits))
    check("callback yes restart fail clears pending",
          db.get_setting(updater.SETTING_PENDING_NOTIFY) is None)


asyncio.run(_callback_tests())


# ------------------------------------------------------------------- config

check("config update check enabled by default",
      config.settings.update_check_enabled is True)
check("config update repo default",
      config.settings.update_repo == "VortexLabsHQ/vortex-telegram-bot",
      repr(config.settings.update_repo))


# ------------------------------------------------------------------- wiring

main_text = (audit_dir.parent / "bot" / "main.py").read_text(encoding="utf-8")
check("wiring main schedules daily update job",
      'run_daily(' in main_text and '"update_check"' in main_text
      and "_update_check_job" in main_text)
check("wiring main calls notify_after_restart at startup",
      "notify_after_restart(" in main_text)
handlers_text = (audit_dir / "handlers.py").read_text(encoding="utf-8")
check("wiring handlers routes update: before admin",
      handlers_text.index('startswith("update:")')
      < handlers_text.index('startswith(_ADMIN_CB + ":")'))

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
