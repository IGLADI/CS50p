import bank


def test_bank_hello():
    assert bank.value("hello") == 0
    assert bank.value("Hello world") == 0


def test_bank_h():
    assert bank.value("h") == 20
    assert bank.value("hi") == 20
    assert bank.value("Hey!") == 20


def test_bank_else():
    assert bank.value("") == 100
    assert bank.value("a") == 100
    assert bank.value("b") == 100
    assert bank.value("c") == 100
    assert bank.value("d") == 100
    assert bank.value("e") == 100
    assert bank.value("f") == 100
    assert bank.value("g") == 100
    assert bank.value("i") == 100
    assert bank.value("j") == 100
    assert bank.value("k") == 100
    assert bank.value("l") == 100
    assert bank.value("m") == 100
    assert bank.value("n") == 100
    assert bank.value("o") == 100
    assert bank.value("p") == 100
    assert bank.value("q") == 100
    assert bank.value("r") == 100
    assert bank.value("s") == 100
    assert bank.value("t") == 100
    assert bank.value("u") == 100
    assert bank.value("v") == 100
    assert bank.value("w") == 100
    assert bank.value("x") == 100
    assert bank.value("y") == 100
    assert bank.value("z") == 100