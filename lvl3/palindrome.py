# get the string from the user
user_input:str = input("Enter a string to check if it is a palindrome: ")

# pro way
if user_input == user_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# beginner way
string_length:int = len(user_input)
is_palindrome:bool = True
for i in range(string_length // 2):
    if user_input[i] != user_input[string_length - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
# check if list is a palindrome
user_list:list = []
list_length:int = int(input("Enter the length of the list: "))

for i in range(list_length):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# check if the list is a palindrome
list_length:int = len(user_list)
is_palindrome:bool = True
for i in range(list_length // 2):
    if user_list[i] != user_list[list_length - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
