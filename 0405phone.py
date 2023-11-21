def sanitize_phone_number(phone):
    phone1 =  phone.strip()
    todelete = [" ","(", "-",")" , "+"]
    result = ""
    for symbol in phone1:
        if symbol not in todelete:
            result = result + symbol
    return result
                

print(sanitize_phone_number("    +38(050)123-32-34"))

