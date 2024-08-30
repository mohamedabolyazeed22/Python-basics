# while Loops
# The `while` loop repeatedly executes a block of code as long as a specified condition is True.

# 1. Basic while Loop
# Executes the block of code as long as the condition is True.
count = 0
while count < 5:
    print(count)  # Output: 0 1 2 3 4
    count += 1  # Increment count to avoid infinite loop

# 2. Infinite Loop
# A `while` loop that runs indefinitely. You need to include a break condition to exit.
while True:
    print("This will print indefinitely.")
    break  # Exit the loop after one iteration

# 3. Using break Statement
# The `break` statement is used to exit the loop prematurely.
number = 0
while number < 10:
    if number == 5:
        break  # Exit the loop when number is 5
    print(number)  # Output: 0 1 2 3 4
    number += 1

# 4. Using continue Statement
# The `continue` statement skips the current iteration and proceeds with the next iteration.
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue  # Skip printing when number is 3
    print(number)  # Output: 1 2 4 5

# 5. Using else with while Loop
# The `else` block is executed when the `while` loop condition becomes False.
count = 0
while count < 3:
    print(count)  # Output: 0 1 2
    count += 1
else:
    print("Loop has ended.")  # Output: Loop has ended.

# 6. Example with Multiple Conditions
# You can use multiple conditions within the `while` loop.
x = 0
y = 10
while x < y:
    print(x, y)  # Output: 0 10, 1 10, 2 10, 3 10, 4 10, 5 10, 6 10, 7 10, 8 10, 9 10
    x += 1
    y -= 1

# 7. Using Input in a while Loop
# You can use `input()` to get user input and control the loop based on it.
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type 'exit' to stop: ")  # Prompts the user to type 'exit' to end the loop
    print("You typed:", user_input)
