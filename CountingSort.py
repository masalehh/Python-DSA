from typing import List 

def counting_sort(arr:List[int]) -> List[int]: 
    """
    Perform counting sort on a list of integers.

    This algorithm is stable for integers when the counting array
    is processed in a prefix-sum manner. It works best when the
    range of input values (max_val - min_val) is not significantly
    larger than the number of elements.

    Time Complexity: O(n + k), where n is the number of elements 
                     and k is the range of input values.
    Space Complexity: O(n + k)

    Args:
        arr (List[int]): List of integers to sort.

    Returns:
        List[int]: Sorted list of integers.
    """
    if not arr:         # Edge case: empty input
        return [] 
    if len(arr) == 1:
        return arr 
    
    # Find the min and max to handle negative numbers
    min_value, max_value = min(arr), max(arr)
    element_range = max_value - min_value + 1 
    
    
    # Step 1: Initialize the counting array
    count = [0] * element_range 
    
    
    # Step 2: Store the count of each element
    for num in arr:
        count[num-min_value] += 1 
        
    print(count)
    # Step 3: Convert count array to prefix sum (for stable sort)
    for i in range(1, len(count)):
        count[i] += count[i - 1]
     
      
    # Step 4: Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num-min_value] -= 1 
        output[count[num-min_value]] = num 
    return output


# Example usage:
if __name__ == "__main__":
    data = [4, 2, -1, 3, 2, 1, 4]
    print("Original:", data)
    sorted_data = counting_sort(data)
    print("Sorted:", sorted_data)
    