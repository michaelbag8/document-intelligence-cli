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
from docintel.validators import (
    is_valid_date,
    is_valid_email,
    is_valid_hashtag,
    is_valid_ip_address,
    is_valid_mention,
    is_valid_money,
    is_valid_phone_number,
    is_valid_url,
)


def process_document(text: str) -> dict[str, list[str]]:
    extraction_rules = {
        "emails": (extract_emails, is_valid_email),
        "phone_numbers": (extract_phone_numbers, is_valid_phone_number),
        "money": (extract_money, is_valid_money),
        "dates": (extract_dates, is_valid_date),
        "hashtags": (extract_hashtags, is_valid_hashtag),
        "mentions": (extract_mentions, is_valid_mention),
        "ip_addresses": (extract_ip_addresses, is_valid_ip_address),
        "url": (extract_urls, is_valid_url)
    }

    result = {}

    for key, (extractor, validator) in extraction_rules.items():
        extracted = extractor(text)
        valid = [item for item in extracted if validator(item)]
        result[key] = valid

    return result