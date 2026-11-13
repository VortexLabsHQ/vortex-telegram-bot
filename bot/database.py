"""
SQLite Database layer for Vortex Telegram Bot.
Manages:
1. `blocked_users` table (per-group or global internal bans) + `ban_audit_logs`
2. `user_contexts` table (strictly isolated per (chat_id, user_id) rolling summary & file summary)
3. `user_messages` table (strictly isolated per (chat_id, user_id) conversation window)
4. `bot_settings` table (runtime config overrides if needed)
"""

from __future__ import annotations

import logging
import sqlite3
import threading
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

logger = logging.getLogger(__name__)

GLOBAL_CHAT_ID = 0  # Used when global_ban is enabled


class Database:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._init_schema()
        # The DB holds user data and (since the custom image provider)
        # API keys in bot_settings — keep it owner-only like .env.
        try:
            self.db_path.chmod(0o600)
        except Exception:
            pass

    @contextmanager
    def _get_conn(self):
        # A context manager: the connection is CLOSED when the `with`
        # block exits. Previously every call leaked a connection (the
        # `with conn:` only committed, never closed it), so the bot
        # accumulated open file descriptors for its whole lifetime.
        conn = sqlite3.connect(str(self.db_path), check_same_thread=False)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA foreign_keys=ON;")
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _init_schema(self) -> None:
        with self._lock, self._get_conn() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS blocked_users (
                    chat_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    banned_by INTEGER NOT NULL,
                    banned_at TEXT NOT NULL,
                    PRIMARY KEY (chat_id, user_id)
                );

                CREATE INDEX IF NOT EXISTS idx_blocked_user_lookup
                ON blocked_users (user_id, chat_id);

                CREATE TABLE IF NOT EXISTS ban_audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    action TEXT NOT NULL,
                    actor_id INTEGER NOT NULL,
                    target_user_id INTEGER NOT NULL,
                    chat_id INTEGER NOT NULL,
                    created_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS user_contexts (
                    chat_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    rolling_summary TEXT NOT NULL DEFAULT '',
                    last_file_summary TEXT NOT NULL DEFAULT '',
                    updated_at TEXT NOT NULL,
                    PRIMARY KEY (chat_id, user_id)
                );

                CREATE TABLE IF NOT EXISTS user_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chat_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_user_messages_lookup
                ON user_messages (chat_id, user_id, id);

                CREATE TABLE IF NOT EXISTS bot_settings (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                );

                -- Allowlist for private mode (/off): only the boss,
                -- managers and these users can use the bot.
                CREATE TABLE IF NOT EXISTS allowlist (
                    user_id INTEGER PRIMARY KEY,
                    added_by INTEGER,
                    added_at TEXT
                );

                -- Managers (admins): boss-appointed users with a subset
                -- of admin-panel permissions (comma-separated names).
                CREATE TABLE IF NOT EXISTS managers (
                    user_id INTEGER PRIMARY KEY,
                    permissions TEXT NOT NULL DEFAULT '',
                    added_by INTEGER,
                    added_at TEXT
                );

                -- Daily per-user message quota (day = Asia/Tehran date, YYYY-MM-DD).
                CREATE TABLE IF NOT EXISTS daily_usage (
                    user_id INTEGER NOT NULL,
                    day TEXT NOT NULL,
                    count INTEGER NOT NULL DEFAULT 0,
                    PRIMARY KEY (user_id, day)
                );

                CREATE INDEX IF NOT EXISTS idx_daily_usage_day
                ON daily_usage (day);

                -- Members the bot has seen per chat (groups + PV), for stats.
                -- first_name/username are refreshed on every message; the
                -- numeric user_id is the stable identity.
                CREATE TABLE IF NOT EXISTS chat_users (
                    chat_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    first_name TEXT NOT NULL DEFAULT '',
                    username TEXT NOT NULL DEFAULT '',
                    last_seen_at TEXT NOT NULL,
                    message_count INTEGER NOT NULL DEFAULT 0,
                    PRIMARY KEY (chat_id, user_id)
                );

                CREATE INDEX IF NOT EXISTS idx_chat_users_lookup
                ON chat_users (chat_id, message_count DESC);

                -- Per-chat unban overrides: a globally-banned user who is
                -- unbanned in ONE chat gets an override row, so they can
                -- use the bot in that chat while staying banned elsewhere.
                CREATE TABLE IF NOT EXISTS ban_overrides (
                    chat_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    PRIMARY KEY (chat_id, user_id)
                );
                """
            )

    # ------------------------------------------------------------------
    # Blocked Users (Internal Ban System)
    # ------------------------------------------------------------------

    def is_user_banned(self, chat_id: int, user_id: int, check_global: bool = True) -> bool:
        """
        Checks if `user_id` is banned in `chat_id` (or globally if `GLOBAL_CHAT_ID` row exists).
        A per-chat unban override (ban_overrides) lets a globally-banned
        user back into ONE chat while staying banned elsewhere.
        Fast indexed lookup executed as the very first step of every message handler.
        """
        with self._lock, self._get_conn() as conn:
            override = conn.execute(
                "SELECT 1 FROM ban_overrides WHERE chat_id = ? AND user_id = ? LIMIT 1",
                (chat_id, user_id),
            ).fetchone()
            if override:
                return False
            if check_global:
                row = conn.execute(
                    "SELECT 1 FROM blocked_users WHERE user_id = ? AND chat_id IN (?, ?) LIMIT 1",
                    (user_id, chat_id, GLOBAL_CHAT_ID),
                ).fetchone()
            else:
                row = conn.execute(
                    "SELECT 1 FROM blocked_users WHERE user_id = ? AND chat_id = ? LIMIT 1",
                    (user_id, chat_id),
                ).fetchone()
            return row is not None

    def is_user_banned_globally(self, user_id: int) -> bool:
        """True when `user_id` has a global (GLOBAL_CHAT_ID) ban row.
        Used by the admin panel. A per-chat
        override does not lift a global ban check — it only allows the
        user into that one chat."""
        with self._lock, self._get_conn() as conn:
            row = conn.execute(
                "SELECT 1 FROM blocked_users WHERE user_id = ? AND chat_id = ? LIMIT 1",
                (user_id, GLOBAL_CHAT_ID),
            ).fetchone()
            return row is not None

    def list_banned_users(self, limit: int = 20) -> list[dict[str, Any]]:
        """Banned users for the admin panel: user id, scope (global or a
        chat id), who banned them and when. Most recent first."""
        with self._lock, self._get_conn() as conn:
            rows = conn.execute(
                "SELECT user_id, chat_id, banned_by, banned_at FROM blocked_users "
                "ORDER BY banned_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
            return [dict(r) for r in rows]

    # ------------------------------------------------------------------
    # Runtime settings (bot_settings key/value) + allowlist + managers
    # ------------------------------------------------------------------

    def get_setting(self, key: str, default: str | None = None) -> str | None:
        """Read a runtime setting (bot_settings table). None when unset."""
        with self._lock, self._get_conn() as conn:
            row = conn.execute(
                "SELECT value FROM bot_settings WHERE key = ? LIMIT 1", (key,)
            ).fetchone()
            return row["value"] if row else default

    def set_setting(self, key: str, value: str) -> None:
        """Write a runtime setting (upsert)."""
        with self._lock, self._get_conn() as conn:
            conn.execute(
                "INSERT INTO bot_settings (key, value) VALUES (?, ?) "
                "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
                (key, value),
            )
            conn.commit()

    def delete_setting(self, key: str) -> None:
        """Remove a runtime setting."""
        with self._lock, self._get_conn() as conn:
            conn.execute("DELETE FROM bot_settings WHERE key = ?", (key,))
            conn.commit()

    def is_bot_enabled(self) -> bool:
        """Public mode (/on) when True (default); private mode (/off)
        when False — only the boss, managers and allowlisted users."""
        return self.get_setting("bot_enabled", "1") != "0"

    def set_bot_enabled(self, enabled: bool) -> None:
        """Persist the /on / /off state."""
        self.set_setting("bot_enabled", "1" if enabled else "0")

    def get_country(self, default: str = "United States") -> str:
        """The bot's country (English name) from bot_settings, falling
        back to `default` (the BOT_COUNTRY env value at runtime, the
        hardcoded default otherwise). Precedence: DB > env > default."""
        return self.get_setting("country", default) or default

    def set_country(self, value: str) -> None:
        """Persist the bot's country (English name)."""
        self.set_setting("country", value)

    def get_language(self, default: str = "en") -> str:
        """The bot's language code from bot_settings, falling back to
        `default` (the BOT_LANGUAGE env value at runtime, "en"
        otherwise). Precedence: DB > env > default."""
        return self.get_setting("language", default) or default

    def set_language(self, value: str) -> None:
        """Persist the bot's language code."""
        self.set_setting("language", value)

    def get_image_model(self) -> str:
        """Image-generation choice: 'duckai' (free, default),
        'hilinkup:<model>' (that HiLinkUp image model first), 'custom'
        (the custom provider in get_image_provider), or 'none' (image
        generation disabled)."""
        return self.get_setting("image_model", "duckai") or "duckai"

    def set_image_model(self, value: str) -> None:
        """Persist the image-generation choice."""
        self.set_setting("image_model", value)

    def get_image_provider(self) -> tuple[str, str, str] | None:
        """The custom image provider (base_url, key, model) from
        bot_settings 'image_provider' (pipe-separated), or None when
        unset or malformed. Set from /admin (validated live first)."""
        raw = self.get_setting("image_provider", "") or ""
        parts = [p.strip() for p in raw.split("|")]
        if len(parts) != 3 or not all(parts):
            return None
        return (parts[0].rstrip("/"), parts[1], parts[2])

    def set_image_provider(self, base_url: str, key: str, model: str) -> None:
        """Persist the custom image provider (pipe-separated)."""
        self.set_setting("image_provider", f"{base_url.rstrip('/')}|{key}|{model}")

    def clear_image_provider(self) -> None:
        """Remove the custom image provider."""
        self.delete_setting("image_provider")

    def is_user_allowlisted(self, user_id: int) -> bool:
        """True when `user_id` is on the private-mode allowlist."""
        with self._lock, self._get_conn() as conn:
            row = conn.execute(
                "SELECT 1 FROM allowlist WHERE user_id = ? LIMIT 1", (user_id,)
            ).fetchone()
            return row is not None

    def add_to_allowlist(self, user_id: int, added_by: int) -> bool:
        """Add a user to the allowlist. False when already listed."""
        with self._lock, self._get_conn() as conn:
            row = conn.execute(
                "SELECT 1 FROM allowlist WHERE user_id = ? LIMIT 1", (user_id,)
            ).fetchone()
            if row:
                return False
            conn.execute(
                "INSERT INTO allowlist (user_id, added_by, added_at) "
                "VALUES (?, ?, ?)",
                (user_id, added_by, datetime.now(timezone.utc).isoformat()),
            )
            conn.commit()
            return True

    def remove_from_allowlist(self, user_id: int) -> bool:
        """Remove a user from the allowlist. False when not listed."""
        with self._lock, self._get_conn() as conn:
            cur = conn.execute(
                "DELETE FROM allowlist WHERE user_id = ?", (user_id,)
            )
            conn.commit()
            return cur.rowcount > 0

    def list_allowlist(self, limit: int = 20) -> list[dict[str, Any]]:
        """Allowlisted users, most recent first."""
        with self._lock, self._get_conn() as conn:
            rows = conn.execute(
                "SELECT user_id, added_by, added_at FROM allowlist "
                "ORDER BY added_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
            return [dict(r) for r in rows]

    def is_manager(self, user_id: int) -> bool:
        """True when `user_id` is a boss-appointed manager."""
        with self._lock, self._get_conn() as conn:
            row = conn.execute(
                "SELECT 1 FROM managers WHERE user_id = ? LIMIT 1", (user_id,)
            ).fetchone()
            return row is not None

    def get_manager_perms(self, user_id: int) -> set[str]:
        """A manager's permission names (empty set when not a manager)."""
        with self._lock, self._get_conn() as conn:
            row = conn.execute(
                "SELECT permissions FROM managers WHERE user_id = ? LIMIT 1",
                (user_id,),
            ).fetchone()
            if not row:
                return set()
            return {p.strip() for p in (row["permissions"] or "").split(",") if p.strip()}

    def list_managers(self, limit: int = 20) -> list[dict[str, Any]]:
        """Managers with their permissions, most recent first."""
        with self._lock, self._get_conn() as conn:
            rows = conn.execute(
                "SELECT user_id, permissions, added_by, added_at FROM managers "
                "ORDER BY added_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
            return [dict(r) for r in rows]

    def add_manager(self, user_id: int, added_by: int, perms: set[str] | None = None) -> bool:
        """Add a manager (starts with no permissions unless given).
        False when already a manager."""
        with self._lock, self._get_conn() as conn:
            row = conn.execute(
                "SELECT 1 FROM managers WHERE user_id = ? LIMIT 1", (user_id,)
            ).fetchone()
            if row:
                return False
            conn.execute(
                "INSERT INTO managers (user_id, permissions, added_by, added_at) "
                "VALUES (?, ?, ?, ?)",
                (user_id, ",".join(sorted(perms or set())), added_by, datetime.now(timezone.utc).isoformat()),
            )
            conn.commit()
            return True

    def remove_manager(self, user_id: int) -> bool:
        """Remove a manager. False when not a manager."""
        with self._lock, self._get_conn() as conn:
            cur = conn.execute(
                "DELETE FROM managers WHERE user_id = ?", (user_id,)
            )
            conn.commit()
            return cur.rowcount > 0

    def set_manager_perms(self, user_id: int, perms: set[str]) -> bool:
        """Replace a manager's permissions. False when not a manager."""
        with self._lock, self._get_conn() as conn:
            cur = conn.execute(
                "UPDATE managers SET permissions = ? WHERE user_id = ?",
                (",".join(sorted(perms)), user_id),
            )
            conn.commit()
            return cur.rowcount > 0

    def ban_user(
        self,
        chat_id: int,
        target_user_id: int,
        actor_id: int,
        global_ban: bool = False,
    ) -> bool:
        """
        Adds `target_user_id` to `blocked_users`.
        Returns True if newly banned, False if the user was already banned.
        Also records an audit log entry.
        """
        effective_chat_id = GLOBAL_CHAT_ID if global_ban else chat_id
        now_iso = datetime.now(timezone.utc).isoformat()

        with self._lock, self._get_conn() as conn:
            existing = conn.execute(
                "SELECT 1 FROM blocked_users WHERE chat_id = ? AND user_id = ?",
                (effective_chat_id, target_user_id),
            ).fetchone()
            if existing:
                return False

            conn.execute(
                "INSERT INTO blocked_users (chat_id, user_id, banned_by, banned_at) VALUES (?, ?, ?, ?)",
                (effective_chat_id, target_user_id, actor_id, now_iso),
            )
            conn.execute(
                "INSERT INTO ban_audit_logs (action, actor_id, target_user_id, chat_id, created_at) "
                "VALUES (?, ?, ?, ?, ?)",
                ("BAN", actor_id, target_user_id, effective_chat_id, now_iso),
            )
        logger.info(
            "BAN_AUDIT | action=BAN actor_id=%s target_user_id=%s chat_id=%s global=%s at=%s",
            actor_id,
            target_user_id,
            chat_id,
            global_ban,
            now_iso,
        )
        return True

    def unban_user(
        self,
        chat_id: int,
        target_user_id: int,
        actor_id: int,
        global_ban: bool = False,
    ) -> bool:
        """
        Removes `target_user_id` from `blocked_users`.
        Returns True if unbanned, False if the user was not banned.
        Also records an audit log entry.
        """
        now_iso = datetime.now(timezone.utc).isoformat()
        with self._lock, self._get_conn() as conn:
            override_added = False
            if global_ban:
                cursor = conn.execute(
                    "DELETE FROM blocked_users WHERE user_id = ? AND chat_id IN (?, ?)",
                    (target_user_id, chat_id, GLOBAL_CHAT_ID),
                )
                # A global unban also clears any per-chat override.
                conn.execute(
                    "DELETE FROM ban_overrides WHERE user_id = ?",
                    (target_user_id,),
                )
            else:
                cursor = conn.execute(
                    "DELETE FROM blocked_users WHERE user_id = ? AND chat_id = ?",
                    (target_user_id, chat_id),
                )
                # Per-chat unban of a GLOBALLY banned user: the global ban
                # still blocks them, so record a per-chat override that
                # lets them back into THIS chat only.
                still_global = conn.execute(
                    "SELECT 1 FROM blocked_users WHERE user_id = ? AND chat_id = ? LIMIT 1",
                    (target_user_id, GLOBAL_CHAT_ID),
                ).fetchone()
                if still_global:
                    cur2 = conn.execute(
                        "INSERT OR IGNORE INTO ban_overrides (chat_id, user_id) VALUES (?, ?)",
                        (chat_id, target_user_id),
                    )
                    override_added = cur2.rowcount > 0
            removed = cursor.rowcount > 0 or override_added
            if removed:
                conn.execute(
                    "INSERT INTO ban_audit_logs (action, actor_id, target_user_id, chat_id, created_at) "
                    "VALUES (?, ?, ?, ?, ?)",
                    ("UNBAN", actor_id, target_user_id, chat_id, now_iso),
                )
        if removed:
            logger.info(
                "BAN_AUDIT | action=UNBAN actor_id=%s target_user_id=%s chat_id=%s global=%s at=%s",
                actor_id,
                target_user_id,
                chat_id,
                global_ban,
                now_iso,
            )
        return removed

    # ------------------------------------------------------------------
    # Per-User Per-Group Isolated Context (chat_id + user_id)
    # ------------------------------------------------------------------

    def get_user_context(self, chat_id: int, user_id: int) -> dict[str, Any]:
        """
        Returns the isolated context for `(chat_id, user_id)`:
        - `rolling_summary`: str
        - `last_file_summary`: str
        - `messages`: list of `{"id": int, "role": str, "content": str}`
        """
        with self._lock, self._get_conn() as conn:
            ctx_row = conn.execute(
                "SELECT rolling_summary, last_file_summary FROM user_contexts WHERE chat_id = ? AND user_id = ?",
                (chat_id, user_id),
            ).fetchone()
            rolling_summary = ctx_row["rolling_summary"] if ctx_row else ""
            last_file_summary = ctx_row["last_file_summary"] if ctx_row else ""

            msg_rows = conn.execute(
                "SELECT id, role, content FROM user_messages WHERE chat_id = ? AND user_id = ? ORDER BY id ASC",
                (chat_id, user_id),
            ).fetchall()
            messages = [
                {"id": r["id"], "role": r["role"], "content": r["content"]}
                for r in msg_rows
            ]

            return {
                "rolling_summary": rolling_summary,
                "last_file_summary": last_file_summary,
                "messages": messages,
            }

    def append_message(self, chat_id: int, user_id: int, role: str, content: str) -> None:
        """Appends a message strictly to `(chat_id, user_id)` history."""
        now_iso = datetime.now(timezone.utc).isoformat()
        with self._lock, self._get_conn() as conn:
            conn.execute(
                """
                INSERT INTO user_contexts (chat_id, user_id, rolling_summary, last_file_summary, updated_at)
                VALUES (?, ?, '', '', ?)
                ON CONFLICT(chat_id, user_id) DO UPDATE SET updated_at = excluded.updated_at
                """,
                (chat_id, user_id, now_iso),
            )
            conn.execute(
                "INSERT INTO user_messages (chat_id, user_id, role, content, created_at) VALUES (?, ?, ?, ?, ?)",
                (chat_id, user_id, role, content, now_iso),
            )

    def update_rolling_summary_and_prune(
        self,
        chat_id: int,
        user_id: int,
        new_summary: str,
        keep_last_n: int,
    ) -> None:
        """
        Saves the updated rolling summary for `(chat_id, user_id)` and deletes older
        messages so only the most recent `keep_last_n` messages remain in the window.
        """
        now_iso = datetime.now(timezone.utc).isoformat()
        with self._lock, self._get_conn() as conn:
            conn.execute(
                """
                INSERT INTO user_contexts (chat_id, user_id, rolling_summary, last_file_summary, updated_at)
                VALUES (?, ?, ?, '', ?)
                ON CONFLICT(chat_id, user_id) DO UPDATE SET
                    rolling_summary = excluded.rolling_summary,
                    updated_at = excluded.updated_at
                """,
                (chat_id, user_id, new_summary, now_iso),
            )
            conn.execute(
                """
                DELETE FROM user_messages
                WHERE chat_id = ? AND user_id = ? AND id NOT IN (
                    SELECT id FROM user_messages
                    WHERE chat_id = ? AND user_id = ?
                    ORDER BY id DESC
                    LIMIT ?
                )
                """,
                (chat_id, user_id, chat_id, user_id, keep_last_n),
            )

    def set_file_summary(self, chat_id: int, user_id: int, file_summary: str) -> None:
        """Stores a short summary of the user's last processed file in their isolated context."""
        now_iso = datetime.now(timezone.utc).isoformat()
        with self._lock, self._get_conn() as conn:
            conn.execute(
                """
                INSERT INTO user_contexts (chat_id, user_id, rolling_summary, last_file_summary, updated_at)
                VALUES (?, ?, '', ?, ?)
                ON CONFLICT(chat_id, user_id) DO UPDATE SET
                    last_file_summary = excluded.last_file_summary,
                    updated_at = excluded.updated_at
                """,
                (chat_id, user_id, file_summary, now_iso),
            )

    def clear_user_context(self, chat_id: int, user_id: int) -> None:
        """
        Clears ONLY the specified `(chat_id, user_id)` conversation history,
        rolling summary, and file summary (used when user says 'ورتکس فراموشم کن').
        """
        with self._lock, self._get_conn() as conn:
            conn.execute(
                "DELETE FROM user_messages WHERE chat_id = ? AND user_id = ?",
                (chat_id, user_id),
            )
            conn.execute(
                "DELETE FROM user_contexts WHERE chat_id = ? AND user_id = ?",
                (chat_id, user_id),
            )

    # ------------------------------------------------------------------
    # Daily per-user message quota (30/day, Boss exempt — enforced in handlers)
    # ------------------------------------------------------------------

    _TEHRAN_TZ = ZoneInfo("Asia/Tehran")

    @staticmethod
    def _today_tehran() -> str:
        """Current date as 'YYYY-MM-DD' in the bot's country timezone
        (the quota day). Named _today_tehran for backward compatibility;
        the timezone now follows the configured country, so the quota
        resets at local midnight, not Tehran midnight."""
        try:
            from bot.countries import country_today, current_country_name

            return country_today(current_country_name())
        except Exception:
            return datetime.now(ZoneInfo("Asia/Tehran")).strftime("%Y-%m-%d")

    def check_and_record_daily_use(
        self, user_id: int, limit: int
    ) -> tuple[bool, int, int]:
        """Atomically check + increment today's usage for `user_id`.
        Returns (allowed, used_today, remaining). When used_today < limit
        the counter is incremented and (True, used+1, limit-(used+1)) is
        returned; otherwise (False, used, 0) with no increment."""
        today = self._today_tehran()
        with self._lock, self._get_conn() as conn:
            # Prune quota rows older than 30 days so the table does not
            # grow forever (one row per user per day).
            cutoff = (datetime.now(timezone.utc) - timedelta(days=30)).strftime("%Y-%m-%d")
            conn.execute("DELETE FROM daily_usage WHERE day < ?", (cutoff,))
            row = conn.execute(
                "SELECT count FROM daily_usage WHERE user_id = ? AND day = ?",
                (user_id, today),
            ).fetchone()
            used = int(row["count"]) if row else 0
            if used >= limit:
                return (False, used, 0)
            conn.execute(
                """
                INSERT INTO daily_usage (user_id, day, count) VALUES (?, ?, 1)
                ON CONFLICT(user_id, day) DO UPDATE SET count = count + 1
                """,
                (user_id, today),
            )
            return (True, used + 1, limit - (used + 1))

    def get_daily_use(self, user_id: int, limit: int) -> tuple[int, int]:
        """(used_today, remaining) for `user_id` without incrementing."""
        today = self._today_tehran()
        with self._lock, self._get_conn() as conn:
            row = conn.execute(
                "SELECT count FROM daily_usage WHERE user_id = ? AND day = ?",
                (user_id, today),
            ).fetchone()
            used = int(row["count"]) if row else 0
            return (used, max(0, limit - used))

    def refund_daily_use(self, user_id: int) -> None:
        """Give back one daily-quota unit (e.g. the bot's reply failed
        after quota was already charged). The counter never goes below 0.
        Quota is charged up front in the handler so the daily limit can
        be enforced before expensive work starts; failures after that
        point refund the unit instead of silently consuming it."""
        today = self._today_tehran()
        with self._lock, self._get_conn() as conn:
            conn.execute(
                """
                UPDATE daily_usage SET count = MAX(count - 1, 0)
                WHERE user_id = ? AND day = ?
                """,
                (user_id, today),
            )

    # ------------------------------------------------------------------
    # Member / group tracking (powers the boss-only «ورتکس آمار»)
    # ------------------------------------------------------------------

    def upsert_chat_user(
        self, chat_id: int, user_id: int, first_name: str, username: str
    ) -> None:
        """Record that `user_id` was seen in `chat_id`: refresh name /
        username / last-seen and bump the per-chat message count by 1."""
        now_iso = datetime.now(timezone.utc).isoformat()
        with self._lock, self._get_conn() as conn:
            conn.execute(
                """
                INSERT INTO chat_users
                    (chat_id, user_id, first_name, username, last_seen_at, message_count)
                VALUES (?, ?, ?, ?, ?, 1)
                ON CONFLICT(chat_id, user_id) DO UPDATE SET
                    first_name = excluded.first_name,
                    username = excluded.username,
                    last_seen_at = excluded.last_seen_at,
                    message_count = message_count + 1
                """,
                (chat_id, user_id, first_name or "", username or "", now_iso),
            )

    def list_known_groups(self) -> list[int]:
        """Distinct group chat_ids (chat_id < 0) the bot has seen."""
        with self._lock, self._get_conn() as conn:
            rows = conn.execute(
                "SELECT DISTINCT chat_id FROM chat_users WHERE chat_id < 0"
            ).fetchall()
            return [int(r["chat_id"]) for r in rows]

    def list_group_members(self, chat_id: int) -> list[dict[str, Any]]:
        """Members seen in `chat_id`, most active first."""
        with self._lock, self._get_conn() as conn:
            rows = conn.execute(
                """
                SELECT user_id, first_name, username, message_count
                FROM chat_users WHERE chat_id = ?
                ORDER BY message_count DESC, user_id ASC
                """,
                (chat_id,),
            ).fetchall()
            return [
                {
                    "user_id": int(r["user_id"]),
                    "first_name": r["first_name"] or "",
                    "username": r["username"] or "",
                    "message_count": int(r["message_count"]),
                }
                for r in rows
            ]

    def count_all_members(self) -> int:
        """Distinct user_ids seen anywhere (all groups + PV)."""
        with self._lock, self._get_conn() as conn:
            row = conn.execute(
                "SELECT COUNT(DISTINCT user_id) AS n FROM chat_users"
            ).fetchone()
            return int(row["n"]) if row else 0

    def list_recent_chat_history(
        self, limit: int = 30, exclude_user_id: int | None = None
    ) -> list[dict[str, Any]]:
        """Most recent (user, assistant) messages from everyone except
        `exclude_user_id` (the boss's own questions are not 'other people
        chatting'). Oldest first, capped at `limit` rows. Powers the
        boss-only chat-history fast path."""
        with self._lock, self._get_conn() as conn:
            if exclude_user_id is not None:
                rows = conn.execute(
                    """
                    SELECT m.user_id, m.role, m.content, m.created_at,
                           c.first_name, c.username
                    FROM user_messages m
                    LEFT JOIN chat_users c
                      ON m.chat_id = c.chat_id AND m.user_id = c.user_id
                    WHERE m.user_id != ?
                    ORDER BY m.id DESC LIMIT ?
                    """,
                    (exclude_user_id, limit),
                ).fetchall()
            else:
                rows = conn.execute(
                    """
                    SELECT m.user_id, m.role, m.content, m.created_at,
                           c.first_name, c.username
                    FROM user_messages m
                    LEFT JOIN chat_users c
                      ON m.chat_id = c.chat_id AND m.user_id = c.user_id
                    ORDER BY m.id DESC LIMIT ?
                    """,
                    (limit,),
                ).fetchall()
            rows = list(reversed(rows))
            return [
                {
                    "user_id": int(r["user_id"]),
                    "role": r["role"],
                    "content": r["content"],
                    "created_at": r["created_at"],
                    "first_name": r["first_name"] or "",
                    "username": r["username"] or "",
                }
                for r in rows
            ]
