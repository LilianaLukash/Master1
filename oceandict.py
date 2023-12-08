articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):

    result = []
    for dict in articles_dict:
        a = (dict["title"].lower()).find(key.lower())
        print(a)
        # b = dict["author"].find(key)
        # print(b)
        if letter_case == True:
            if dict["title"].find(key) > -1 or dict["author"].find(key) > -1:
                result.append(dict)
        else:
            if (dict["title"].lower()).find(key.lower()) > -1 or (dict["author"].lower()).find(key.lower()) > -1:
                result.append(dict)
    return result

print(find_articles("Ocean"))