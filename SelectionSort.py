

from typing import List, TypeVar

T = TypeVar('T')

def selection_sort_algo(arr: List[T]) -> List[T]:
    """
    Perform an in-place selection sort on the given list.

    Selection Sort works by repeatedly finding the minimum element from
    the unsorted portion of the list and moving it to the beginning.

    Args:
        arr (List[T]): A list of comparable elements to be sorted.

    Returns:
        List[T]: The sorted list in ascending order.

    Time Complexity:
        - Worst case: O(n^2)
        - Best case: O(n^2)
        - Average case: O(n^2)
    Space Complexity:
        - O(1) (in-place sorting)

    Example:
        >>> selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]
    """

    n = len(arr)
    if n < 2: 
        return arr  # Alrady sorted 
    
    for i in range(n-1):
        min_index = i 
        # Find the minimum in the unsorted portion
        for j in range(i+1, n):
            if  arr[min_index] > arr[j]:
                min_index = j 
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr 



if __name__ == "__main__":
    # Example usage
    data = [64, 11, 25, 109, 90, 12, 37, 22, 11, 90]
    print("Original list:", data)
    sorted_data = selection_sort_algo(data)
    print("Sorted list:", sorted_data)
    
