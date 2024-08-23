# 🌟 Exploring the Name "Mohamed" 🌟

# Assign the name to a variable
name__one = "Mohamed"

# Access and print the 5th character (index 4)
print("Character at index 4:", name__one[4])  # Output: 'm'

# Access and print the 3rd character from the end (index -3)
print("Character at index -3:", name__one[-3])  # Output: 'm'

# Slice and print the first two characters (index 0 to 2, but not including 2)
print("First two characters:", name__one[0:2])  # Output: 'Mo'

# Slice and print characters from index 2 to 4 (not including 4)
print("Characters from index 2 to 4:", name__one[2:4])  # Output: 'ha'

# Slice and print from index 4 to the end of the string
print("Characters from index 4 to end:", name__one[4:])  # Output: 'med'

# Slice and print characters from the start up to index 6 (not including 6)
print("Characters from start to index 6:", name__one[:6])  # Output: 'Mohame'

# Slice and print from index 4 to 6 (not including 6)
print("Characters from index 4 to 6:", name__one[4:6])  # Output: 'me'

# Check if "Mo" is in the name and print the result
print("Is 'Mo' in the name?:", "Mo" in name__one)  # Output: True

# Print characters from index 0 to 5 with a step of 2
print(name__one[0:5:2])  # Output: 'Mhm'

# Print the string in reverse order
print(name__one[::-1])  # Output: 'demahoM'

# Print the string with the default step of 1 (essentially the same as the original string)
print(name__one[::1])  # Output: 'Mohamed'

# Print every third character from the string
print(name__one[::3])  # Output: 'Moe'
