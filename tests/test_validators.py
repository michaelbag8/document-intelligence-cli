from docintel.validator import (
    is_valid_email,
    is_valid_phone_number
    #is_valid_money,
    #is_valid_date,
    #is_valid_ip_address,    
    
)

#Test for email validtion
def test_valid_email():
    assert is_valid_email("support@example.com") is True


def test_valid_email_with_plus():
    assert is_valid_email("michael+bag8@gmail.com") is True


def test_invalid_email():
    assert is_valid_email("hello@@example.com") is False


def test_invalid_email_without_domain():
    assert is_valid_email("hello@") is False


def test_invalid_email_without_at_symbol():
    assert is_valid_email("hello.example.com") is False


def test_invalid_email_with_double_dot():
    assert is_valid_email("hello@example..com") is False


# Test for phone number validation
def test_valid_phone_number():
    assert is_valid_phone_number("+1234567890") is True


def test_valid_phone_number_without_plus():
    assert is_valid_phone_number("1234567890") is True


def test_invalid_phone_number():
    assert is_valid_phone_number("123") is False


def test_invalid_phone_number_with_letters():
    assert is_valid_phone_number("+12345abc890") is False


def test_invalid_phone_number_with_spaces():
    assert is_valid_phone_number("+1 234 567 890") is False