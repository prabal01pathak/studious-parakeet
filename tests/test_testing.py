from testing import __version__
from testing.sum import sum_two, call_seconds


def test_version():
    assert __version__ == '0.1.0'


def test_sum():
    assert sum(1, 2) == 3


def test_call_seconds():
    assert call_seconds() == 3
