# Comparison Operators
# Comparison operators are used to compare two values and return a boolean result (True or False).

# 1. Equality (==): Checks if two values are equal.
a = 5
b = 10
result = (a == b)  # Result: False

# 2. Inequality (!=): Checks if two values are not equal.
result = (a != b)  # Result: True

# 3. Greater Than (>): Checks if the left value is greater than the right value.
result = (a > b)  # Result: False

# 4. Less Than (<): Checks if the left value is less than the right value.
result = (a < b)  # Result: True

# 5. Greater Than or Equal To (>=): Checks if the left value is greater than or equal to the right value.
result = (a >= b)  # Result: False

# 6. Less Than or Equal To (<=): Checks if the left value is less than or equal to the right value.
result = (a <= b)  # Result: True

# Logical Operators
# Logical operators are used to combine multiple boolean expressions.

# 1. AND (and): Returns True if both expressions are True.
x = True
y = False
result = (x and y)  # Result: False

# 2. OR (or): Returns True if at least one of the expressions is True.
result = (x or y)  # Result: True

# 3. NOT (not): Returns True if the expression is False; returns False if the expression is True.
result = not x  # Result: False

# 4. Combining Comparison and Logical Operators
# You can combine multiple comparison and logical operators to form more complex conditions.

# Example:
age = 20
has_id = True
can_vote = (age >= 18) and has_id  # Result: True

# Another example:
temperature = 25
is_hot = (temperature > 30) or (temperature > 20 and temperature <= 30)  # Result: True
