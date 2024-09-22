# bisection_search_algorithm
def bisection_search(arr, target):
    """
    Perform a bisection search to find the target in a sorted array.
    
    Parameters:
    arr (list): A sorted list of elements.
    target (int/float/str): The value to search for.
    
    Returns:
    int: The index of the target in the array if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Compute the middle index
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is smaller, ignore the right half
        elif arr[mid] > target:
            high = mid - 1
        
        # If target is larger, ignore the left half
        else:
            low = mid + 1
    
    # Target is not present in the array
    return -1

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11]
target_value = 7

index = bisection_search(sorted_list, target_value)
if index != -1:
    print(f"Target {target_value} found at index {index}.")
else:
    print(f"Target {target_value} not found in the list.")
