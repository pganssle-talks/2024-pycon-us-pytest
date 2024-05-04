import pytest
import sys


@pytest.mark.skipif(sys.version_info < (3, 10), reason="Uses feature from 3.10")
def test_skipped():
    assert (14).bit_count() == 3


@pytest.mark.xfail(strict=True, reason="Always fails")
def test_xfail():
    assert False


@pytest.mark.xfail(strict=True, reason="Always fails")
def test_xpass():
    assert True
