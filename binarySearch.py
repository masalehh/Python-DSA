
from typing import List 

def binary_search(arr:List[int], searchValue:int) -> int: 
    """
    Perform binary search on a sorted list of integers.

    Parameters:
        arr (List[int]): The sorted list to search.
        target (int): The value to search for.

    Returns:
        int: Index of the target if found, else -1.
    """
    
    left , right = 0, len(arr)-1
    
    while left <= right:
        mid = (left+right)//2 
        if arr[mid] == searchValue:
            return mid 
        elif arr[mid] < searchValue:
            left = mid+1 
        else:
            right = mid-1 
            
    return -1 

if __name__ == "__main__":
    sorted_list = [2, 5, 8, 12, 14, 16, 23, 38, 56, 72, 87, 91]
    searchValue = 72
    
    searhValueIndex = binary_search(sorted_list, searchValue)
    
    if searhValueIndex != -1:
         print(f"Target {searchValue} found at index {searhValueIndex}.")
    else:
        print(f"Target {searchValue} not found.")
    
    
    searchValue = 720
    searhValueIndex = binary_search(sorted_list, searchValue)
    
    if searhValueIndex != -1:
         print(f"Target {searchValue} found at index {searhValueIndex}.")
    else:
        print(f"Target {searchValue} not found.")