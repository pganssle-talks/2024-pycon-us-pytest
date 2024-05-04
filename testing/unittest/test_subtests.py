import unittest
from datetime import datetime, UTC

class Tests(unittest.TestCase):
    def test_fromisoformat(self):
        cases = [
            "2025-01-01T01+00:00",
            "2025-01-01T01:00+00:00",
            "badstring",  # Raises exception
            "2025-01-01T01:00:00+00:00",
            "2025-01-01T02:00:00+00:00",  # Value is wrong
        ]

        expected_datetime = datetime(2025, 1, 1, 1, tzinfo=UTC)

        for case in cases:
            with self.subTest(case):
                self.assertEqual(datetime.fromisoformat(case), expected_datetime)
