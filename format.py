def formatted_numbers():
    lo = ["| decimal  |   hex    |  binary  |"]
    for i in range(16):
        lo.append('|{:<10d}|{:^10x}|{:>10b}|'.format(i,i,i))
    return lo
mo = formatted_numbers()
for l in mo:
    print(l)