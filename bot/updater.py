"""Self-update support for the Vortex Telegram Bot.

Daily check against the latest GitHub release of the public repo:
when a newer version exists, the boss gets one private message with
✅/❌ buttons. On ✅ the bot pulls the update and restarts itself
(the "updated and back on" notice is sent at startup, see
``notify_after_restart``).

Assumptions the installer must provide:
- The systemd service is named ``vortex-bot``.
- A sudoers rule allows the bot's user to run exactly
  ``sudo systemctl restart vortex-bot`` with no password
  (e.g. ``vortex ALL=(ALL) NOPASSWD: /bin/systemctl restart vortex-bot``).
  Without it the restart step fails and the boss is told so.
- The install is a git checkout of the repo (``.git`` next to the code),
  so the update is ``git pull --ff-only``. When there is no ``.git``
  directory the updater falls back to downloading the release tarball
  from GitHub and extracting it over the install (``.git``, ``.env``
  and ``data/`` are never overwritten).

The version check uses the unauthenticated GitHub API, which only
works while the repo is public. While the repo is private the API
returns 404, ``fetch_latest_release`` returns None, and the daily
check silently does nothing — the bot keeps running the old version.
"""

from __future__ import annotations

import logging
import re
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path
from typing import Any

import httpx
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.locale import t

logger = logging.getLogger(__name__)

# i18n: these strings are localized by the locale system (bot/locale/)
# at call time, so an /admin language change applies immediately.
# Keys: update.available / update.yes / update.no / update.updating /
# update.done / update.later / update.failed / update.not_boss.
def _msg_update_available(version: str) -> str:
    return t("update.available", version=version)


def _btn_update_yes() -> str:
    return t("update.yes")


def _btn_update_no() -> str:
    return t("update.no")


# Backwards-compatible aliases (resolved once, in the default language):
# older tests and callers compare against these names. New code uses
# t("update.*") directly so the language applies per call.
MSG_UPDATE_AVAILABLE = t("update.available", version="{version}")
BTN_UPDATE_YES = t("update.yes")
BTN_UPDATE_NO = t("update.no")
MSG_UPDATING = t("update.updating")
MSG_UPDATED = t("update.done")
MSG_UPDATE_LATER = t("update.later")
MSG_UPDATE_FAILED = t("update.failed")
MSG_NOT_BOSS = t("update.not_boss")

# bot_settings keys used by the updater.
SETTING_AVAILABLE = "update_available_version"
SETTING_DISMISSED = "update_dismissed_version"
SETTING_PENDING_NOTIFY = "update_pending_notify"

SERVICE_NAME = "vortex-bot"
GITHUB_API_URL = "https://api.github.com/repos/{repo}/releases/latest"
USER_AGENT = "vortex-telegram-bot-updater"

# Install root: the directory that contains the bot/ package.
INSTALL_ROOT = Path(__file__).resolve().parent.parent


def _parse_version(version: str) -> tuple[int, ...]:
    """Dotted version -> tuple of ints. Tolerant of a leading "v" and
    of non-numeric suffixes (e.g. "1.2.0-rc1" -> (1, 2, 0))."""
    version = version.strip().lstrip("vV")
    parts: list[int] = []
    for segment in version.split("."):
        match = re.match(r"(\d+)", segment)
        parts.append(int(match.group(1)) if match else 0)
    return tuple(parts)


def is_newer(latest: str, current: str) -> bool:
    """True when `latest` is a newer dotted version than `current`.
    A leading "v" is ignored and shorter versions are padded with
    zeros, so "1.2" == "1.2.0" and "1.10.0" > "1.9.9"."""
    if not latest or not current:
        return False
    latest_parts = _parse_version(latest)
    current_parts = _parse_version(current)
    width = max(len(latest_parts), len(current_parts))
    latest_parts += (0,) * (width - len(latest_parts))
    current_parts += (0,) * (width - len(current_parts))
    return latest_parts > current_parts


async def fetch_latest_release(
    repo: str, client: httpx.AsyncClient | None = None
) -> str | None:
    """Latest release tag (e.g. "v1.2.0") for `repo` ("owner/name"),
    or None on any failure (network error, 404, non-200, missing tag).
    Never raises. `client` is injectable for tests; otherwise a short
    lived client with a 10s timeout is created and closed here."""
    own_client = client is None
    if own_client:
        client = httpx.AsyncClient(
            timeout=10.0, headers={"User-Agent": USER_AGENT}
        )
    try:
        assert client is not None
        resp = await client.get(GITHUB_API_URL.format(repo=repo))
        if resp.status_code != 200:
            logger.info(
                "Update check: GitHub API returned %s for %s.",
                resp.status_code,
                repo,
            )
            return None
        tag = resp.json().get("tag_name")
        return str(tag).strip() if tag else None
    except Exception:
        logger.exception("Update check: failed to fetch latest release.")
        return None
    finally:
        if own_client and client is not None:
            await client.aclose()


def _git_pull() -> bool:
    """``git pull --ff-only`` in the install root. True on success."""
    try:
        result = subprocess.run(
            ["git", "pull", "--ff-only"],
            cwd=str(INSTALL_ROOT),
            timeout=120,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            logger.warning(
                "Update: git pull failed (%s): %s",
                result.returncode,
                (result.stderr or result.stdout or "").strip()[:500],
            )
            return False
        return True
    except Exception:
        logger.exception("Update: git pull raised.")
        return False


def _download_tarball(repo: str, tag: str) -> bool:
    """Download the release tarball for `tag` and extract it over the
    install root. ``.git``, ``.env`` and ``data/`` (live user data)
    are never overwritten. True on success."""
    url = f"https://codeload.github.com/{repo}/tarball/refs/tags/{tag}"
    try:
        with httpx.Client(
            timeout=120.0,
            headers={"User-Agent": USER_AGENT},
            follow_redirects=True,
        ) as client:
            resp = client.get(url)
            if resp.status_code != 200:
                logger.warning(
                    "Update: tarball download returned %s.", resp.status_code
                )
                return False
            with tempfile.TemporaryDirectory(prefix="vortex_update_") as tmp:
                tar_path = Path(tmp) / "release.tar.gz"
                tar_path.write_bytes(resp.content)
                with tarfile.open(tar_path, "r:gz") as tar:
                    tar.extractall(tmp, filter="data")
                extracted = [p for p in Path(tmp).iterdir() if p.is_dir()]
                if len(extracted) != 1:
                    logger.warning(
                        "Update: unexpected tarball layout (%d top dirs).",
                        len(extracted),
                    )
                    return False
                src = extracted[0]
                for item in src.iterdir():
                    if item.name in {".git", ".env", "data", "__pycache__"}:
                        continue
                    dest = INSTALL_ROOT / item.name
                    if dest.exists():
                        if dest.is_dir() and not dest.is_symlink():
                            shutil.rmtree(dest)
                        else:
                            dest.unlink()
                    if item.is_dir():
                        shutil.copytree(item, dest)
                    else:
                        shutil.copy2(item, dest)
        return True
    except Exception:
        logger.exception("Update: tarball install raised.")
        return False


async def perform_update(repo: str) -> bool:
    """Fetch the update into the install: ``git pull --ff-only`` when
    this is a git checkout, otherwise the release tarball. True when
    the new code is in place (a restart is still needed)."""
    if (INSTALL_ROOT / ".git").is_dir():
        return _git_pull()
    latest = await fetch_latest_release(repo)
    if not latest:
        logger.warning("Update: no .git dir and no release tag; aborting.")
        return False
    return _download_tarball(repo, latest)


def _restart_service() -> bool:
    """Restart the systemd service (needs the sudoers rule documented
    at the top of this module). True when systemctl exits 0."""
    try:
        result = subprocess.run(
            ["sudo", "systemctl", "restart", SERVICE_NAME],
            timeout=60,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            logger.warning(
                "Update: systemctl restart failed (%s): %s",
                result.returncode,
                (result.stderr or "").strip()[:500],
            )
            return False
        return True
    except Exception:
        logger.exception("Update: systemctl restart raised.")
        return False


def _update_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    _btn_update_yes(), callback_data="update:yes"
                ),
                InlineKeyboardButton(
                    _btn_update_no(), callback_data="update:no"
                ),
            ]
        ]
    )


async def check_for_update(
    bot: Any,
    db: Any,
    repo: str,
    current: str,
    boss_id: int = 0,
    enabled: bool = True,
) -> None:
    """The daily job: when a newer release exists and the boss has
    not already been told about / dismissed this version, send the
    boss one PV message with ✅/❌ buttons and record the version in
    bot_settings so the boss is never nagged daily. Never raises."""
    try:
        if not enabled or not boss_id or not repo or not current:
            return
        latest = await fetch_latest_release(repo)
        if not latest or not is_newer(latest, current):
            return
        if db.get_setting(SETTING_DISMISSED) == latest:
            return
        if db.get_setting(SETTING_AVAILABLE) == latest:
            return
        await bot.send_message(
            chat_id=boss_id,
            text=_msg_update_available(latest),
            reply_markup=_update_keyboard(),
        )
        db.set_setting(SETTING_AVAILABLE, latest)
        logger.info("Update check: notified boss about %s.", latest)
    except Exception:
        logger.exception("Update check failed.")


async def handle_update_callback(
    query: Any,
    db: Any,
    boss_id: int,
    repo: str = "",
    perform_update_fn: Any = None,
    restart_fn: Any = None,
) -> None:
    """Handle an "update:yes" / "update:no" button tap. Boss-only;
    anyone else gets a refusal. Never raises.

    `perform_update_fn` / `restart_fn` are injectable so tests can
    stub the git/systemctl steps; they default to the real ones."""
    try:
        user = getattr(query, "from_user", None)
        if not user or user.id != boss_id:
            try:
                await query.answer(t("update.not_boss"))
            except Exception:
                pass
            return
        data = (getattr(query, "data", "") or "").strip()
        action = data.split(":", 1)[1] if ":" in data else ""
        try:
            await query.answer()
        except Exception:
            pass
        if action == "no":
            available = db.get_setting(SETTING_AVAILABLE)
            if available:
                db.set_setting(SETTING_DISMISSED, available)
            db.delete_setting(SETTING_AVAILABLE)
            await query.edit_message_text(t("update.later"))
            return
        if action != "yes":
            return
        await query.edit_message_text(t("update.updating"))
        perform = perform_update_fn or perform_update
        # The real perform_update takes the repo; a test stub may
        # take no arguments, so fall back to a bare call.
        try:
            ok = await perform(repo)
        except TypeError:
            ok = await perform()
        if not ok:
            db.delete_setting(SETTING_AVAILABLE)
            await query.edit_message_text(t("update.failed"))
            return
        db.set_setting(SETTING_PENDING_NOTIFY, "1")
        restart = restart_fn or _restart_service
        if restart():
            # The process restarts here; notify_after_restart() sends
            # the "updated and back on" message at startup.
            return
        db.delete_setting(SETTING_PENDING_NOTIFY)
        db.delete_setting(SETTING_AVAILABLE)
        await query.edit_message_text(t("update.failed"))
    except Exception:
        logger.exception("Update callback failed.")
        try:
            await query.edit_message_text(t("update.failed"))
        except Exception:
            pass


async def notify_after_restart(bot: Any, db: Any, boss_id: int) -> None:
    """Called once at startup: if a self-update set the pending flag,
    clear it and tell the boss the bot is updated and back on.
    Never raises."""
    try:
        if not boss_id or db.get_setting(SETTING_PENDING_NOTIFY) != "1":
            return
        db.delete_setting(SETTING_PENDING_NOTIFY)
        await bot.send_message(chat_id=boss_id, text=t("update.done"))
        logger.info("Update: notified boss after restart.")
    except Exception:
        logger.exception("Update post-restart notify failed.")
