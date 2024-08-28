# 1. Numeric Types
# int (Integer): Represents whole numbers, both positive and negative, without a decimal point.
x = 10  # Example of an integer
y = -5  # Example of a negative integer

# float (Floating-Point Number): Represents real numbers with a decimal point.
pi = 3.14  # Example of a float
temperature = -2.5  # Example of a negative float

# complex (Complex Number): Represents numbers with a real and an imaginary part.
z = 3 + 4j  # Example of a complex number with real part 3 and imaginary part 4j

# 2. Sequence Types
# str (String): Represents a sequence of characters (text).
name = "Mohamed"  # Example of a string
greeting = 'Hello, World!'  # Another example of a string

# list (List): An ordered collection of items, which can be of different data types.
numbers = [1, 2, 3, 4]  # Example of a list of integers
mixed = [1, "apple", 3.14]  # Example of a mixed-type list

# tuple (Tuple): Similar to a list, but immutable.
coordinates = (10, 20)  # Example of a tuple with two integers
person = ("Alice", 25)  # Example of a tuple with a string and an integer

# range (Range): Represents a sequence of numbers, typically used in loops.
sequence = range(0, 10)  # Example of a range from 0 to 9
step_sequence = range(5, 15, 2)  # Example of a range from 5 to 14 with a step of 2

# 3. Mapping Type
# dict (Dictionary): An unordered collection of key-value pairs.
person_info = {"name": "Mohamed", "age": 25}  # Example of a dictionary with two key-value pairs
scores = {"math": 90, "science": 85}  # Example of a dictionary with subject scores

# 4. Set Types
# set (Set): An unordered collection of unique items.
fruits = {"apple", "banana", "cherry"}  # Example of a set of fruits
unique_numbers = {1, 2, 3, 4}  # Example of a set of unique numbers

# frozenset (Frozen Set): Similar to a set, but immutable.
immutable_set = frozenset([1, 2, 3])  # Example of a frozenset, which cannot be modified

# 5. Boolean Type
# bool (Boolean): Represents one of two values: True or False.
is_active = True  # Example of a boolean value representing True
is_empty = False  # Example of a boolean value representing False

# 6. Binary Types
# bytes: Represents a sequence of bytes (immutable).
byte_data = b"Hello"  # Example of a bytes object

# bytearray: A mutable sequence of bytes.
byte_array = bytearray(5)  # Example of a bytearray with 5 bytes

# memoryview: Allows access to the memory of an object without copying it.
mem_view = memoryview(byte_data)  # Example of a memoryview object created from a bytes object

# 7. None Type
# NoneType: Represents the absence of a value or a null value.
result = None  # Example of a variable with a NoneType value
value = None  # Another example of a NoneType value, often used as a default
