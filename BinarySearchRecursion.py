
from typing import List 
def binary_search_recursive(arr:List[int], searchValue:int, left: int, right: int) -> int:
    """
    Recursive binary search function.

    Returns:
        int: Index of target if found, else -1.
    """
    if left > right:
        return -1 
    
    mid = (left + right) // 2 
    
    if arr[mid] == searchValue:
        return mid 
    elif arr[mid] < searchValue:
        return binary_search_recursive(arr, searchValue, mid+1, right)
    else:
        return binary_search_recursive(arr, searchValue, left, mid-1)
    
   
    
if __name__ == "__main__":
    sorted_list = [2, 5, 8, 12, 14, 16, 23, 38, 56, 72, 87, 91]
    searchValue = 72
    
    searhValueIndex = binary_search_recursive(sorted_list, searchValue, 0, len(sorted_list)-1)
    
    if searhValueIndex != -1:
         print(f"Target {searchValue} found at index {searhValueIndex}.")
    else:
        print(f"Target {searchValue} not found.")
    
    
    searchValue = 720
    searhValueIndex = binary_search_recursive(sorted_list, searchValue, 0, len(sorted_list)-1)
    
    if searhValueIndex != -1:
         print(f"Target {searchValue} found at index {searhValueIndex}.")
    else:
        print(f"Target {searchValue} not found.")
