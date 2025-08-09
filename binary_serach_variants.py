# Different variants of binary search

from typing import Any, List, Callable 

def binary_search(arr: List[int], searchValue: int) -> int:
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == searchValue:
            return mid 
        elif arr[mid] < searchValue:
            left = mid + 1 
        else:
            right = mid - 1 
            
    return -1 


def binary_search_custom(arr: List[Any], searchValue:Any, key: Callable[[Any], Any]) -> int: 
    """
    Binary search using a custom key function for comparison.

    Parameters:
        arr (List[Any]): Sorted list of objects or values.
        target (Any): The value to search for.
        key (Callable): Function to extract comparison key from each element.

    Returns:
        int: Index of the matching element, or -1 if not found.
    """
    
    left, right = 0, len(arr)-1 
    while left <= right: 
        mid = (left+right) // 2 
        mid_value = key(arr[mid])
        if mid_value == searchValue:
            return mid 
        elif mid_value < searchValue:
            left = mid + 1 
        else:
            right = mid - 1 
            
    return -1 

def binary_search_first_occurence(arr:List[int], searchValue: int) -> int: 
    """
    Finds the first occurrence of the target in a sorted list with duplicates.

    Returns:
        int: Index of the first occurrence, or -1 if not found.
    """
    
    left, right = 0, len(arr)-1 
    result = -1 
    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == searchValue:
            result = mid 
            right = mid - 1 
        elif arr[mid] < searchValue:
            left = mid + 1 
        else:
            right = mid - 1 
    return result 



def binary_search_last_occurrence(arr: List[Any], searchValue: int) -> int: 
    """
    Finds the last occurrence of the target in a sorted list with duplicates.

    Returns:
        int: Index of the last occurrence, or -1 if not found.
    """
    
    left, right = 0, len(arr) - 1 
    result = -1
    while left <= right:
        mid = (left + right) // 2 
         
        if arr[mid] == searchValue:
            result = mid 
            left = mid + 1 
        elif arr[mid] < searchValue:
            left = mid + 1 
        else:
            right = mid - 1 
    return result 



def binary_search_float(arr: List[Any], searchValue: float, epsilon: float = 1e-6) -> int: 
    """
    Binary search for floating-point values with a tolerance (epsilon).

    Returns:
        int: Index of the value within epsilon of target, or -1 if not found.
    """
    
    left, right = 0, len(arr) - 1 
    
    while left <= right:
        mid = (left + right) // 2 
        if abs(arr[mid] - searchValue) < epsilon:
            return mid 
        elif arr[mid] < searchValue:
            left = mid + 1 
        else:
            right = mid - 1 
    
    return -1 

       
    

# === Example Usage ===
arr = [2, 4, 4, 4, 10, 15, 20, 23, 23, 27, 31, 31, 31]
float_arr = [1.1, 2.2, 3.3, 4.4, 5.5]
objects = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

print("Standard Binary Search:", binary_search(arr, 10))
print("First Occurrence of 4:", binary_search_first_occurence(arr, 31))
print("Last Occurrence of 4:", binary_search_last_occurrence(arr, 31)) 
print("Float Search (3.3):", binary_search_float(float_arr, 3.3))
print("Custom Key Search (id=2):", binary_search_custom(objects, 2, key=lambda x: x["id"]))