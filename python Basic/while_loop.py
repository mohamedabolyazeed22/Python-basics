# Initialize user_input with a negative value to enter the loop
user_input = -1

# Keep asking the user for a positive integer until they provide one
while user_input <= 0:
    user_input = int(input("Enter a positive integer: "))

# Once a positive integer is provided, print a success message
print("You entered a positive integer:", user_input)
