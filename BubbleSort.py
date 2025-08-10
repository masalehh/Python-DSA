from typing import List, TypeVar 

T = TypeVar('T')

def bubble_sort_algo(arr:List[T]) -> List[T]:
    """
    Perform an in-place bubble sort on the given list.
    
    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The pass through the list
    is repeated until the list is sorted.
    
    Args:
        arr (List[T]): The list of comparable elements to be sorted.
    
    Returns:
        List[T]: The sorted list in ascending order.
    
    Time Complexity:
        - Worst case: O(n^2)
        - Best case: O(n) (if already sorted)
        - Average case: O(n^2)
    
    Space Complexity:
        - O(1) (in-place sorting)
    
    Example:
        >>> bubble_sort([3, 2, 1])
        [1, 2, 3]
    """

    n = len(arr)

    if n < 2:
        return arr      # Already sorted 
    
    for i in range(n):
        swapped = False 
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True 
        
        if not swapped:
            break
    return arr 


if __name__ == "__main__":
    mylist = [64, 34, 25, 90, 12, 107, 59, 22, 11, 90, 5]
    print("List before sorted: ", mylist) 
    sorted_list = bubble_sort_algo(mylist)
    print(f"Sorted List: {sorted_list}")



    

