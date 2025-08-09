# Binary Search Tree 

class BSTNode:
    """Binary Search Tree Node: Left < Root < Right."""
    def __init__(self, value) -> None:
        self.value = value 
        self.left = None 
        self.right = None 
        
    def insert(self, value):
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
                
    
    def search_BST(self, value):
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
    


    