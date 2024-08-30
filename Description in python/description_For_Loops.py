# for Loops
# The `for` loop is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code for each item in the sequence.

# 1. Basic for Loop
# Iterates over each item in a sequence (e.g., a list).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry

# 2. Iterating Over a String
# Iterates over each character in a string.
word = "hello"
for char in word:
    print(char)  # Output: h, e, l, l, o

# 3. Using range() Function
# The `range()` function generates a sequence of numbers.
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# 4. Iterating with Indexes
# Use `enumerate()` to get both the index and the value in a loop.
animals = ["cat", "dog", "rabbit"]
for index, animal in enumerate(animals):
    print(index, animal)  # Output: 0 cat, 1 dog, 2 rabbit

# 5. Nested for Loops
# Use nested `for` loops to iterate over sequences within sequences.
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")  # Output: i=0, j=0, i=0, j=1, i=1, j=0, i=1, j=1, i=2, j=0, i=2, j=1

# 6. List Comprehensions
# A concise way to create lists using `for` loops within a single line.
squares = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]

# 7. Iterating Over Dictionaries
# Iterate over keys and values in a dictionary.
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")  # Output: name: Alice, age: 30

# 8. Iterating Over Sets
# Iterates over each item in a set.
numbers = {1, 2, 3, 4}
for number in numbers:
    print(number)  # Output: 1, 2, 3, 4 (order may vary as sets are unordered)

# 9. Using else with for Loop
# The `else` block is executed when the loop completes normally (not terminated by `break`).
for i in range(3):
    print(i)  # Output: 0, 1, 2
else:
    print("Loop has ended.")  # Output: Loop has ended.

# for Loops with Strings
# Iterating over characters in a string using a for loop.

# 1. Basic Iteration
# Iterate over each character in a string.
text = "Python"
for char in text:
    print(char)  # Output: P, y, t, h, o, n

# 2. Using Indexes
# Iterate over each character with its index using `range()` and `len()`.
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")  # Output: Index 0: P, Index 1: y, Index 2: t, ...

# 3. Slicing Strings
# Using `for` loops to iterate over substrings (slices) of a string.
for i in range(len(text) - 1):
    print(text[i:i+2])  # Output: Py, yt, th, ho, on

# 4. Reversing a String
# Iterate over a string in reverse order using slicing.
for char in text[::-1]:
    print(char)  # Output: n, o, h, t, y, P

# 5. Checking for Substrings
# Iterate over a string and check for a specific substring.
substring = "on"
for i in range(len(text) - len(substring) + 1):
    if text[i:i+len(substring)] == substring:
        print(f"Found '{substring}' starting at index {i}")  # Output: Found 'on' starting at index 4

# 6. Counting Characters
# Count occurrences of a specific character in a string.
char_to_count = 'o'
count = 0
for char in text:
    if char == char_to_count:
        count += 1
print(f"Character '{char_to_count}' appears {count} times.")  # Output: Character 'o' appears 1 times.

# 7. Constructing a New String
# Build a new string by concatenating characters based on some condition.
new_string = ""
for char in text:
    if char.isupper():  # Example condition
        new_string += char
print(f"Uppercase characters: {new_string}")  # Output: P

# 8. Capitalizing Each Character
# Convert each character to uppercase and build a new string.
upper_text = ""
for char in text:
    upper_text += char.upper()
print(upper_text)  # Output: PYTHON
