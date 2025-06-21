# Get integer input from the user
n = int(input("Enter an integer: "))

# beginner 
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()  # Move to the next line after printing stars

print()  # Blank line between triangles

# intermediate
for i in range(1, n + 1):
    print('*' * i)

print()  # Blank line between triangles

# pro
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)