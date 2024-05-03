import pytest

def test_float_bad():
    a = 0.1 + 0.2
    assert a == 0.3


def test_float_good():
    a = 0.1 + 0.2
    assert a == pytest.approx(0.3)
