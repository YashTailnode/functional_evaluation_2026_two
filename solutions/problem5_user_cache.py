from collections.abc import Callable
from threading import Lock
from typing import Any


class ThreadSafeUserCache:

    def __init__(self, fetch_user: Callable[[str], Any]):
        self._fetch_user = fetch_user
        self._cache: dict[str, Any] = {}
        self._key_locks: dict[str, Lock] = {}
        self._key_locks_guard = Lock()

    def get_user(self, user_id: str) -> Any:
        lock = self._lock_for(user_id)

        with lock:
            if user_id not in self._cache:
                self._cache[user_id] = self._fetch_user(user_id)

            return self._cache[user_id]

    def _lock_for(self, user_id: str) -> Lock:
        with self._key_locks_guard:
            if user_id not in self._key_locks:
                self._key_locks[user_id] = Lock()

            return self._key_locks[user_id]

