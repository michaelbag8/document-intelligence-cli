from docintel.validators import (
    is_valid_date,
    is_valid_email,
    is_valid_ip_address,
    is_valid_money,
    is_valid_phone_number,
    is_valid_url,
    is_valid_hashtag,
    is_valid_mention,
)



# Test for email validation
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

def test_valid_email_with_dot():
    assert is_valid_email("first.last@example.com") is True


def test_valid_email_with_hyphen():
    assert is_valid_email("user-name@example.com") is True


def test_invalid_email_without_local_part():
    assert is_valid_email("@example.com") is False


def test_invalid_email_without_tld():
    assert is_valid_email("user@example") is False


def test_invalid_email_with_space():
    assert is_valid_email("user name@example.com") is False


def test_invalid_email_with_space_in_domain():
    assert is_valid_email("user@exam ple.com") is False


def test_invalid_email_with_multiple_at_symbols():
    assert is_valid_email("user@@example.com") is False


def test_invalid_email_with_trailing_dot_in_domain():
    assert is_valid_email("user@example.com.") is False

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

def test_invalid_phone_number_with_leading_zero():
    assert is_valid_phone_number("0123456789") is False


def test_invalid_phone_number_with_plus_and_leading_zero():
    assert is_valid_phone_number("+0123456789") is False


def test_invalid_phone_number_too_short():
    assert is_valid_phone_number("123456") is False


def test_invalid_phone_number_too_long():
    assert is_valid_phone_number("1234567890123456") is False


def test_valid_phone_number_with_exactly_7_digits():
    assert is_valid_phone_number("1234567") is True


def test_valid_phone_number_with_exactly_15_digits():
    assert is_valid_phone_number("123456789012345") is True

#Test for money validation      
def test_valid_money_without_cents():
    assert is_valid_money("$12") is True


def test_valid_money_with_cents():
    assert is_valid_money("$12.34") is True


def test_valid_money_with_comma():
    assert is_valid_money("$1,000") is True


def test_valid_money_with_comma_and_cents():
    assert is_valid_money("$2,500.50") is True


def test_invalid_money_without_currency_symbol():
    assert is_valid_money("12.34") is False


def test_invalid_money_without_amount():
    assert is_valid_money("$") is False


def test_invalid_money_with_letters():
    assert is_valid_money("$12abc") is False


def test_invalid_money_with_three_decimal_places():
    assert is_valid_money("$12.345") is False


#Test for date validation
def test_valid_date():
    assert is_valid_date("2023-01-01") is True  

def test_invalid_date():
    assert is_valid_date("2023-13-01") is False 

def test_invalid_date_format():
    assert is_valid_date("01-01-2023") is False

def test_invalid_date_with_letters():
    assert is_valid_date("2023-01-AB") is False

def test_invalid_date_with_extra_characters():
    assert is_valid_date("2023-01-01T00:00:00") is False

def test_invalid_date_february_30():
    assert is_valid_date("2023-02-30") is False


def test_invalid_date_february_29_non_leap_year():
    assert is_valid_date("2023-02-29") is False


def test_valid_date_february_29_leap_year():
    assert is_valid_date("2024-02-29") is True


#Test for IP address validation
def test_valid_ip_address():
    assert is_valid_ip_address("192.168.1.1") is True

def test_invalid_ip_address():
    assert is_valid_ip_address("256.256.256.256") is False  

def test_invalid_ip_address_with_letters():
    assert is_valid_ip_address("192.168.1.A") is False

def test_invalid_ip_address_with_extra_octets():
    assert is_valid_ip_address("192.168.1.1.1") is False

def test_invalid_ip_address_with_missing_octets():
    assert is_valid_ip_address("192.168.1") is False

def test_valid_ip_address_with_leading_zeros():
    assert is_valid_ip_address("192.168.01.01") is True


def test_invalid_ip_address_with_empty_octet():
    assert is_valid_ip_address("192..1.1") is False


def test_invalid_ip_address_with_five_digit_octet():
    assert is_valid_ip_address("192.168.0001.1") is False


def test_invalid_ip_address_with_negative_octet():
    assert is_valid_ip_address("192.168.-1.1") is False


def test_invalid_ip_address_with_spaces():
    assert is_valid_ip_address("192.168.1. 1") is False


#Test for url validation
def test_valid_url_without_www():
    assert is_valid_url("https://example.com") is True

def test_valid_url_without_https():
    assert is_valid_url("http://www.example.com") is True

def test_invalid_url_without_protocol():
    assert is_valid_url("www.example.com") is False

def test_invalid_url_with_invalid_characters(): 
    assert is_valid_url("https://www.exa mple.com") is False

def test_valid_url_with_path():
    assert is_valid_url("https://example.com/path/to/resource")


def test_valid_url_with_query():
    assert is_valid_url("https://example.com/search?q=test")


def test_valid_url_with_port():
    assert is_valid_url("https://example.com:8080")


def test_valid_url_with_deep_path():
    assert is_valid_url("https://example.com/path/to/resource")

def test_valid_hashtag_with_numbers():
    assert is_valid_hashtag("#python2026") is True


def test_valid_hashtag_with_underscore():
    assert is_valid_hashtag("#python_ai") is True


def test_invalid_hashtag_without_hash():
    assert is_valid_hashtag("python") is False


def test_invalid_hashtag_with_space():
    assert is_valid_hashtag("#python ai") is False


def test_invalid_hashtag_with_hyphen():
    assert is_valid_hashtag("#python-ai") is False


def test_invalid_empty_hashtag():
    assert is_valid_hashtag("#") is False

def test_valid_mention_with_numbers():
    assert is_valid_mention("@user2026") is True


def test_valid_mention_with_underscore():
    assert is_valid_mention("@python_dev") is True


def test_invalid_mention_without_at():
    assert is_valid_mention("user") is False


def test_invalid_mention_with_space():
    assert is_valid_mention("@python dev") is False


def test_invalid_mention_with_hyphen():
    assert is_valid_mention("@python-dev") is False


def test_invalid_empty_mention():
    assert is_valid_mention("@") is False