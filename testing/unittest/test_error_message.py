import itertools
import unittest
from datetime import datetime
from typing import Sequence
from zoneinfo import ZoneInfo


def get_datetimes() -> Sequence[tuple[datetime]]:
    zones = tuple(
        map(ZoneInfo, ("UTC", "America/New_York", "America/Chicago", "Asia/Atyrau"))
    )
    dates = (
        datetime(1970, 1, 1),
        datetime(2024, 5, 16, 1, 14),
        datetime(2024, 1, 2, 15, 22),
        datetime(2000, 2, 29),
        datetime(2000, 4, 1),
    )

    zoned_dts = [
        dt.replace(tzinfo=tzinfo) for dt, tzinfo in itertools.product(dates, zones)
    ]
    out = []
    for dt1 in zoned_dts:
        for dt2 in zoned_dts:
            out.append((dt1, dt2))
    return out


class Tests(unittest.TestCase):
    def test_timestamp(self):
        for dt_1, dt_2 in get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
            self.assertEqual(ts2, dt_rt.timestamp())
