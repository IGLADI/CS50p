from numb3rs import validate


def test_ip_validation():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("128.128.128.128") == True


def test_ip_validation_fail():
    assert validate("256.256.256.256") == False
    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False


def test_ip_length():
    assert validate("0.0.0") == False
    assert validate("0.0.0.0.0") == False
