# Initial lists with the same elements
L1 = [1, 2, 3]
L2 = [1, 2, 3]

print("Original L1:", L1)  # Display the initial list L1
print("Original L2:", L2)  # Display the initial list L2

# Modify the first element of L1
L1[0] = 5
print("Modified L1:", L1)  # L1 now starts with 5, but L2 remains unchanged

# Reassign L1 to a new list and make L2 reference this new list
L1 = [4, 5, 6]
L2 = L1  # L2 now refers to the same list as L1
print("New L1:", L1)  # Display the new list L1
print("New L2:", L2)  # L2 reflects the change since it points to the same list as L1

# Modify an element of L1, which also affects L2 because they reference the same list
L1[1] = 10
print("Updated L1:", L1)  # L1 shows the updated value
print("Updated L2:", L2)  # L2 also reflects the updated value

# Corrected slicing (Example: Slicing the list to get a sublist)
L1 = [10, 20, 30]
L2 = L1[1:3]  # Correctly slice the list to get elements from index 1 to 2
print("Final L1:", L1)  # L1 remains unchanged
print("Final L2:", L2)  # L2 contains elements [20, 30] from the sliced list
