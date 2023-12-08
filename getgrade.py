def get_grade(key):
    d1 = { "F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, 'В': 5, "A":  5}
    return d1[key]


def get_description(key):
    d2 = { "F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D": "Satisfactorily", "C": "Good", "В": "Very good", "A":  "Perfectly"}
    a = d2[key]
    return a

a="AA"
print(get_grade(a))
print(get_description(a))