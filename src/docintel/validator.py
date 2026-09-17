import re

def is_valid_email(email):
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if ".." in email:
        return False  

    return re.match(pattern, email) is not None

def is_valid_phone_number(phone):
    pattern = r"\+?[1-9]\d{1,14}"

    return re.match(pattern, phone) is not None


# def is_valid_money():
#     pass
# def is_valid_date():
#     pass
# def is_valid_ip_address():
#     pass