import re
def total_salary(path):
    summ = 0
    fh = open(path, 'r')
    lines = fh.readlines()
    for l in lines:
        numbers = re.findall(r'\d+', l)
        summ +=float(numbers[0])
    fh.close()
    return summ   