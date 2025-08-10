# Different variants of binary search alogorithm 

from typing import List, Any, Callable

def  binary_search(arr:List[int], searchValue:int) -> int:
    left , right = 0, len(arr)-1 


    while left <= right: 
        mid = (left+right) // 2 
        if arr[mid] == searchValue:
            return mid 
        elif arr[mid] < searchValue:
            left = mid + 1 
        else:
            right = mid - 1 
    return -1 



# === Example Usage ===
arr = [2, 4, 4, 4, 10, 15, 20]
print(f"Binary Search for value {10} is at index: ", binary_search(arr, 10))