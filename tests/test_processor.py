from docintel.processor import process_document


def test_process_document():
    text = """
    Contact us at support@example.com or call +1234567890.
    The total cost is $12.34.
    """

    result = process_document(text)

    assert result == {
        "emails": ["support@example.com"],
        "phone_numbers": ["+1234567890"],
        "money": ["$12.34"],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_invalid_values():
    text = """
    Contact us at support@example.com or bad@@example.com.
    Call +1234567890 or +12345abc890.
    The total cost is $12.34 or $12.345.
    """

    result = process_document(text)

    assert result == {
        "emails": ["support@example.com"],
        "phone_numbers": ["+1234567890"],
        "money": ["$12.34"],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_no_values():
    text = "This document contains no emails, phone numbers, or money."

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_multiple_values():
    text = """
    Contact support@example.com or admin@example.com.
    Call +1234567890 or +9876543210.
    The costs are $12.34 and $2,500.50.
    """

    result = process_document(text)

    assert result == {
        "emails": [
            "support@example.com",
            "admin@example.com",
        ],
        "phone_numbers": [
            "+1234567890",
            "+9876543210",
        ],
        "money": [
            "$12.34",
            "$2,500.50",
        ],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_invalid_email():
    text = """
    Contact us at support@@example.com.
    Call +1234567890.
    """

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": ["+1234567890"],
        "money": [],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_invalid_phone_number():
    text = """
    Contact us at support@example.com.
    Call +12345abc890.
    """

    result = process_document(text)

    assert result == {
        "emails": ["support@example.com"],
        "phone_numbers": [],
        "money": [],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_invalid_money():
    text = """
    The total cost is $12.345.
    """

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_dates():
    text = """
    The project started on 2026-09-17.
    The deadline is 2026-12-31.
    """

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
        "dates": [
            "2026-09-17",
            "2026-12-31",
        ],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_invalid_dates():
    text = """
    Valid date: 2026-09-17.
    Invalid dates: 2026-13-01, 2026-02-30, 2025-02-29.
    """

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
        "dates": ["2026-09-17"],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_hashtags():
    text = """
    #Python #ArtificialIntelligence #DocumentIntelligence #Nigeria
    """

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
        "dates": [],
        "hashtags": [
            "#Python",
            "#ArtificialIntelligence",
            "#DocumentIntelligence",
            "#Nigeria",
        ],
        "mentions": [],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_mentions():
    text = """
    Contact @michael or @admin.
    You can also reach @python_dev.
    """

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
        "dates": [],
        "hashtags": [],
        "mentions": [
            "@michael",
            "@admin",
            "@python_dev",
        ],
        "ip_addresses": [],
        "urls": [],
    }


def test_process_document_with_ip_addresses():
    text = """
    Server: 192.168.1.100.
    Gateway: 10.0.0.1.
    DNS: 8.8.8.8.
    """

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [
            "192.168.1.100",
            "10.0.0.1",
            "8.8.8.8",
        ],
        "urls": [],
    }


def test_process_document_with_invalid_ip_addresses():
    text = """
    Valid IP: 192.168.1.100.
    Invalid IPs: 999.999.999.999 and 192.168.1.300.
    """

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [
            "192.168.1.100",
        ],
        "urls": [],
    }


def test_process_document_with_all_values():
    text = """
    Contact support@example.com.
    Call +1234567890.
    The cost is $1,250.50.
    The project date is 2026-09-17.
    Follow #Python and #AI.
    Contact @michael and @admin.
    Server IP is 192.168.1.100.
    """

    result = process_document(text)

    assert result == {
        "emails": ["support@example.com"],
        "phone_numbers": ["+1234567890"],
        "money": ["$1,250.50"],
        "dates": ["2026-09-17"],
        "hashtags": ["#Python", "#AI"],
        "mentions": ["@michael", "@admin"],
        "ip_addresses": ["192.168.1.100"],
        "urls": [],
    }

def test_process_document_with_urls():
    text = """
    Our urls is https://example.com
    """

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
        "dates": [],
        "hashtags": [],
        "mentions": [],
        "ip_addresses": [],
        "urls": ["https://example.com"],
    }