# Comparison operators

# Greater than
print(1 > 2)  # False

# Less than
print(1 < 2)  # True

# Less than or equal to
print(2 <= 2)  # True

# Equal to
print(2 == 2)  # True

# Equal to (different from above)
print(2 == 3)  # False

# Not equal to
print(2 != 2)  # False

# Not equal to 
print(3 != 2)  # True 

# Define boolean variables
a = True
b = False

# Evaluate expressions
result_not_a = not a
result_a_and_b = a and b
result_a_and_not_b = a and (not b)
result_a_or_b = a or b
result_not_a_or_b = (not a) or b

# Print results
print(f"not a: {result_not_a}")
print(f"a and b: {result_a_and_b}")
print(f"a and (not b): {result_a_and_not_b}")
print(f"a or b: {result_a_or_b}")
print(f"(not a) or b: {result_not_a_or_b}")