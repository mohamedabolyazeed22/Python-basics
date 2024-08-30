x = 20
y = 15

# Swapping the values of x and y using tuple unpacking
x, y = y, x

print(x)  # Output: 15
print(y)  # Output: 20

def q_r(x, y):
    # Perform integer division and modulus operation
    q = x // y  # Integer division
    r = x % y   # Modulus (remainder)
    return (q, r)

# Call the function and print the result
result = q_r(9, 6)
print(result)  # Output: (1, 3)
