import pytest

def test_light_thing():
    assert 1 + 1 == 2

@pytest.mark.heavy
def test_heavy_thing():
    assert calculate_digit_of_e(1_000_000_000) == 4
