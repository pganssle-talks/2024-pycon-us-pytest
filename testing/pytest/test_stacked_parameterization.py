import pytest

@pytest.mark.parametrize("x", [4, 5, 6])
@pytest.mark.parametrize("y", [3, 2, 1])
def test_multiply(x, y):
    z = x * y
    assert z > x and z > y
