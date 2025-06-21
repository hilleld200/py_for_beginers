# get the numbers for division
num1:float = float(input("Enter first number: "))
num2:float = float(input("Enter second number: "))

# check if the second number is zero to avoid division by zero error --bonus--
if num2 == 0:
    print("ERROR: Division by zero is not allowed.")
else:
    # divide the two numbers
    answer:float = num1 / num2

    # print the output to the user
    print(f"The answer to the problem: {num1} / {num2}\n\t\
        Is: {answer}\n")
