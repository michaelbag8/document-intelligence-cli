
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

def test_extract_urls():
    result = extract_urls("Visit us at https://www.example.com")
    assert result == ["https://www.example.com"]

def test_extract_phone_numbers():
    result = extract_phone_numbers("Call us at +1234567890")
    assert result == ["+1234567890"]

def test_extract_money():
    result = extract_money("The price is $12.34")
    assert result == ["$12.34"]

def test_extract_dates():
    result = extract_dates("Important dates are 12/01/2020 and 01/12/2020")
    assert result == ["12/01/2020", "01/12/2020"]

def test_extract_hashtags():
    result = extract_hashtags("Check this out #hashtag")
    assert result == ["#hashtag"]

def test_extract_mentions():
    result = extract_mentions("Hello @user, how are you?")
    assert result == ["@user"]

def test_extract_ip_addresses():
    result = extract_ip_addresses("My IP is 192.168.1.1")
    assert result == ["192.168.1.1"]
