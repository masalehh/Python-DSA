
def linear_search(arr, searchValue):
    """
    Searches for the target value in the given list using linear search.

    Parameters:
        arr (list): The list of elements to search through.
        target (Any): The value to search for.

    Returns:
        int: The index of the target if found, else -1.
    """
    
    # Iterate through the list using index and value 
    for index, value in enumerate(arr):
        if value == searchValue:    
            return index            # Return index if search value found 
    return -1                       # Return -1 if searchValue not found 


# Example usage 
if __name__ == "__main__":
    sample_list = [5, 8, 13, 21, 34, 3, 106]
    
    searchValue = 34 
    
    index = linear_search(sample_list, searchValue)
    
    if index != -1:
        print(f"Searched Value {searchValue} found at index {index}")
    else:
        print(f"Searched Value {searchValue} not found in thie list") 
        
    searchValue = 321 
    
    index = linear_search(sample_list, searchValue)
    
    if index != -1:
        print(f"Searched Value {searchValue} found at index {index}")
    else:
        print(f"Searched Value {searchValue} not found in the list") 