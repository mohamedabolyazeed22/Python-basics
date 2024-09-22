# Start with a simple list of numbers
numbers_list = [1, 2, 3]
print(numbers_list)  # Output the original list

# Add a new number to the end of the list
numbers_list.append(4)
print(numbers_list)  # Check out the list with the new addition!

# Extend the list with multiple new numbers at once
numbers_list.extend([5, 6, 7])
print(numbers_list)  # The list is growing fast!

# Remove the last element in the list
del(numbers_list[6])
print(numbers_list)  # Oops, took one out. Let's see what's left!

# Remove a specific number by its value
numbers_list.remove(6)
print(numbers_list)  # The number 6 is out, the list is leaner!

# Pop the last item off the list
numbers_list.pop()
print(numbers_list)  # Say goodbye to the last item on the list.

# Pop an item by its index
numbers_list.pop(3)
print(numbers_list)  # The fourth item is gone now. Clean and neat!
