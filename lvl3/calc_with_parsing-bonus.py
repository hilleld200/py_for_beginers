EXIT_CODE = 'exit'
ADD_OPERAND = '+'
SUB_OPERAND = '-'
MUL_OPERAND = '*'
DEV_OPERAND = '/'

user_input: str = input("Enter mathematical expression (or 'exit' to quit): ")
while user_input != EXIT_CODE:    
    # get the first number
    index: int = 0
    while index < len(user_input) and user_input[index] != ' ':
        index += 1
    first_number:float = float(user_input[:index])
    
    # get the operator
    operator_index = index + 1
    operator = user_input[operator_index]
    
    # get the second number
    second_number: float = float(user_input[operator_index + 2:])  # Skip the space after the operator
    
    # perform the calculation based on the operator
    result: float = 0.0
    if operator == ADD_OPERAND:
        result = first_number + second_number
    elif operator == SUB_OPERAND:
        result = first_number - second_number
    elif operator == MUL_OPERAND:
        result = first_number * second_number
    elif operator == DEV_OPERAND:
        result = first_number / second_number
    
    print(f"The result of {first_number} {operator} {second_number} is: {result}\n")
    
    # get the next expression
    user_input = input("Enter mathematical expression (or 'exit' to quit): ")
    