from um import count

def test_single_um():
    assert count("hello, um, world") == 1

def test_no_um():
    assert count("yummy") == 0

def test_multiple_um():
    assert count("um, um, um, um") == 4

def test_mixed_case_um():
    assert count("Um, uM, uM, UM") == 4

if __name__ == "__main__":
    test_single_um()
    test_no_um()
    test_multiple_um()
    test_mixed_case_um()
