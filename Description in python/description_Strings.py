# Strings in Python

# 1. String Declaration
# Strings are sequences of characters enclosed in quotes. You can use single (' '), double (" "), or triple (''' ''' or """ """) quotes.

# Examples of string declaration:
single_quote_string = 'Hello, World!'  # Using single quotes
double_quote_string = "Hello, World!"  # Using double quotes
triple_single_quote_string = '''Hello, 
World!'''  # Using triple single quotes for multi-line string
triple_double_quote_string = """Hello, 
World!"""  # Using triple double quotes for multi-line string

# 2. String Concatenation
# You can concatenate strings using the + operator.

# Example of string concatenation:
greeting = "Hello, " + "World!"  # Result: "Hello, World!"

# 3. String Repetition
# You can repeat strings using the * operator.

# Example of string repetition:
echo = "Hello! " * 3  # Result: "Hello! Hello! Hello! "

# 4. String Indexing
# Strings are indexed sequences. You can access individual characters using indices (starting from 0).

# Example of string indexing:
text = "Python"
first_character = text[0]  # Result: 'P'
last_character = text[-1]  # Result: 'n'

# 5. String Slicing
# You can obtain substrings by slicing the string using the [start:stop] syntax.

# Example of string slicing:
substring = text[1:4]  # Result: 'yth'

# 6. String Methods
# Strings have many built-in methods for manipulation.

# Examples of string methods:
uppercase_text = text.upper()  # Converts string to uppercase: 'PYTHON'
lowercase_text = text.lower()  # Converts string to lowercase: 'python'
title_text = text.title()  # Converts string to title case: 'Python'
replaced_text = text.replace('Python', 'Java')  # Replaces 'Python' with 'Java': 'Java'
split_text = text.split('t')  # Splits string by 't': ['Py', 'hon']

# 7. String Formatting
# You can format strings using f-strings (Python 3.6+) or the format() method.

# Examples of string formatting:
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."  # Using f-strings
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)  # Using format() method

# 8. String Escape Characters
# Use backslashes (\) to include special characters in strings.

# Examples of escape characters:
escaped_string = "He said, \"Hello!\""  # Includes double quotes in the string
newline_string = "Hello,\nWorld!"  # Includes a newline character
