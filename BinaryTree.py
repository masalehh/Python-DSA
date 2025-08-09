#implement binary tree, preorder, postorder and inorder traversal 

from typing import Optional

class BinaryTreeNode:
    def __init__(self, value) -> None:
        self.value = value 
        self.left: Optional['BinaryTreeNode'] = None
        self.right: Optional['BinaryTreeNode'] = None
        
    
    def preorder(self):
        """Root -> Left -> Right"""
        print(self.value, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
            
        
    def inorder(self):
        """Left -> Root -> Right"""
        if self.left:
            self.left.inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.inorder()
        
    
    def postorder(self):
        """Left -> Right -> Root"""
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value, end=" ") 
        
        

# Example usage
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

root.preorder()  # 1 2 4 5 3
print()
root.postorder() # 4 5 2 3 1 
print()  
root.inorder()   # 4 2 5 1 3 

              