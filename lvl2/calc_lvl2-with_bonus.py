EXIT_OPERAND = 'X'
ADD_OPERAND = '+'
SUB_OPERAND = '-'
MUL_OPERAND = '*'
DEV_OPERAND = '/'

COLORS = {
        "BLACK": '\033[30m',
        "RED": '\033[31m',
        "GREEN": '\033[32m',
        "YELLOW" : '\033[33m',
        "BLUE" : '\033[34m',
        "MAGENTA" : '\033[35m',
        "CYAN" : '\033[36m',
        "WHITE" : '\033[37m',
        "RESET" : '\033[0m' # Resets all formatting (color, style, etc.)
}


while user_operand != EXIT_OPERAND:
    # get user operand
    user_operand: str = input(f"{COLORS['CYAN']}Enter operand:{COLORS['RESET']} ")
    # get 2 number for the user
    num1: float = float(input(f"{COLORS['YELLOW']}Enter first number:{COLORS['RESET']} "))
    num2: float = float(input(f"{COLORS['YELLOW']}Enter second number:{COLORS['RESET']} "))
    
    # calc the output by the operand
    output: float = 0
    
    if user_operand == ADD_OPERAND:
        output = num1 + num2
    elif user_operand == SUB_OPERAND:
        output = num1 - num2 
    elif user_operand == MUL_OPERAND:
        output = num1 * num2 
    elif user_operand == DEV_OPERAND:
        if num2 == 0:
            # check if the second number is zero to avoid division by zero error
            print(f"{COLORS['RED']}ERROR: Division by zero is not allowed.{COLORS['RESET']}")
            continue
        output = num1 / num2
    elif user_operand == EXIT_OPERAND:
        break
    else:
        print(f"{COLORS['RED']}ERROR: The operator '{user_operand}' is not supported{COLORS['RESET']}")
        continue
    # print the output to user
    
    print(f"The answer to the problem: {COLORS['MAGENTA']} {num1} {user_operand} {num2} {COLORS['RESET']}\n\t\
        Is: {COLORS['GREEN']} {output} {COLORS['RESET']}\n")
    
    
 
