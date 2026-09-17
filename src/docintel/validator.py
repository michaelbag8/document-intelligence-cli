import re


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


