from typing import List, TypeVar, Any

T = TypeVar('T', bound=Any)

def merge_sort(arr: List[T]) -> List[T]:
    """
    Merge Sort Algorithm
    --------------------
    A stable, divide-and-conquer sorting algorithm.
    Time Complexity: O(n log n) in all cases.
    Space Complexity: O(n) due to temporary arrays.
    
    Parameters:
        arr (List[T]): The list to be sorted.
    
    Returns:
        List[T]: A new sorted list.
    """
    
    if len(arr) <= 1:
        return arr 
    
    
    # Split array into two subarrays 
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: List[T], right: List[T]) -> List[T]:
    """Helper function to merge two sorted lists."""
    merged = [] 
    i = j = 0
    
    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1 
        else:
            merged.append(right[j])
            j+=1 
                
    # Collect remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged 
    
    
    # Example usage
if __name__ == "__main__":
    nums = [38, 27, 43, -80, 3, 9, 82, 10]
    print("Original:", nums)
    print("Sorted:", merge_sort(nums))