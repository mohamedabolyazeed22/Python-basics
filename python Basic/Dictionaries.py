# Create a dictionary where numbers represent keys and names represent values
dic = {1: "Mohamed", 2: "Ahmed"}

# Print the entire dictionary to display all key-value pairs
print(dic)

# Access and print the value associated with key 1 (which is "Mohamed")
print(dic[1])  # Fetch the value linked to key 1 and display "Mohamed"

# Add a new key-value pair to the dictionary, with key 3 and value "Abdo"
dic[3] = "Abdo"

# Print the updated dictionary to include the new key-value pair
print(dic)

# Check if the value "Mohamed" is in the dictionary's values
print("Mohamed" in dic.values())  # This will return True if "Mohamed" exists in the dictionary

# Delete the key-value pair where the key is 2 (associated with "Ahmed")
del dic[2]

# Print the updated dictionary after deletion
print(dic)

# Access and print all the keys in the dictionary
print(dic.keys())  # Outputs dict_keys([1, 2])

# Access and print all the values in the dictionary
print(dic.values())  # Outputs dict_values(['Mohamed', 'Ahmed'])

# Iterate over all keys and print them
for key in dic.keys():
    print(f"Key: {key}")

# Iterate over all values and print them
for value in dic.values():
    print(f"Value: {value}")

# Iterate over key-value pairs
for key, value in dic.items():
    print(f"Key: {key}, Value: {value}")


