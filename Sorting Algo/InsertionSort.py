
from typing import List, TypeVar, Protocol

class Comparable(Protocol):
    def __lt__(self, other: "Comparable") -> bool: ...
    def __gt__(self, other: "Comparable") -> bool: ...

T = TypeVar('T', bound="Comparable") 

def insertionSort(arr: List[T]) -> None: 
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    This function modifies the list in-place.

    Time Complexity:
        - Best Case: O(n) when already sorted
        - Worst Case: O(n^2) when sorted in reverse order
    Space Complexity:
        - O(1) (in-place sorting)

    Args:
        arr (List[T]): The list of comparable elements to be sorted.

    Example:
        >>> nums = [5, 2, 1, 64, 34, 25, 12, 9, 22, 11, 90, 5]
        >>> insertion_sort(nums)
        >>> nums
        [1, 2, 5, 5, 9, 11, 11, 12, 22, 25, 34, 64, 90]
    """
    

    for i in range(1, len(arr)):
        key_item = arr[i] 
        j = i - 1 
        
        # Move elements greater than key_item one position ahead
        while j >= 0 and arr[j] > key_item:
            arr[j+1] = arr[j] 
            j -= 1 
            
        arr[j + 1] = key_item 



if __name__ == "__main__":
    data = [5, 2, 1, 64, 11, 34, 25, 12, 9, 22, 11, 90, 5]
    print("Before sorting:", data)
    insertionSort(data)
    print("After sorting:", data)