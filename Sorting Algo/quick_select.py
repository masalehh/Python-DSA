def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 
    
    for j in range(low, high):
        if arr[i] < pivot:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
    
    
    
def quick_select(arr, low, high, k):
    if low <= high: 
        """
        "In Quick Sort, a single-element subarray is a base case that requires no action. 
        In Quick Select, a single-element subarray is the target that must be returned to 
        the caller. The <= ensures we don't exit the function empty-handed 
        when the search space converges."
        """
        pi = partition(arr, low, high)
        
        if pi == k:
            return arr[pi] 
        
        elif pi > k:
            return quick_select(arr, low, pi - 1, k) 
        else:
            return quick_select(arr, pi + 1, high, k) 