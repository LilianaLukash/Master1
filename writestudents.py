def save_applicant_data(source, output):
    with open(output, "w") as fh:
        res = []
        for abi in source:
            line = ""
            line_list = abi.values()
            for l in line_list:
                if line == "":
                    line = str(l)
                else:
                    line = line + "," + str(l)
            line = line + "\n"
            res.append(line)
        fh.writelines(res)

a = [{
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    }]
save_applicant_data(a,"students.txt")