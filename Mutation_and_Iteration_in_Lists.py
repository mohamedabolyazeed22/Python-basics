def remove_dups(l1, l2):
    # Iterate through each element in the first list (l1)
    for e in l1:
        # Check if the element exists in the second list (l2)
        if e in l2:
            # If the element is found in l2, remove it from l1
            l1.remove(e)

# Example lists
l1 = [1, 2, 3, 4, 5]  # Original list
l2 = [2, 3]           # Elements to be removed from l1

# Call the function to remove duplicates
remove_dups(l1, l2)

# Output the modified list (l1) after removing the duplicates
print(l1)  # Expected output: [1, 3, 4, 5]

def remove_dups(l1, l2):
    # Create a copy of the first list (l1) to avoid modifying it while iterating
    l1_copy = l1[:]
    
    # Iterate through each element in the copy of the first list
    for e in l1_copy:
        # Check if the element exists in the second list (l2)
        if e in l2:
            # If the element is found in l2, remove it from the original list (l1)
            l1.remove(e)

# Example lists
l1 = [1, 2, 3, 4, 5]  # Original list
l2 = [2, 3]           # Elements to be removed from l1

# Call the function to remove duplicates using the improved method
remove_dups(l1, l2)

# Output the modified list (l1) after removing the duplicates
print(l1)  # Expected output: [1, 4, 5]
