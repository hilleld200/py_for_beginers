EXIT_CODE = 'exit'
ADD_OPERAND = '+'
SUB_OPERAND = '-'
MUL_OPERAND = '*'
DEV_OPERAND = '/'

def add(first_number: float, second_number: float) -> float:
    return first_number + second_number
def subtract(first_number: float, second_number: float) -> float:
    return first_number - second_number
def multiply(first_number: float, second_number: float) -> float:
    return first_number * second_number
def divide(first_number: float, second_number: float) -> float:
    if second_number == 0:
        print("ERROR: Division by zero is not allowed.")
        return None
    return first_number / second_number

FUNCTIONS_DICT = {
    ADD_OPERAND: add,
    SUB_OPERAND: subtract,
    MUL_OPERAND: multiply,
    DEV_OPERAND: divide
}

def parse_expression(user_input: str) -> tuple[float, str, float]:
    """Parse a mathematical expression from user input.

    Args:
        user_input (str): The input string containing the mathematical expression.

    Returns:
        tuple[float, str, float]: A tuple containing the first number, operator, and second number.
    """
    index: int = 0
    while index < len(user_input) and user_input[index] != ' ':
        index += 1
    first_number: float = float(user_input[:index])

    operator_index = index + 1
    operator = user_input[operator_index]

    second_number: float = float(user_input[operator_index + 2:])  # Skip the space after the operator

    return first_number, operator, second_number

def calculator_loop():
    """
    Main loop for the calculator that continuously accepts user input
    and performs calculations until the user decides to exit.
    """
    while True:
        user_input: str = input("Enter mathematical expression (or 'exit' to quit): ")
        if user_input.lower() == EXIT_CODE:
            return
        
        row_expression = parse_expression(user_input)
        first_number, operator, second_number = row_expression
        
        if operator not in FUNCTIONS_DICT:
            print(f"ERROR: The operator '{operator}' is not supported.")
            continue
        result = FUNCTIONS_DICT[operator](first_number, second_number)
        if result is not None:
            print(f"The result of {first_number} {operator} {second_number} is: {result}\n")

def main():
    """Main function to run the calculator."""
    print("Welcome to the calculator!")
    
    calculator_loop()
    
    print("Thank you for using the calculator. Goodbye!")    


if __name__ == "__main__":
    main()