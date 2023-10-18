import twttr

def test_shorten():
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("hello") == "hll"
    
def test_shorten_empty():
    assert twttr.shorten("") == ""
    
def test_shorten_no_vowels():
    assert twttr.shorten("aeiou") == ""
    assert twttr.shorten("AEIOU") == ""
    
def test_numbers():
    assert twttr.shorten("1234567890") == "1234567890"
    
def test_punctuation():
    assert twttr.shorten(".,?!") == ".,?!"