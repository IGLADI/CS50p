import pytest
from jar import Jar  


def test_init_valid_capacity():
    jar = Jar(10)
    assert jar._capacity == 10
    assert jar._cookies == 0


def test_init_invalid_capacity():
    with pytest.raises(ValueError, match="Capacity must be positive"):
        Jar(capacity=-5)


def test_str():
    jar = Jar(capacity=5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit_valid():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5


def test_deposit_invalid():
    jar = Jar(capacity=5)
    with pytest.raises(ValueError, match="Too many cookies"):
        jar.deposit(10)


def test_withdraw_valid():
    jar = Jar(capacity=8)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2


def test_withdraw_invalid():
    jar = Jar(capacity=5)
    with pytest.raises(ValueError, match="Not enough cookies"):
        jar.withdraw(3)


def test_capacity():
    jar = Jar(capacity=15)
    assert jar._capacity == 15


def test_size():
    jar = Jar()
    jar.deposit(7)
    assert jar._cookies == 7
