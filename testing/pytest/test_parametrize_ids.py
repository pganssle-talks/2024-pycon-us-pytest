import pytest

@pytest.mark.parametrize("x,expected", [
    (1, 1),
    (2, 4),
    (0, 0),
    (-4, 16),
], ids=[None, None, "zero", "negative"])
def test_square(x, expected):
    assert x**2 == expected
