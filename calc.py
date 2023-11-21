result = None
operand = None
operator = None
wait_for_number = True
aval = ["+", "-", "*", "/"]

while True:
    if wait_for_number:
        o = input("input number")
        try:
            operand = float(o)
            if operator:
                if operator == "+":
                    result = result + operand 
                elif operator == "-":
                    result = result - operand 
                elif operator == "*":
                        result = result * operand 
                elif operator == "/":
                        result = result / operand
                print(result)
            else:
                result = operand 
            wait_for_number = False  
        except: 
            print(f'{o} is not a number. Try again.')
                
        
    else:
        operator = input("operator")
        if operator == "=":
            print(result)
            break
        elif operator in aval:
            wait_for_number = True
            continue
        else:
            print(f'{operator} is not an operation. Try again.')