# More Operations on Strings

# 1. Finding Substrings
# Use the `find()` method to locate the position of a substring. Returns -1 if not found.
text = "Hello, World!"
position = text.find("World")  # Result: 7

# 2. Checking for Substrings
# Use the `in` operator to check if a substring exists within a string.
exists = "World" in text  # Result: True

# 3. String Splitting
# Use the `split()` method to divide a string into a list of substrings based on a delimiter.
text = "apple,banana,cherry"
split_list = text.split(",")  # Result: ['apple', 'banana', 'cherry']

# 4. Joining Strings
# Use the `join()` method to concatenate a list of strings into a single string, with a specified separator.
words = ["Hello", "World"]
joined_string = " ".join(words)  # Result: "Hello World"

# 5. Stripping Whitespace
# Use the `strip()` method to remove leading and trailing whitespace from a string.
whitespace_text = "   Hello, World!   "
stripped_text = whitespace_text.strip()  # Result: "Hello, World!"

# 6. Padding Strings
# Use the `rjust()`, `ljust()`, and `center()` methods to pad strings with a specified character.
padded_right = "Hello".rjust(10, '-')  # Result: "-----Hello"
padded_left = "Hello".ljust(10, '-')  # Result: "Hello-----"
centered = "Hello".center(10, '*')  # Result: "**Hello***"

# 7. Changing Case
# Convert strings to uppercase, lowercase, or title case using `upper()`, `lower()`, and `title()` methods.
text = "python programming"
uppercase = text.upper()  # Result: "PYTHON PROGRAMMING"
lowercase = text.lower()  # Result: "python programming"
title_case = text.title()  # Result: "Python Programming"

# 8. Checking String Properties
# Use methods like `isalpha()`, `isdigit()`, and `isspace()` to check the properties of strings.
alpha_check = "Hello".isalpha()  # Result: True (all characters are alphabetic)
digit_check = "1234".isdigit()  # Result: True (all characters are digits)
space_check = "   ".isspace()  # Result: True (all characters are whitespace)

# 9. Replacing Substrings
# Use the `replace()` method to replace occurrences of a substring with another substring.
text = "I love cats"
new_text = text.replace("cats", "dogs")  # Result: "I love dogs"

# 10. Counting Occurrences
# Use the `count()` method to count the number of occurrences of a substring.
text = "ababab"
count = text.count("ab")  # Result: 3

# 11. Formatting Strings
# Use formatted string literals (f-strings) or the `format()` method to insert variables into strings.
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."  # Using f-strings
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)  # Using format() method

# 12. Checking Prefix and Suffix
# Use `startswith()` and `endswith()` to check if a string starts or ends with a specific substring.
starts_with = text.startswith("abab")  # Result: True
ends_with = text.endswith("abab")  # Result: True
