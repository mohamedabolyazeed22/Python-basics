# Get an integer from the user
user_input = int(input("Enter an integer: "))

# Check if the number is between 1 and 100 inclusive
if user_input >= 1 and user_input <= 100:
    print("The number", user_input, "is between 1 and 100!")
elif user_input < 0 or user_input > 100:
    print("The number", user_input, "is outside the range of 1 to 100!")
else:
    # If the number is 0, which is neither positive nor negative
    print("The number is 0, which is not between 1 and 100!")

# Print a success message to let the user know we're done
print("Done with conditional!")
