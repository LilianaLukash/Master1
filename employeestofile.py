


def write_employees_to_file(employee_list, path):
    
    res = " "
    for employee in employee_list:
        for on in employee:
            res = res + "\n" + on

    fh = open(path, 'w')
    fh.write(res[2:])
    fh.close()

worker_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
write_employees_to_file(worker_list, "mim.txt")
f = open("mim.txt", 'r')
k = f.read()
print(k)
f.close()