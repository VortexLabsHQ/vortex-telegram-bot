"""Token pool for the Vortex bot: multiple LLM providers, each with its own
base URL, API key and model, with health checks, random rotation,
rate-limit failover, and a quarantine ("dead folder") for keys that stop
working.

- Providers come from LLM_PROVIDERS (comma-separated) in .env, each entry
  `base_url|key|model` (base URL first, then the API key, then the model to
  use on that provider). Falls back to the old single-provider vars
  (LLM_BASE_URL + LLM_API_KEYS + LLM_MODEL) when LLM_PROVIDERS is empty.
  This lets Moz use several providers (e.g. TokenHarbor + IteraCompute)
  and fail over between them.
- Every TOKEN_HEALTH_CHECK_INTERVAL_SECONDS (default 1800 = 30 min) each
  key is tested with a cheap GET {its own base_url}/models call. Keys that
  fail are quarantined (see below); healthy keys are candidates for the
  active slot.
- The active entry is picked at random among healthy entries (rotation).
  A chat call uses the active entry's base URL, key AND model, so a
  failover can switch provider entirely.
- When a chat call hits a rate limit (429) or an auth error (401), that
  key is quarantined immediately and the call is retried with a different
  random healthy entry (possibly another provider).
- QUARANTINE ("dead folder"): a key that fails is moved OUT of the active
  pool and into a separate JSON file (TOKEN_DEAD_PATH, default
  data/dead_tokens.json, mode 0600). It stays there until the recovery job
  tests it. If it is the LAST healthy key, it is NOT quarantined (just
  marked unhealthy in memory) so a single-key setup never goes down for
  10 hours — the 30-min health check brings it back when its quota resets.
- RECOVERY: every TOKEN_DEAD_RETRY_INTERVAL_SECONDS (default 36000 = 10 h)
  the recovery job tests every quarantined key against its own provider's
  base URL; a key that answers is removed from the dead file and added
  back to the active pool.
- On startup the pool loads the dead file and excludes those keys from the
  active set, so a quarantined key is not resurrected by a restart.
- Keys are never logged or returned in full; only a short prefix+suffix is
  used for identification in logs.
"""

from __future__ import annotations

import asyncio
import json
import logging
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

from bot.config import ProviderEntry

logger = logging.getLogger(__name__)


def _short(key: str) -> str:
    # First 9 + last 4 chars: keys sharing a prefix (e.g. all TokenHarbor
    # keys start 'thk_live_') still get distinct labels.
    return (key[:9] + "…" + key[-4:]) if len(key) > 13 else key


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class TokenPool:
    def __init__(
        self,
        entries: list[ProviderEntry],
        dead_path: Path | None = None,
        pinned_model: str | None = None,
        manual_selection: str | None = None,
    ) -> None:
        # Dedupe by (base_url, key, model), drop empties, keep order.
        # NOTE: the SAME key may serve DIFFERENT models on one provider
        # (e.g. one NVIDIA key for both deepseek-v4.1-flash and
        # nemotron-3-ultra). Deduping by key alone silently dropped the
        # second model — the pinned Nemotron entry never reached the pool,
        # so pick_active() could never return it and the bot fell back to
        # a random provider. Only an exact (base_url, key, model) repeat
        # is a true duplicate.
        seen: set[tuple[str, str, str]] = set()
        self.entries: list[ProviderEntry] = []
        for e in entries:
            k = (e.key or "").strip()
            ident = (e.base_url.rstrip("/"), k, (e.model or "").strip())
            if k and ident not in seen:
                seen.add(ident)
                self.entries.append(
                    ProviderEntry(
                        base_url=e.base_url.rstrip("/"), key=k, model=e.model
                    )
                )
        if not self.entries:
            raise ValueError("TokenPool needs at least one provider entry.")
        self.dead_path = dead_path
        # Pinned model (e.g. deepseek-ai/deepseek-v4.1-flash): when set and
        # healthy, it is ALWAYS the active entry (no random rotation). It
        # only changes when the pinned entry stops working (quarantined /
        # unhealthy), and it is re-picked as soon as it recovers.
        self._pinned_model = (pinned_model or "").strip()
        # Manual selection from /admin (base_url, model) chosen by the boss:
        # it wins over the pinned model in pick_active() while the entry is
        # healthy. Format in .env: LLM_MANUAL_SELECTION=base_url|model.
        # Cleared from /admin ("خودکار") or by passing "".
        self._manual: tuple[str, str] | None = None
        if manual_selection:
            parts = [p.strip() for p in manual_selection.split("|")]
            if len(parts) == 2 and all(parts):
                self._manual = (parts[0].rstrip("/"), parts[1])
        self._healthy: set[str] = {e.key for e in self.entries}
        # Short in-memory cooldowns for rate-limited keys (429). A 429 is
        # usually a per-minute limit, so the key is parked for a couple of
        # minutes instead of being quarantined into the dead file for 10 h.
        # Keys on cooldown are excluded from healthy_entries until the
        # cooldown expires. This is in-memory only; a restart clears it.
        # Initialized BEFORE pick_active() because healthy_entries reads it.
        self._cooldown_until: dict[str, float] = {}
        self._active: ProviderEntry = self.pick_active() or random.choice(self.entries)
        self._lock = asyncio.Lock()
        # Exclude keys that were quarantined before a restart.
        dead = self._load_dead()
        if dead:
            quarantined = {d["key"] for d in dead if d.get("key") in self._healthy}
            if quarantined:
                # If EVERY key is quarantined, do NOT exclude them all:
                # health_check skips dead keys, so the bot would stay down
                # until retry_dead runs (up to 10 h). Keep them in memory
                # instead; the next health check re-tests and re-quarantines
                # the ones that really fail.
                if quarantined >= {e.key for e in self.entries}:
                    logger.warning(
                        "TokenPool: all %d key(s) are quarantined; keeping them in memory so the health check can re-test them.",
                        len(quarantined),
                    )
                else:
                    self._healthy -= quarantined
                    if self._active.key in quarantined:
                        nxt = self.pick_active()
                        if nxt is not None:
                            self._active = nxt
                    logger.info(
                        "TokenPool loaded %d quarantined key(s) from %s; %d healthy.",
                        len(quarantined),
                        self.dead_path,
                        len(self._healthy),
                    )

    # -- entry lookup -------------------------------------------------------

    def _entry_for_key(self, key: str) -> ProviderEntry | None:
        for e in self.entries:
            if e.key == key:
                return e
        return None

    @property
    def keys(self) -> list[str]:
        return [e.key for e in self.entries]

    @property
    def active_entry(self) -> ProviderEntry:
        return self._active

    @property
    def active_key(self) -> str:
        return self._active.key

    @property
    def healthy_entries(self) -> list[ProviderEntry]:
        # Exclude keys on a rate-limit cooldown (and drop expired ones).
        now = time.monotonic()
        expired = [k for k, until in self._cooldown_until.items() if until <= now]
        for k in expired:
            del self._cooldown_until[k]
        return [
            e
            for e in self.entries
            if e.key in self._healthy and e.key not in self._cooldown_until
        ]

    @property
    def healthy_keys(self) -> list[str]:
        return [e.key for e in self.healthy_entries]

    @staticmethod
    async def probe_entry(base_url: str, key: str) -> bool:
        """Test whether a (base_url, key) pair works: GET {base_url}/models
        with the key. True on HTTP 200. Used to validate a key the boss
        adds from /admin before it joins the pool."""
        url = base_url.rstrip("/") + "/models"
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                r = await client.get(url, headers={"Authorization": "Bearer " + key})
                return r.status_code == 200
        except Exception:
            return False

    async def add_entry(self, entry: ProviderEntry) -> bool:
        """Add a provider entry (from /admin). Returns False when an
        identical (base_url, key, model) entry already exists. A key
        that was previously quarantined is removed from the dead file so
        it can be tested again, and the active entry is re-picked (a new
        entry matching the pinned model becomes active)."""
        ident = (entry.base_url.rstrip("/"), (entry.key or "").strip(), (entry.model or "").strip())
        if not ident[1] or not ident[2]:
            return False
        async with self._lock:
            for e in self.entries:
                if (e.base_url.rstrip("/"), e.key, e.model) == ident:
                    return False
            self.entries.append(
                ProviderEntry(base_url=ident[0], key=ident[1], model=ident[2])
            )
            self._healthy.add(ident[1])
            self._cooldown_until.pop(ident[1], None)
            dead = [d for d in self._load_dead() if d.get("key") != ident[1]]
            self._save_dead(dead)
            nxt = self.pick_active()
            if nxt is not None:
                self._active = nxt
            logger.info("Token %s added to pool (%s).", _short(ident[1]), ident[2])
            return True

    async def remove_entry(self, key: str) -> list[ProviderEntry]:
        """Remove EVERY entry using `key` (one key can serve several
        models on one provider). Also drops the key from the healthy set,
        cooldowns and the dead file, and re-picks the active entry when
        needed. Returns the removed entries (empty when the key was not
        in the pool)."""
        async with self._lock:
            removed = [e for e in self.entries if e.key == key]
            if not removed:
                return []
            self.entries = [e for e in self.entries if e.key != key]
            self._healthy.discard(key)
            self._cooldown_until.pop(key, None)
            dead = [d for d in self._load_dead() if d.get("key") != key]
            self._save_dead(dead)
            if self._active.key == key:
                nxt = self.pick_active()
                if nxt is not None:
                    self._active = nxt
            logger.info(
                "Token %s removed from pool (%d entries).",
                _short(key),
                len(removed),
            )
            return removed

    def describe_entries(self) -> list[dict[str, Any]]:
        """Per-entry status for the boss-only admin panel: provider base
        URL, model, status ('healthy' | 'cooldown' | 'quarantined'),
        whether it is the active entry, and a masked key fingerprint.
        Never returns a full key."""
        now = time.monotonic()
        out: list[dict[str, Any]] = []
        for e in self.entries:
            if e.key in self._cooldown_until and self._cooldown_until[e.key] > now:
                status = "cooldown"
            elif e.key not in self._healthy:
                status = "quarantined"
            else:
                status = "healthy"
            out.append(
                {
                    "base_url": e.base_url,
                    "model": e.model,
                    "status": status,
                    "active": e is self._active,
                    "key_fp": _short(e.key),
                }
            )
        return out

    def pick_random_healthy(self) -> ProviderEntry | None:
        healthy = self.healthy_entries
        if not healthy:
            return None
        return random.choice(healthy)

    def pick_active(self) -> ProviderEntry | None:
        """The entry that should be active: the boss's manual selection
        (from /admin) when it is healthy, then the pinned model when it is
        healthy, otherwise a random healthy entry. This is what makes a
        manual pick 'stick' — rotation and health checks keep returning
        it while it works, and only fall back when it stops working."""
        if self._manual:
            base, model = self._manual
            for e in self.healthy_entries:
                if e.base_url == base and e.model == model:
                    return e
        if self._pinned_model:
            for e in self.healthy_entries:
                if e.model == self._pinned_model:
                    return e
        return self.pick_random_healthy()

    @property
    def manual_selection(self) -> tuple[str, str] | None:
        """The boss's manual (base_url, model) selection, or None."""
        return self._manual

    async def set_manual_selection(
        self, base_url: str, model: str
    ) -> ProviderEntry | None:
        """Set the boss's manual active entry (from /admin). The entry
        must exist in the pool. Returns the new active entry, or None
        when no healthy entry is available. When the chosen entry is not
        healthy, the active entry falls back (pinned, then random) — the
        manual selection is still remembered and applies as soon as the
        entry recovers."""
        async with self._lock:
            self._manual = (base_url.rstrip("/"), (model or "").strip())
            nxt = self.pick_active()
            if nxt is not None:
                self._active = nxt
            logger.info(
                "Manual selection set to %s (%s); active=%s.",
                model,
                base_url,
                _short(self._active.key) if self._active else None,
            )
            return nxt

    async def clear_manual_selection(self) -> ProviderEntry | None:
        """Clear the boss's manual selection (back to pinned model /
        random rotation). Returns the new active entry."""
        async with self._lock:
            self._manual = None
            nxt = self.pick_active()
            if nxt is not None:
                self._active = nxt
            logger.info("Manual selection cleared; active=%s.", _short(nxt.key) if nxt else None)
            return nxt

    async def set_pinned_model(self, model: str) -> ProviderEntry | None:
        """Set the pinned model at runtime (from /admin 'no model' or a
        future pin). Empty string clears the pin (free rotation). The
        manual selection still wins over the pin when set. Returns the
        new active entry."""
        async with self._lock:
            self._pinned_model = (model or "").strip()
            nxt = self.pick_active()
            if nxt is not None:
                self._active = nxt
            logger.info(
                "Pinned model set to %r; active=%s.",
                self._pinned_model,
                _short(nxt.key) if nxt else None,
            )
            return nxt

    @staticmethod
    async def list_models(base_url: str, key: str) -> list[str]:
        """Fetch the model ids a key can use: GET {base_url}/models.
        Returns the ids in provider order, exact duplicates removed.
        Empty list when the provider fails or answers non-200."""
        url = base_url.rstrip("/") + "/models"
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                r = await client.get(url, headers={"Authorization": "Bearer " + key})
                if r.status_code != 200:
                    return []
                data = r.json().get("data", [])
                ids: list[str] = []
                seen: set[str] = set()
                for d in data:
                    mid = (d.get("id") or "").strip() if isinstance(d, dict) else ""
                    if mid and mid not in seen:
                        seen.add(mid)
                        ids.append(mid)
                return ids
        except Exception:
            return []

    @staticmethod
    async def probe_model(base_url: str, key: str, model: str) -> bool:
        """Test whether a model actually answers chat: one minimal chat
        completion (user 'hi', max_tokens 1). True on HTTP 200 with a
        non-empty reply. Used before activating a model the boss picked
        from a key's /models list — a model can be listed yet hang or
        return empty (seen on NVIDIA)."""
        url = base_url.rstrip("/") + "/chat/completions"
        try:
            async with httpx.AsyncClient(timeout=25) as client:
                r = await client.post(
                    url,
                    headers={"Authorization": "Bearer " + key},
                    json={
                        "model": model,
                        "messages": [{"role": "user", "content": "hi"}],
                        "max_tokens": 1,
                    },
                )
                if r.status_code != 200:
                    return False
                choices = r.json().get("choices", [])
                if not choices:
                    return False
                content = (choices[0].get("message") or {}).get("content") or ""
                return bool(str(content).strip())
        except Exception:
            return False

    def healthy_entry_for_base_url(self, base_url: str) -> ProviderEntry | None:
        """A random healthy entry on the given provider base URL (used for
        vision calls, which need a specific provider). None when that
        provider has no healthy key."""
        base = base_url.rstrip("/")
        cands = [e for e in self.healthy_entries if e.base_url == base]
        if not cands:
            return None
        return random.choice(cands)

    # -- dead-file (quarantine) persistence --------------------------------

    def _load_dead(self) -> list[dict]:
        """Read the quarantine file. Returns a list of {key, base_url,
        model, reason, quarantined_at} dicts (empty list when the file is
        missing). Older entries may lack base_url/model."""
        if self.dead_path is None:
            return []
        try:
            if not self.dead_path.exists():
                return []
            data = json.loads(self.dead_path.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return [e for e in data if isinstance(e, dict) and e.get("key")]
            return []
        except Exception as exc:
            logger.warning("Could not read dead-token file %s: %s", self.dead_path, type(exc).__name__)
            return []

    def _save_dead(self, entries: list[dict]) -> None:
        """Write the quarantine file (mode 0600). No-op when no path set."""
        if self.dead_path is None:
            return
        try:
            self.dead_path.parent.mkdir(parents=True, exist_ok=True)
            self.dead_path.write_text(
                json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            try:
                self.dead_path.chmod(0o600)
            except Exception:
                pass
        except Exception as exc:
            logger.warning("Could not write dead-token file %s: %s", self.dead_path, type(exc).__name__)

    def _quarantine_locked(self, key: str, reason: str) -> None:
        """Move a key into the dead file. Caller must hold self._lock."""
        entries = self._load_dead()
        if not any(e.get("key") == key for e in entries):
            ent = self._entry_for_key(key)
            entries.append(
                {
                    "key": key,
                    "base_url": ent.base_url if ent else "",
                    "model": ent.model if ent else "",
                    "reason": reason,
                    "quarantined_at": _now_iso(),
                }
            )
            self._save_dead(entries)
        self._healthy.discard(key)
        logger.warning(
            "Token %s quarantined (%s); %d healthy left.",
            _short(key),
            reason,
            len(self._healthy),
        )

    async def quarantine(self, key: str, reason: str) -> None:
        """Public quarantine: move a key into the dead file and out of the
        healthy set. Picks a new active entry when needed (pinned model
        first, when healthy)."""
        async with self._lock:
            self._quarantine_locked(key, reason)
            if self._active.key == key:
                nxt = self.pick_active()
                if nxt is not None:
                    self._active = nxt

    # -- active-entry selection --------------------------------------------

    async def mark_unhealthy(self, key: str) -> ProviderEntry | None:
        """Mark a key unhealthy for an AUTH failure (401/403) only. When
        other healthy keys remain, the key is QUARANTINED into the dead
        file; when it is the last healthy key it is only marked unhealthy
        in memory (so a single-key setup recovers at the next 30-min
        health check instead of going down for 10 hours). Transient
        failures (timeouts, connection errors, 5xx) and rate limits must
        NOT call this — use rotate_active() / mark_rate_limited() instead,
        or a single slow answer exiles the pinned key for 10 hours.
        Returns the new active entry, or None when no healthy entry remains."""
        async with self._lock:
            others = [k for k in self._healthy if k != key]
            if others:
                self._quarantine_locked(key, "auth_error")
            else:
                self._healthy.discard(key)
                logger.warning(
                    "Token %s marked unhealthy (last healthy key; NOT quarantined).",
                    _short(key),
                )
            nxt = self.pick_active()
            if nxt is not None and nxt != self._active:
                self._active = nxt
                logger.info(
                    "Switched active token to %s (%s).",
                    _short(nxt.key),
                    nxt.base_url,
                )
            return nxt

    async def mark_rate_limited(
        self, key: str, retry_after: float | None = None
    ) -> ProviderEntry | None:
        """Park a rate-limited (429) key on a SHORT in-memory cooldown
        instead of quarantining it for 10 hours. A 429 is usually a
        per-minute limit; the key is excluded from healthy_entries until
        the cooldown expires (default 120 s, or the provider's Retry-After
        when given, capped at 300 s), then it rejoins automatically.
        Picks a new active entry when needed. Returns the new active
        entry, or None when no healthy entry remains."""
        seconds = 120.0
        if retry_after is not None:
            try:
                seconds = min(max(float(retry_after), 5.0), 300.0)
            except (TypeError, ValueError):
                seconds = 120.0
        async with self._lock:
            self._cooldown_until[key] = time.monotonic() + seconds
            logger.warning(
                "Token %s rate-limited; cooling down for %.0fs.",
                _short(key),
                seconds,
            )
            nxt = self.pick_active()
            if nxt is not None and nxt != self._active:
                self._active = nxt
                logger.info(
                    "Switched active token to %s (%s).",
                    _short(nxt.key),
                    nxt.base_url,
                )
            return nxt

    async def rotate_active(self, exclude_key: str) -> ProviderEntry | None:
        """Switch the active entry to a different healthy entry WITHOUT
        quarantining or marking anything unhealthy. Used when a call fails
        transiently (e.g. the model returned an empty reply): the failing
        entry stays healthy and is re-picked by the next health check, so
        a glitch only costs one call instead of a 10-hour exile.
        Returns the new active entry, or None when no other healthy entry exists."""
        async with self._lock:
            others = [e for e in self.healthy_entries if e.key != exclude_key]
            if not others:
                return None
            nxt = random.choice(others)
            if nxt != self._active:
                self._active = nxt
                logger.info(
                    "Temporarily switched active token to %s (%s) (key kept healthy).",
                    _short(nxt.key),
                    nxt.base_url,
                )
            return nxt

    # -- periodic checks ----------------------------------------------------

    async def health_check(self) -> dict[str, bool]:
        """Test every NON-QUARANTINED key once (GET {its own base_url}/models).
        A key that fails is quarantined (when other healthy keys remain). Updates
        the healthy set and re-picks the active entry (pinned model first
        when healthy, otherwise at random among healthy entries). If ALL
        keys fail, state is left untouched (likely a provider/network
        outage, not dead keys) and the previous active entry is kept.
        Returns {key_short_label: ok}."""
        results: dict[str, bool] = {}
        # Only quarantined keys (in the dead file) are the recovery job's
        # work. Keys marked unhealthy in memory must be re-tested here,
        # otherwise they can never come back: health_check used to skip
        # every key not in _healthy, so a key dropped by a transient
        # failure stayed out of the pool until a restart.
        dead_keys = {e.get('key', '') for e in self._load_dead()}
        async with httpx.AsyncClient(timeout=20) as client:
            for ent in self.entries:
                if ent.key in dead_keys:
                    continue  # quarantined keys are the recovery job's work
                ok = False
                try:
                    r = await client.get(
                        ent.base_url + "/models",
                        headers={"Authorization": "Bearer " + ent.key},
                    )
                    ok = r.status_code == 200
                except Exception:
                    ok = False
                results[ent.key] = ok
        async with self._lock:
            if not results:
                return {}
            ok_keys = {k for k, v in results.items() if v}
            failed = [k for k, v in results.items() if not v]
            if not ok_keys:
                logger.warning(
                    "Token health check: ALL %d tested keys failed; keeping previous active entry.",
                    len(results),
                )
                return {_short(k): v for k, v in results.items()}
            # Re-read the dead file under the lock: a key quarantined by
            # mark_unhealthy() while the HTTP loop was running must stay
            # out, and keys retry_dead() revived meanwhile must stay in.
            # Never wholesale-replace _healthy with the stale snapshot.
            current_dead = {e.get("key", "") for e in self._load_dead()}
            for key in failed:
                if key not in current_dead:
                    self._quarantine_locked(key, "health_check_failed")
            self._healthy = ok_keys - current_dead
            nxt = self.pick_active()
            if nxt is not None:
                self._active = nxt
            logger.info(
                "Token health check: %d/%d healthy; active=%s (%s).",
                len(self._healthy),
                len(self.entries),
                _short(self._active.key),
                self._active.base_url,
            )
        return {_short(k): v for k, v in results.items()}

    async def retry_dead(self) -> dict[str, bool]:
        """Recovery job: test every quarantined key once against its own
        provider's base URL. A key that answers is removed from the dead
        file and added back to the active pool. Returns
        {key_short_label: recovered}."""
        entries = self._load_dead()
        if not entries:
            return {}
        recovered: dict[str, bool] = {}
        async with httpx.AsyncClient(timeout=20) as client:
            for entry in entries:
                key = entry.get("key", "")
                if not key:
                    continue
                base = (entry.get("base_url") or "").rstrip("/")
                if not base:
                    ent = self._entry_for_key(key)
                    base = ent.base_url if ent else ""
                if not base:
                    continue
                ok = False
                try:
                    r = await client.get(
                        base + "/models",
                        headers={"Authorization": "Bearer " + key},
                    )
                    ok = r.status_code == 200
                except Exception:
                    ok = False
                recovered[key] = ok
        async with self._lock:
            revived = [k for k, ok in recovered.items() if ok]
            revived_set = set(revived)
            if revived:
                # Re-read the dead file under the lock and remove ONLY the
                # revived keys. The snapshot taken before the HTTP checks
                # is stale: keys quarantined meanwhile must NOT be dropped.
                current = self._load_dead()
                still_dead = [
                    e for e in current if e.get("key") and e["key"] not in revived_set
                ]
                self._save_dead(still_dead)
                for key in revived:
                    if key in self.keys:
                        self._healthy.add(key)
                logger.info(
                    "Dead-token recovery: %d key(s) revived: %s.",
                    len(revived),
                    ", ".join(_short(k) for k in revived),
                )
                # Always re-pick the active entry so a recovered pinned
                # model is restored immediately, not at the next check.
                nxt = self.pick_active()
                if nxt is not None:
                    self._active = nxt
            else:
                still_dead = [
                    e for e in entries if e.get("key") and not recovered.get(e["key"], False)
                ]
                if still_dead:
                    logger.info(
                        "Dead-token recovery: %d key(s) still dead.",
                        len(still_dead),
                    )
        return {_short(k): v for k, v in recovered.items()}
