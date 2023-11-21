result = None
operand = None
operator = None
wait_for_number = True
while True:
    if wait_for_number:
        try:
            operand = float(input("Enter a number ="))
        except ValueError:
            print("Incorrect input. Please enter a valid number.")
            
    operator = input("Enter an operator ( +, -, *, / ): ")

    if operator not in ['+', '-', '*', '/']:
            print("Incorrect operator. Please enter a valid operator.")
            wait_for_number = False
    else:
        if result == None:
            result = 0
            
        if operator == '+':
            result = result + operand
        elif operator == '-':
            result = result - operand
        elif operator == '*':
            result = result * operand
        elif operator == '/':
            if operand == 0:
                print("Please enter a non-zero operand.")
                
            else:
                result = result / operand
        elif operator == '=':
            print("result =", result)
            break
        else:
            print("Incorrect operator. Please enter a valid operator.")
            
        print("result = ", result)
        wait_for_number = True