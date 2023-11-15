from working import convert
import pytest

def test_hours_off_by_one():
    result = convert("9 AM to 5 PM")
    assert result == "09:00 to 17:00", "Hours should not be off by one."

def test_minutes_off_by_five():
    result = convert("9:05 AM to 5:15 PM")
    assert result == "09:05 to 17:15", "Minutes should not be off by five."

def test_Valueerror_ommiting_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
        
def test_Valueerror_outofrange():
    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")