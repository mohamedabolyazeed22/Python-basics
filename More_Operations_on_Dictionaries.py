# Create a dictionary where numbers represent keys and names represent values
dic = {1: "Mohamed", 2: "Ahmed"}

# Use the get() method to retrieve the value for a specific key
# It returns the value if the key exists, and 'None' (or a default value) if the key doesn't exist
value = dic.get(1)  # Retrieves "Mohamed" because key 1 exists
print(f"Value for key 1: {value}")

# Attempt to retrieve a value for a non-existing key, using a default return value
value = dic.get(5, "Not Found")  # Since key 5 doesn't exist, returns the default "Not Found"
print(f"Value for key 5: {value}")

# Use the update() method to merge another dictionary or add/update multiple key-value pairs
# Adding new keys 3 and 4 to the dictionary, and updating the value of key 2
dic.update({3: "Sara", 4: "John", 2: "Ali"})
print(f"Updated dictionary: {dic}")  # Now contains {1: "Mohamed", 2: "Ali", 3: "Sara", 4: "John"}

# Use pop() to remove a specific key and return its value
removed_value = dic.pop(4)  # Removes key 4 ("John") and returns the value
print(f"Removed value: {removed_value}")
print(f"Dictionary after popping key 4: {dic}")

# pop() with a default value when the key does not exist
removed_value = dic.pop(5, "No such key")  # Key 5 does not exist, returns default value
print(f"Attempt to pop key 5: {removed_value}")

# Use popitem() to remove and return the last key-value pair added to the dictionary
last_item = dic.popitem()  # Removes and returns the last inserted key-value pair
print(f"Last item removed: {last_item}")
print(f"Dictionary after popitem: {dic}")

# Use setdefault() to get the value of a key if it exists, or insert it if it doesn't
# In this case, key 5 does not exist, so it will be added with the value "New Value"
default_value = dic.setdefault(5, "New Value")
print(f"Value for key 5 after setdefault: {default_value}")
print(f"Dictionary after setdefault: {dic}")

# Use clear() to remove all items from the dictionary
dic.clear()  # Completely empties the dictionary
print(f"Dictionary after clear(): {dic}")
