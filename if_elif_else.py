# Get an integer from the user
user_input = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero
if user_input > 0:
    # If the number is greater than 0, it's positive!
    print("The number", user_input, "is positive!")
elif user_input < 0:
    # If the number is less than 0, it's negative!
    print("The number", user_input, "is negative!")
else:
    # If the number is neither greater nor less than 0, it must be zero!
    print("The number is zero!")

# Print a success message to let the user know we're done
print("Done with conditional!")
