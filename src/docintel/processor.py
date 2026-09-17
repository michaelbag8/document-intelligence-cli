from docintel.validator import (
    extract_emails,
    extract_money,
    extract_phone_numbers,
    is_valid_email,
    is_valid_money,
    is_valid_phone_number,
)


def process_document(text):
    extractors = {
        "emails": (extract_emails, is_valid_email),
        "phone_numbers": (extract_phone_numbers, is_valid_phone_number),
        "money": (extract_money, is_valid_money),
    }

    result = {}
    for key, (extractor, validator) in extractors.items():
        extracted = extractor(text)
        valid = [item for item in extracted if validator(item)]
        result[key] = valid

    return result

