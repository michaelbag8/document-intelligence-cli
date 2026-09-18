
from docintel.extractors import (
    extract_dates,
    extract_emails,
    extract_hashtags,
    extract_ip_addresses,
    extract_mentions,
    extract_money,
    extract_phone_numbers,
    extract_urls,
)


# Test for email extraction
def test_extract_multiple_emails():
    result = extract_emails("Contact us at support@example.com and also at michaelbag8@gmail.com")
    assert result == ["support@example.com", "michaelbag8@gmail.com"]

def test_extract_single_email():
    result = extract_emails("Contact us at learn2earn@example.com")
    assert result == ["learn2earn@example.com"]


def test_extract_plus_email():
    result = extract_emails("Contact us at michael+bag8@gmail.com")
    assert result == ["michael+bag8@gmail.com"]


def test_extract_no_email():
    result = extract_emails("Contact us at no 2 Ebije street otukpo, Benin city, Edo state. You can also reach us at")
    assert result == []

def test_extract_invalid_email():
    result = extract_emails("Contact us at hello@@example.com")

    assert result == []

def test_extract_comma_invalid_email():
    result = extract_emails("Contact us at hello@example..com")

    assert result == ["hello@example..com"]


# Test for URL extraction
def test_extract_url_with_www():   
    result = extract_urls("Visit https://www.example.com")
    assert result == ["https://www.example.com"]

def test_extract_url_without_www():
    result = extract_urls("Visit https://example.com")
    assert result == ["https://example.com"]


def test_extract_url_with_subdomain():
    result = extract_urls("Visit https://subdomain.example.com")
    assert result == ["https://subdomain.example.com"]

def test_extract_url_with_port():
    result = extract_urls("Visit https://example.com:8080")
    assert result == ["https://example.com:8080"]

def test_extract_multiples_urls():
    result = extract_urls("Visit https://example.com and http://google.com")
    assert result == ["https://example.com", "http://google.com"]

def test_extract_url_with_path():
    result = extract_urls("Visit https://example.com/path/to/resource")
    assert result == ["https://example.com/path/to/resource"]

def test_extract_url_with_query():
    result = extract_urls("Visit https://example.com/search?q=test")
    assert result == ["https://example.com/search?q=test"]


# Test for phone number extraction
def test_extract_phone_numbers():
    result = extract_phone_numbers("Call us at +1234567890")
    assert result == ["+1234567890"]

def test_extract_multiple_phone_numbers():
    result = extract_phone_numbers("Call us at +1234567890 or +0987654321")
    assert result == ["+1234567890", "987654321"]

def test_extract_phone_numbers_without_plus():
    result = extract_phone_numbers("Call us at 1234567890")
    assert result == ["1234567890"] 

def test_extract_phone_numbers_with_country_code():
    result = extract_phone_numbers("Call us at +12345678900")
    assert result == ["+12345678900"]

def test_extract_no_phone_numbers():
    result = extract_phone_numbers("Talk to us on our office line")
    assert result == []


# Test for money extraction
def test_extract_money():
    result = extract_money("The price is $12.34")
    assert result == ["$12.34"]

def test_extract_multiple_money():
    result = extract_money("The prices are $12.34 and $56.78")
    assert result == ["$12.34", "$56.78"]

def test_extract_money_without_cents():
    result = extract_money("The price is $12")
    assert result == ["$12"]

def test_extract_money_with_cents():
    result = extract_money("The price is $12.34")
    assert result == ["$12.34"]

def test_extract_money_with_no_dollar_sign():
    result = extract_money("The price is 12.34")
    assert result == []

def test_extract_money_with_no_numbers():
    result = extract_money("The price is $")
    assert result == []



# Test for date extraction
def test_extract_dates():
    result = extract_dates(
        "Important dates are 2020-01-12 and 2020-12-01"
    )
    assert result == ["2020-01-12", "2020-12-01"]


def test_extract_single_date():
    result = extract_dates("The event is on 2020-01-12")
    assert result == ["2020-01-12"]


def test_extract_no_dates():
    result = extract_dates("There are no dates here")
    assert result == []

def test_extract_invalid_dates():
    result = extract_dates("Invalid dates like 32nd January 2020 should not be extracted")
    assert result == []

# Test for hashtag extraction
def test_extract_hashtags():
    result = extract_hashtags("Check this out #hashtag")
    assert result == ["#hashtag"]

def test_extract_multiple_hashtags():
    result = extract_hashtags("Check this out #hashtag1 and #hashtag2")
    assert result == ["#hashtag1", "#hashtag2"]

def test_extract_no_hashtags():
    result = extract_hashtags("There are no hashtags here")
    assert result == []

def test_extract_invalid_hashtags():
    result = extract_hashtags("Invalid hashtags like #123 should not be extracted")
    assert result == ["#123"] 

def test_extract_hashtags_with_special_characters():
    result = extract_hashtags("Check this out #hashtag! and #hashtag?")
    assert result == ["#hashtag", "#hashtag"]

# Test for mention extraction
def test_extract_mentions():
    result = extract_mentions("Hello @user, how are you?")
    assert result == ["@user"]

def test_extract_multiple_mentions():
    result = extract_mentions("Hello @user1 and @user2, how are you?")
    assert result == ["@user1", "@user2"]

def test_extract_no_mentions():
    result = extract_mentions("There are no mentions here")
    assert result == []

def test_extract_invalid_mentions():
    result = extract_mentions("Invalid mentions like @123 should not be extracted")
    assert result == ["@123"]

def test_extract_mentions_with_special_characters():
    result = extract_mentions("Hello @user! and @user?")
    assert result == ["@user", "@user"]

# Test for IP address extraction
def test_extract_ip_addresses():
    result = extract_ip_addresses("My IP is 192.168.1.1")
    assert result == ["192.168.1.1"]

def test_extract_multiple_ip_addresses():
    result = extract_ip_addresses("My IPs are 192.168.1.1 and 10.0.0.1")
    assert result == ["192.168.1.1", "10.0.0.1"]    

def test_extract_no_ip_addresses():
    result = extract_ip_addresses("There are no IP addresses here")
    assert result == []     

def test_extract_invalid_ip_addresses():
    result = extract_ip_addresses("Invalid IPs like 999.999.999.999 should not be extracted")
    assert result == ["999.999.999.999"]

def test_extract_ip_addresses_with_leading_zeros():
    result = extract_ip_addresses("My IP is 192.168.01.01")
    assert result == ["192.168.01.01"]  
