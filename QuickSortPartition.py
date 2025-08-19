from typing import List, Any 

def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low-1 
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return i+1 



def quicksort(arr: List[int], low: int, high: int):
    if low < high: 
        piv = partition(arr, low, high)
        quicksort(arr, low, piv-1)
        quicksort(arr, piv+1, high)
        
        

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted List: ", data)
size = len(data)
quicksort(data, 0, size-1)
print("Sorted List: ", data) 
    
    