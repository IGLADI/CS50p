import plates


def test_plates():
    assert plates.is_valid("aaa111") == True
    assert plates.is_valid("zz24") == True


def test_plates_begins_alpha():
    assert plates.is_valid("1aa") == False
    assert plates.is_valid("1111") == False


def test_plates_length():
    assert plates.is_valid("a") == False
    assert plates.is_valid("aa") == True
    assert plates.is_valid("aaaaaa") == True
    assert plates.is_valid("aaaaaaa") == False


def test_plates_no_punctuation():
    assert plates.is_valid("aaa!") == False
    assert plates.is_valid("aaa.") == False
    assert plates.is_valid("aaa,") == False
    assert plates.is_valid("aaa?") == False
    assert plates.is_valid("aa aa") == False


def test_plates_numbers_placement():
    assert plates.is_valid("11aa") == False
    assert plates.is_valid("a1a") == False
    assert plates.is_valid("aa0") == False
    assert plates.is_valid("aa01") == False
    assert plates.is_valid("AAA22A") == False
