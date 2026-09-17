from docintel.validator import is_valid_email


# Test for email validation
def test_is_valid_email():
    assert is_valid_email("support@example.com")
    assert is_valid_email("michael+bag8@gmail.com")
    assert not is_valid_email("hello@@example.com")
    assert not is_valid_email("@example.com")
    assert not is_valid_email("hello")

def test_valid_email_with_plus():
    assert is_valid_email("michael+bag8@gmail.com") is True

def test_valid_email_with_subdomain():
    assert is_valid_email("user@mail.example.com") is True  

def test_valid_email_with_numbers():
    assert is_valid_email("user123@example.com") is True    

def test_invalid_email():
    assert is_valid_email("hello@@example.com") is False

def test_invalid_email_without_domain():
    assert is_valid_email("hello@") is False

