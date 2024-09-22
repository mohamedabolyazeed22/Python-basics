# Function to print a custom greeting message
def print_hello():
    # Print a message indicating the role of a penetration tester
    print("Hello, I am a Penetration Tester!")

# Call the function to display the greeting message
print_hello()

# Function to calculate and print the sum of two numbers
def print_sum(num1, num2):
    # Calculate the sum of num1 and num2
    total = num1 + num2
    # Print the result of the addition
    print(f"The sum of {num1} and {num2} is {total}")

# Call the function with example numbers to display their sum
print_sum(10, 16)

# Function to estimate the value of pi (π) using a simple fraction
def pi():
    # Return an approximation of pi using the fraction 22/7
    return 22 / 7

# Calculate the circumference of a circle with radius 7 using the estimated value of pi
radius = 7
circumference = 2 * radius * pi()
print(f"The circumference of a circle with radius {radius} is approximately {circumference:.2f}")

# Function to check if a number is even
def is_even(num):
    # Return True if num is even, otherwise return False
    return num % 2 == 0

# Check if 6 is even and print the result
print(f"Is 6 even? {is_even(6)}")
