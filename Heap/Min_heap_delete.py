

def delete_min(self):
    if not self.heap:
        return None 
    
    root = self.heap[0]
    last = self.heap.pop() 
    
    if self.heap:
        self.heap[0] = last 
        self._heapify_down(0)
    return root 


def _heapify_down(self, i ):
    n = len(self.heap) 
    
    while True: 
        left = 2*i + 1 
        right = 2*i + 2 
        smallest = i 
        
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left 
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right 
            
        if smallest == i: 
            break 
        
        self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
        i = smallest 
        
        
        
"""
Deletion from a Min Heap 
Now we simulate deletion from a Min-Heap (delete_min) step-by-step — the operation most candidates get wrong.
We will start from the heap obtained earlier:
[2, 5, 14, 10, 9]

Tree view:
       2
       / \
      5  14
     / \
   10   9

Goal: remove the minimum (root = 2)

Step 1 — Remove root and move last element to root
Last element = 9
Array becomes:
[9, 5, 14, 10]

Tree:
       9
       / \
      5  14
     /
   10

Heap property is broken → we must heapify-down.

Step 2 — Compare with children
Children of 9:
left = 5


right = 14


Smallest child = 5
Swap:
[5, 9, 14, 10]

Tree:
       5
       / \
      9  14
     /
   10


Step 3 — Continue heapify-down
Now node = 9
Children:
left = 10


right = none


10 is larger → no swap
 Stop.
Final heap:
[5, 9, 14, 10]

Tree:
       5
       / \
      9  14
     /
   10


The Core Logic (must say in interview)
Deletion always follows three rules:
Remove root


Move last element to root


Bubble down (swap with smaller child)


This ensures:
O(log n)


Critical Interview Trap (very common)
Many candidates swap with any child instead of the smaller child (min-heap) or larger child (max-heap).
Correct rule:
Heap Type
Swap With
Min heap
smaller child
Max heap
larger child


Mental Model (important for solving problems)
Insertion fixes violations bottom → up
 Deletion fixes violations top → down
Understanding this allows you to reason about:
Top-K problems


Streaming heaps


Median heaps


Priority scheduling problems

"""