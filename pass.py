def is_valid_password(password):
    check = [0,0,0,0]
    if len(str(password))==8:
        check[0] = 1
    for s in str(password):
        if s.islower():
            check[1] = 1
        if s.isupper():
            check[2] = 1
        if s.isdigit():
            check[3] = 1
    if check == [1,1,1,1]:
        return True
    else:
        return False
    
print(is_valid_password("As273877"))
print(is_valid_password(" "))