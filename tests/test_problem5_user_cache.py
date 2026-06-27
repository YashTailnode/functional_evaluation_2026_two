from concurrent.futures import ThreadPoolExecutor
from time import sleep
import unittest

from solutions.problem5_user_cache import ThreadSafeUserCache


class ThreadSafeUserCacheTest(unittest.TestCase):
    def test_fetches_user_once_for_cached_id(self):
        calls = []

        def fetch_user(user_id):
            calls.append(user_id)
            return {"id": user_id}

        cache = ThreadSafeUserCache(fetch_user)

        self.assertEqual(cache.get_user("42"), {"id": "42"})
        self.assertEqual(cache.get_user("42"), {"id": "42"})
        self.assertEqual(calls, ["42"])

    def test_caches_falsy_values(self):
        calls = []

        def fetch_user(user_id):
            calls.append(user_id)
            return None

        cache = ThreadSafeUserCache(fetch_user)

        self.assertIsNone(cache.get_user("missing"))
        self.assertIsNone(cache.get_user("missing"))
        self.assertEqual(calls, ["missing"])

    def test_concurrent_requests_for_same_user_share_one_fetch(self):
        calls = []

        def fetch_user(user_id):
            sleep(0.02)
            calls.append(user_id)
            return {"id": user_id}

        cache = ThreadSafeUserCache(fetch_user)

        with ThreadPoolExecutor(max_workers=8) as executor:
            results = list(executor.map(cache.get_user, ["42"] * 8))

        self.assertEqual(results, [{"id": "42"}] * 8)
        self.assertEqual(calls, ["42"])


if __name__ == "__main__":
    unittest.main()
