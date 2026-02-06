
class MinHeap:
    def __init__(self) -> None:
        self.heap = [] 
        
        def insert(self, value):
            self.heap.append(value) 
            self._heapify_up(len(self.heap) - 1) 
            
            
        def _heapify_up(self, i):
            while i > 0:
                parent = (i - 1) // 2 
                if self.heap[i] < self.heap[parent]:
                    self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                    i = parent 
                else:
                    break 
                
                
"""
“After insertion, the heap was already valid except possibly at the edge between the new node 
and its parent. If the immediate parent satisfies the heap property, then by transitivity 
all ancestors also satisfy it, so no further checks are required.”

Visual Representation of Insertion to a Heap
Let’s visualize step-by-step insertion using the exact logic of your code (append → heapify_up).
Assume we insert the numbers in this order:
10, 5, 14, 9, 2

I will show:
array representation (actual heap storage)


tree representation (virtual view)


swaps performed by _heapify_up



Step 1 — insert 10
Append:
[10]

Tree:
10

No parent → stop.

Step 2 — insert 5
Append:
[10, 5]

Tree:
  10
  /
 5

Heapify-up:
Compare 5 with parent 10


5 < 10 → swap


Result:
[5, 10]

Tree:
  5
  /
10


Step 3 — insert 14
Append:
[5, 10, 14]

Tree:
   5
   / \
 10  14

Heapify-up:
Compare 14 with parent 5


No swap → stop



Step 4 — insert 9
Append:
[5, 10, 14, 9]

Tree:
     5
     / \
   10  14
  /
 9

Heapify-up:
Compare 9 with parent 10


9 < 10 → swap


[5, 9, 14, 10]

Tree:
     5
     / \
    9  14
   /
 10

Now compare 9 with parent 5
 No swap → stop

Step 5 — insert 2
Append:
[5, 9, 14, 10, 2]

Tree:
       5
       / \
      9  14
     / \
   10   2

Heapify-up:
First compare
2 vs parent 9 → swap
[5, 2, 14, 10, 9]

Tree:
       5
       / \
      2  14
     / \
   10   9

Second compare
2 vs parent 5 → swap
[2, 5, 14, 10, 9]

Tree:
       2
       / \
      5  14
     / \
   10   9

Now at root → stop

Core Pattern You Must Internalize (Interview Key)
Insertion always follows two strict steps:
Insert at last position (maintains complete tree)


Bubble up until heap property holds


This guarantees:
height ≈ log n
→ insertion O(log n)


Extremely Important Interview Insight
Many candidates memorize code but fail when interviewer asks:
“Show me how the heap evolves after inserting each element.”
Being able to simulate the array and tree simultaneously signals strong DS mastery.

"""