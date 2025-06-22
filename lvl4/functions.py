# to init a function you need to do:
def function_name(parameter1, parameter2):
    # function body
    return parameter1 + parameter2
# function can return a value or not
# if it does not return a value, it will return None by default

def add_numbers(a: float, b: float) -> float:
    return a + b

def calc_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    
    sum: float = 0.0
    for number in numbers:
        sum += number
    return sum / len(numbers)

def get_list_of_numbers() -> list[float]:
    numbers: list[float] = []
    while True:
        user_input: str = input("Enter a number (or 'done' to finish): ")
        if user_input == 'done':
            break
        
        number: float = float(user_input)
        numbers.append(number)
    return numbers


def main():
    print("Welcome to average calculator!")
    print("the average is " + str(calc_average(get_list_of_numbers())))
    
    
    
if __name__ == "__main__":
    main()