from datetime import datetime, timezone
import sys

import pytest
UTC = timezone.utc


#fmt: off
@pytest.mark.parametrize("dt_str", [
    "2025-01-01T01+00:00",
    "2025-01-01T01:00+00:00",
    "2025-01-01T01:00:00+00:00",
    pytest.param("2025-01-01T01:00:00Z",
                 marks=pytest.mark.xfail(sys.version_info < (3, 11),
                                         reason="Z is not supported")),
])
def test_fromisoformat(dt_str: str) -> None:
    expected_datetime = datetime(2025, 1, 1, 1, tzinfo=UTC)
    assert datetime.fromisoformat(dt_str) == expected_datetime
#fmt: on
