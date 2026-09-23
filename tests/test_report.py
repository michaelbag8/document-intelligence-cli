from docintel.report import generate_report


def test_generate_report():
    result = {
        "emails": ["support@acme.com", "admin@acme.com"],
        "phone_numbers": ["+2348012345678"],
        "money": ["$1,250.00", "$500"],
    }

    report = generate_report(result)

    assert "Document Intelligence Report" in report
    assert "Emails:" in report
    assert "Phone Numbers:" in report
    assert "Money:" in report

    assert "support@acme.com" in report
    assert "admin@acme.com" in report
    assert "+2348012345678" in report
    assert "$1,250.00" in report
    assert "$500" in report

def test_generate_report_empty():
    result = {}

    report = generate_report(result)

    assert "Document Intelligence Report" in report
    assert "===========================" in report
    assert report.strip() == "Document Intelligence Report\n==========================="

def test_generate_report_single_entry():
    result = {
        "emails": ["    support@acme.com   "],
        "phone_numbers": ["   +2348012345678   "],
        "money": ["   $1,250.00   "],
    }

    report = generate_report(result)

    assert "Document Intelligence Report" in report
    assert "===========================" in report
    assert "Emails:" in report
    assert "Phone Numbers:" in report
    assert "Money:" in report

    assert "support@acme.com" in report
    assert "+2348012345678" in report
    assert "$1,250.00" in report


def test_generate_report_with_special_characters():
    result = {
        "emails": ["support@acme.com", "admin@acme.com"],
        "phone_numbers": ["+2348012345678"],
        "money": ["$1,250.00", "$500"],
    }

    report = generate_report(result)

    assert "Document Intelligence Report" in report
    assert "===========================" in report
    assert "Emails:" in report
    assert "Phone Numbers:" in report
    assert "Money:" in report

    assert "support@acme.com" in report
    assert "admin@acme.com" in report
    assert "+2348012345678" in report
    assert "$1,250.00" in report
    assert "$500" in report

def test_generate_report_with_empty_values():
    result = {
        "emails": [],
        "phone_numbers": [],
        "money": [],
    }

    report = generate_report(result)

    assert "Document Intelligence Report" in report
    assert "===========================" in report
    assert "Emails:" in report
    assert "Phone Numbers:" in report
    assert "Money:" in report

    assert "- None" not in report  # Ensure no empty values are displayed   

def test_generate_report_with_none_values():
    result = {
        "emails": None,
        "phone_numbers": None,
        "money": None,
    }

    report = generate_report(result)

    assert "Document Intelligence Report" in report
    assert "===========================" in report
    assert "Emails:" in report
    assert "Phone Numbers:" in report
    assert "Money:" in report

    assert "- None" not in report  # Ensure no empty values are displayed   


def test_generate_report_with_mixed_values():
    result = {
        "emails": ["   support@acme.com   ", None],
        "phone_numbers": ["   +2348012345678   ", None],
        "money": ["   $1,250.00   ", None],
    }

    report = generate_report(result)

    assert "Document Intelligence Report" in report
    assert "===========================" in report
    assert "Emails:" in report
    assert "Phone Numbers:" in report
    assert "Money:" in report

    assert "support@acme.com" in report
    assert "+2348012345678" in report
    assert "$1,250.00" in report

def test_generate_report_with_urls():
    result = {
        "urls": [
            "https://example.com",
            "https://example.com/docs",
        ]
    }

    report = generate_report(result)

    assert "URLs:" in report
    assert "https://example.com" in report
    assert "https://example.com/docs" in report


def test_generate_report_strips_value_whitespace():
    result = {
        "emails": ["   support@acme.com   "],
    }

    report = generate_report(result)

    assert "  - support@acme.com" in report
    assert "  -    support@acme.com" not in report


def test_generate_report_skips_none_values():
    result = {
        "emails": ["support@acme.com", None],
    }

    report = generate_report(result)

    assert "support@acme.com" in report
    assert "- None" not in report