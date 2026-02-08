from typing import List, TypeVar, Any 

T = TypeVar('T', bound=Any)  # T must support comparison operators

def quick_sort(arr: List[T]) -> List[T]:
    """
    Quick Sort Algorithm
    --------------------
    A divide-and-conquer sorting algorithm with an average time 
    complexity of O(n log n). Worst case is O(n^2), but with good 
    pivot selection (randomized/median), it performs well in practice.
    
    Parameters:
        arr (List[T]): The list to be sorted.
    
    Returns:
        List[T]: A new sorted list.
    """
    
    # Base Case: already sorted if 0 or 1 element 
    if len(arr) <= 1:
        return arr 
    
    # Choose pivot (here: middle element for balance)
    pivot = arr[len(arr) // 2]
    
    #partiion into three lists 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]   # handles duplicates 
    right = [x for x in arr if x > pivot]
    
    
    # Recursively sort sublists
    return quick_sort(left) + middle + quick_sort(right)


# Example usage 
if __name__ == "__main__":
    nums = [10, 7, 8, 802, 9, 1, -25, 5]
    print("Original:", nums)
    print("Sorted:", quick_sort(nums))