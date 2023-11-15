import fuel
import pytest


def test_convert():
    assert fuel.convert("0/4") == 0
    assert fuel.convert("1/2") == 50
    assert fuel.convert("2/2") == 100
    with pytest.raises(ZeroDivisionError):
        fuel.convert("2/0")
    with pytest.raises(ValueError):
        fuel.convert("cat")


def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(2) == "2%"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
