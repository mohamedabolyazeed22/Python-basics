# Get an integer from the user
user_input = int(input("Enter an integer: "))

# Check if the number is even or odd using the modulo operator (%)
if user_input % 2 == 0:
    # If the remainder is 0, the number is even!
    print("The number", user_input, "is even!")
else:
    # If the remainder is not 0, the number is odd!
    print("The number", user_input, "is odd!")

# Print a success message to let the user know we're done
print("Done with conditional!")