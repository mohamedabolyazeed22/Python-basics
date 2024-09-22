# Creating an empty tuple 't'
t = ()
# Checking the type of 't', which should be <class 'tuple'>
print(type(t))  # Output: <class 'tuple'>

# Creating a tuple 'tup' with mixed data types: integers and strings
tup = (1, "c", 3, "num")
# Printing the tuple
print(tup)  # Output: (1, 'c', 3, 'num')

# Accessing and printing the element at index 3 in 'tup'
print(tup[3])  # Output: num

# Accessing and printing the element at index 2 in 'tup'
print(tup[2])  # Output: 3

# Creating a new tuple 'tup2' by concatenating 'tup' with another tuple (20, 30)
tup2 = tup + (20, 30)
# Printing the new tuple
print(tup2)  # Output: (1, 'c', 3, 'num', 20, 30)

# Slicing 'tup2' to get a sub-tuple from index 1 to 2 (not including 2)
print(tup2[1:2])  # Output: ('c',)

# Demonstrating the difference between a string and a single-element tuple
x = ("c")   # This is just a string, not a tuple
y = ("c",)  # This is a single-element tuple
print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'tuple'>

# Creating a normal integer
x1 = 10
# Creating a single-element tuple
x2 = 10,

# Printing the type of 'x1', which is an integer
print(type(x1))  # Output: <class 'int'>
# Printing the type of 'x2', which is a tuple
print(type(x2))  # Output: <class 'tuple'>
