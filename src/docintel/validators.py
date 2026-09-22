import re
from datetime import datetime
from urllib.parse import urlparse


def is_valid_email(email: str) -> bool:
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if ".." in email:
        return False  

    return re.match(pattern, email) is not None


def is_valid_phone_number(phone: int) -> bool:
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
     

def is_valid_money(money: str) -> bool:
    formats = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"

    return re.fullmatch(formats, money) is not None


def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)

    if parsed.scheme not in {"http", "https"}:
        return False

    if not parsed.netloc:
        return False

    if any(char.isspace() for char in url):
        return False

    try:
        hostname = parsed.hostname
    except ValueError:
        return False

    if not hostname:
        return False

    return "." in hostname

def is_valid_date(date: str) -> bool:
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(pattern, date) is None:
        return False
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_hashtag(hashtag: str) -> bool:
    pattern = r'^#[a-zA-Z0-9_]+$'
    return re.match(pattern, hashtag) is not None

def is_valid_mention(mention: str) -> bool:
    pattern = r'^@[a-zA-Z0-9_]+$'
    return re.match(pattern, mention) is not None

def is_valid_ip_address(ip: str) -> bool:
    pattern = r'^(?:\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False

    parts = ip.split('.')
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False

    return True 


