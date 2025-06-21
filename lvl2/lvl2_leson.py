# Get user input for age and height
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

# Check if the user meets the requirements
if age >= 12 and height >= 1.4:
    print("You can enter the rollercoaster!")
elif age < 12 and height >= 1.4:
    print("You are tall enough, but not old enough to enter the rollercoaster.")
elif age >= 12 and height < 1.4:
    print("You are old enough, but not tall enough to enter the rollercoaster.")
else:
    print("Sorry, you do not meet the age and height requirements.")

# Bonus: Show how many years or meters are missing
if age < 12:
    print(f"You need {12 - age} more year(s) to be old enough.")
if height < 1.4:
    print(f"You need {1.4 - height:.2f} more meter(s) to be tall enough.")

# Example of a loop: allow the user to check again
while True:
    again = input("Do you want to check another person? (yes/no): ")
    if again == "yes":
        age = int(input("Enter your age: "))
        height = float(input("Enter your height in meters: "))
        if age >= 12 and height >= 1.4:
            print("You can enter the rollercoaster!")
        elif age < 12 and height >= 1.4:
            print("You are tall enough, but not old enough to enter the rollercoaster.")
        elif age >= 12 and height < 1.4:
            print("You are old enough, but not tall enough to enter the rollercoaster.")
        elif age == -1 and height == -1:
            print("Nice try, but you cannot enter the rollercoaster with these values.")
            continue
        else:
            print("Sorry, you do not meet the age and height requirements.")
        if age < 12:
            print(f"You need {12 - age} more year(s) to be old enough.")
        if height < 1.4:
            print(f"You need {1.4 - height:.2f} more meter(s) to be tall enough.")
    elif again.lower() == "no":
        print("Goodbye!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")