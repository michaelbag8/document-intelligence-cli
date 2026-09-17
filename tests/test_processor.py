from docintel.processor import process_document


def test_process_document():
    text = """
    Contact us at support@example.com or call +1234567890.
    The total cost is $12.34
    """

    result = process_document(text)

    assert result == {
        "emails": ["support@example.com"],
        "phone_numbers": ["+1234567890"],
        "money": ["$12.34"],
    }


def test_process_document_with_invalid_values():
    text = """
    Contact us at support@example.com or bad@@example.com.
    Call +1234567890 or 123.
    The total cost is $12.34 or $12.345.
    """

    result = process_document(text)

    assert result == {
        "emails": ["support@example.com"],
        "phone_numbers": ["+1234567890"],
        "money": ["$12.34"],
    }


def test_process_document_with_no_values():
    text = "This document contains no emails, phone numbers, or money."

    result = process_document(text)

    assert result == {
        "emails": [],
        "phone_numbers": [],
        "money": [],
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
    }
