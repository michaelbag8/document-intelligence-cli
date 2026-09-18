import re
from datetime import datetime 


def is_valid_email(email):
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if ".." in email:
        return False  

    return re.match(pattern, email) is not None


def is_valid_phone_number(phone):
    if not phone:
        return False

    if phone.startswith("+"):
        digits = phone[1:]
    else:
        digits = phone

    if not digits.isdigit():
        return False

    if len(digits) < 7:
        return False

    if len(digits) > 15:
        return False

    return digits.startswith("0") is False
     

def is_valid_money(money):
    formats = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"

    return re.fullmatch(formats, money) is not None

def is_valid_url(url):
    pattern = r'^https?://(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/[\w-]*)*/?$'
    return re.match(pattern, url) is not None

def is_valid_date(date):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(pattern, date) is None:
        return False
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_hashtag(hashtag):
    pattern = r'^#[a-zA-Z0-9_]+$'
    return re.match(pattern, hashtag) is not None

def is_valid_mention(mention):
    pattern = r'^@[a-zA-Z0-9_]+$'
    return re.match(pattern, mention) is not None

def is_valid_ip_address(ip):
    pattern = r'^(?:\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False

    parts = ip.split('.')
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False

    return True 


