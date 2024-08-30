# 1. print() Function
# The `print()` function outputs text or variables to the console.

# Basic usage:
print("Hello, World!")  # Output: Hello, World!

# Printing multiple items:
print("Name:", "Alice", "Age:", 30)  # Output: Name: Alice Age: 30

# Using separators and end parameters:
print("Hello", "World", sep=", ")  # Output: Hello, World
print("Hello", end=" ")  # Keeps the cursor on the same line
print("World!")  # Output: Hello World!

# Printing formatted strings using f-strings:
name = "Bob"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Bob and I am 25 years old.

# Printing with format() method:
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is Bob and I am 25 years old.

# 2. input() Function
# The `input()` function reads a line of text from the user input.

# Basic usage:
user_input = input("Enter your name: ")  # Prompts the user and stores input in 'user_input'
print("Hello, " + user_input)  # Output: Hello, [user_input]

# Converting input to a specific type (e.g., integer):
age = int(input("Enter your age: "))  # Converts the input to an integer
print("You are", age, "years old.")  # Output: You are [age] years old.

# Handling invalid input with try-except:
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input! Please enter a valid number.")
