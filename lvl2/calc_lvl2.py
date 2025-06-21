EXIT_OPERAND = 'X'
ADD_OPERAND = '+'
SUB_OPERAND = '-'
MUL_OPERAND = '*'
DEV_OPERAND = '/'

while user_operand != EXIT_OPERAND:
    # get user operand
    user_operand: str = input("Enter operand: ")
    # get 2 number for the user
    num1: float = float(input("Enter first number: "))
    num2: float = float(input("Enter second number: "))
    
    # calc the output by the operand
    output: float = 0
    
    if user_operand == ADD_OPERAND:
        output = num1 + num2
    elif user_operand == SUB_OPERAND:
        output = num1 - num2 
    elif user_operand == MUL_OPERAND:
        output = num1 * num2 
    elif user_operand == DEV_OPERAND:
        # check if the second number is zero to avoid division by zero error
        if num2 == 0:
            print("ERROR: Division by zero is not allowed.")
            continue
        output = num1 / num2
    elif user_operand == EXIT_OPERAND:
        break
    else:
        print(f"ERROR: The operator '{user_operand}' is not supported")
        continue
    # print the output to user
    
    print(f"The answer to the problem: {num1} {user_operand} {num2}\n\t\
        Is: {output}\n")
    
    
 
