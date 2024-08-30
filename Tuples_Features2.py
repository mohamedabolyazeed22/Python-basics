# Creating tuples
t1 = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = (1, "hello", 3.5)

# Accessing elements
print(t1[0])  # Output: 1
print(t2[1:3])  # Output: ('b', 'c')

# Nested tuples
nested = (1, (2, 3), (4, 5, 6))
print(nested[1])  # Output: (2, 3)

# Immutable property
# t1[0] = 10  # This will raise a TypeError

# Hashable tuple
my_dict = { (1, 2): "tuple as key" }
print(my_dict[(1, 2)])  # Output: tuple as key
