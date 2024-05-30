from src.email_validator import is_valid_email


def test_email_has_symbol():
    assert is_valid_email('abc@gmail.com') == True
    assert is_valid_email('abcgmail.com') == False


def test_email_has_valid_domain():
    assert is_valid_email('abc@gmail.com') == True
    assert is_valid_email('abc@.com') == False
    assert is_valid_email('abc@com') == False
    assert is_valid_email('abc@') == False
    assert is_valid_email('@') == False
