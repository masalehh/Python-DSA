from typing import List

def counting_sort(arr: List[int], exp: int) -> None:
    """
    A stable counting sort based on the digit at 'exp' place.
    
    Args:
        arr: The list of integers to be sorted.
        exp: The digit's place (1, 10, 100, ...).
    """
    
    n = len(arr) 
    output = [0] * n            # For Output sorted list 
    count = [0] * 10            # Because digits range from 0-9 
    
    
    # Count occurrences of each digit at current exp
    for num in arr: 
        index = (num // exp) % 10 
        count[index] += 1 
        
        
    # Convert count to prefix sum to get positions
    for i in range(1, 10):
        count[i] += count[i-1]
        
    
    # Build output array (stable, so traverse from right)
    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10 
        output[count[index] - 1] = arr[i]
        count[index] -= 1 
    
    # Copy output to arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr: List[int]) -> None: 
    """
    Radix Sort using Counting Sort as a stable subroutine.
    Sorts the list of non-negative integers in-place.

    Args:
        arr: List of integers to be sorted.
    """
    
    if not arr: 
        return  
    
    # Find maximum number to know number of digits
    max_val = max(arr) 
    
    # Sort by each digit (exp = 1, 10, 100, ...)
    exp = 1 
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10 
        
        
if __name__ == "__main__":
    nums = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Before sorting:", nums)
    radix_sort(nums)
    print("After sorting: ", nums)
