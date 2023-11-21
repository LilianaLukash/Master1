def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    result_list = {
    "UA": [],
    "JP": [],
    "TW": [],
    "SG": []
}
    for phone in list_phones:
        if sanitize_phone_number(phone).startswith("81"):
            result_list["JP"].append(sanitize_phone_number(phone))
        elif sanitize_phone_number(phone).startswith("65"):
            result_list["SG"].append(sanitize_phone_number(phone))
        elif sanitize_phone_number(phone).startswith("886"):
            result_list["TW"].append(sanitize_phone_number(phone))
        else:
            result_list["UA"].append(sanitize_phone_number(phone))
    return result_list
        
print(get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976']))