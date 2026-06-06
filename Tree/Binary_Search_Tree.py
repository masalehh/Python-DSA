# Binary Search Tree 
from typing import Optional 


class BSTNode:
    """Binary Search Tree Node: Left < Root < Right."""
    def __init__(self, value: int) -> None:
        self.value = value 
        self.left: Optional[BSTNode] = None 
        self.right: Optional[BSTNode] = None 
        
    def insert(self, value: int):
        """Inserts a value into the BST."""
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
                
    
    def search_BST(self, value: int) -> bool:
        """Searches for a value in BST."""
        if value == self.value:
            return True 
        elif value < self.value and self.left:
            return self.left.search_BST(value)
        elif value > self.value and self.right:
            return self.right.search_BST(value)
        
        return False 
        
        


# Example usage
root = BSTNode(10)
root.insert(5)
root.insert(25)
root.insert(32)
root.insert(7)

print(root.search_BST(7))  # True
print(root.search_BST(20)) # False 
    

"""
For insert():

Time Complexity

At each step, you compare the value and move either left or right.

Best case: O(1)
If the tree has only one node and you insert directly.
Average case (balanced BST): O(log n)
Height of a balanced BST is about log n.
Worst case (skewed BST): O(n)
If nodes are inserted in sorted order:

1
 \
  2
   \
    3
     \
      4
    Height becomes n, so you may traverse all nodes.
    
    Space Complexity

This implementation is recursive, so the call stack uses space proportional to the tree height.

Average case: O(log n)
Worst case: O(n)

For:
search_BST()
Time Complexity

Again, you move down only one path (left or right).

Best case: O(1)
Value is at the root.
Average case (balanced BST): O(log n)
Worst case (skewed BST): O(n)
Space Complexity

Recursive calls consume stack space equal to the tree height.

Average case: O(log n)
Worst case: O(n)

General Rule

For both operations:

Tree Type	    Height (h)	Time Complexity	    Space Complexity
Balanced BST	O(log n)	O(log n)	        O(log n)
Skewed BST	    O(n)	    O(n)	            O(n)

"""

    