# get the boolean values from the user
bool1:bool = input("Enter first boolean value (True/False): ")
bool2:bool = input("Enter second boolean value (True/False): ")

# convert the input strings to boolean values
bool1 = bool1 == 'True'
bool2 = bool2 == 'True'
# perform the logical operations
and_result:bool = bool1 and bool2
or_result:bool = bool1 or bool2
not_result1:bool = not bool1
not_result2:bool = not bool2
# print the results to the user
print(f"The result of {bool1} AND {bool2} is: {and_result}")
print(f"The result of {bool1} OR {bool2} is: {or_result}")
print(f"The result of NOT {bool1} is: {not_result1}")
print(f"The result of NOT {bool2} is: {not_result2}")