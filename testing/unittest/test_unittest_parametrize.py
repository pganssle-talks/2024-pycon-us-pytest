from datetime import datetime, UTC
import unittest_parametrize
from unittest_parametrize import parametrize, param

class Tests(unittest_parametrize.ParametrizedTestCase):
    @parametrize("dt_str", [
        ("2025-01-01T01+00:00",),
        ("2025-01-01T01:00+00:00",),
        ("2025-01-01T01:00:00+00:00",),
    ])
    def test_fromisoformat(self, dt_str):
        expected_datetime = datetime(2025, 1, 1, 1, tzinfo=UTC)
        self.assertEqual(datetime.fromisoformat(dt_str), expected_datetime)

    @parametrize("x,expected", [
        param(1, 1),
        param(2, 4),
        param(0, 0,),
        param(-4, 16),
    ], ids=[None, None, "zero", "negative"])
    def test_square(self, x, expected):
        self.assertEqual(x**2, expected)


