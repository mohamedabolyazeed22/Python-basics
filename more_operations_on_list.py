# Start with a fun string that shows love for Computer Science
s = "I <3 CS"
print(s)  # Display the original string

# Convert the string into a list of characters
char_list = list(s)
print("String turned into list:", char_list)  # See each character separated into a list

# Split the string around the "<" character
split_list = s.split("<")
print("String split around '<':", split_list)  # The string is split into parts around the "<"


# A list of characters spelling out a name
name_list = ['M', 'o', 'h', 'a', 'm', 'e', 'd']

# Join the characters together to form a complete name
full_name = ''.join(name_list)

# Print the original list (no changes made to it)
print("Original list of characters:", name_list)  # Shows the list still intact

# Print the full name formed by joining the characters
print("Full name created from the list:", full_name)  # Shows the complete name

# A list of numbers, some positive and some negative
list_sort = [1, 5, -3, 20, 4, 9]

# Sort the list in ascending order and store it in a new variable
sorted_num = sorted(list_sort)

# Print the sorted list of numbers
print("Sorted list of numbers:", sorted_num)  # The numbers are now in order, from smallest to largest
