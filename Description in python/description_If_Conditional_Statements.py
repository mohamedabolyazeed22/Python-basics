# if Conditional Statements
# Conditional statements are used to execute different blocks of code based on certain conditions.

# 1. Basic if Statement
# Executes a block of code if the condition is True.
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# 2. if-else Statement
# Executes one block of code if the condition is True, and another block if it is False.
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")  # Output: y is not greater than 5

# 3. if-elif-else Statement
# Checks multiple conditions. Executes the block of code for the first True condition.
temperature = 25
if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's warm outside.")  # Output: It's warm outside.
else:
    print("It's cold outside.")

# 4. Nested if Statements
# An `if` statement inside another `if` statement.
a = 10
b = 20
if a > 5:
    if b > 15:
        print("a is greater than 5 and b is greater than 15.")  # Output: a is greater than 5 and b is greater than 15.

# 5. Ternary Conditional Expression
# A shorthand way to write simple `if-else` statements.
age = 18
message = "Adult" if age >= 18 else "Minor"
print(message)  # Output: Adult

# 6. Combining Conditions
# Multiple conditions can be combined using logical operators.
x = 15
y = 25
if x < 20 and y > 20:
    print("x is less than 20 and y is greater than 20.")  # Output: x is less than 20 and y is greater than 20.

# 7. Example with Comparison Operators
number = 10
if number % 2 == 0:
    print("The number is even.")  # Output: The number is even.
else:
    print("The number is odd.")
