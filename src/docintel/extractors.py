import re


def extract_emails(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(email_pattern, text)


def extract_urls(text):
    url_pattern = r"https?://[^\s]+"
    return re.findall(url_pattern, text)


def extract_phone_numbers(text):
    phone_pattern = r"\+?[1-9]\d{1,14}"
    return re.findall(phone_pattern, text)


def extract_money(text):
    money_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?(?!\d|,\d|\.\d)"
    return re.findall(money_pattern, text)


def extract_dates(text):
    date_pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    return re.findall(date_pattern, text)


def extract_hashtags(text):
    hashtag_pattern = r"#\w+"
    return re.findall(hashtag_pattern, text)


def extract_mentions(text):
    mention_pattern = r"(?<![\w@])@\w+"
    return re.findall(mention_pattern, text)

def extract_ip_addresses(text):
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    return re.findall(ip_pattern, text)
