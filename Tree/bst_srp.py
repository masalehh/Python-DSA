from typing import Optional 

class BSTNode: 
    def __init__(self, value: int) -> None:
        self.value = value 
        self.left: Optional[BSTNode] = None 
        self.right: Optional[BSTNode] = None 
        

class BST: 
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None 
        
        
    def insert(self, value: int):
        if self.root is None: 
            self.root = BSTNode(value)
            return 
        self._insert(self.root, value) 
        
        
    def _insert(self, node: BSTNode, value: int) -> None: 
        if value < node.value: 
            if node.left: 
                self._insert(node.left, value)
            else: 
                node.left = BSTNode(value) 
                
        elif value > node.value: 
            if node.right: 
                self._insert(node.right, value)
            else: 
                node.right = BSTNode(value) 
                
                
    def search(self, value: int) -> bool: 
        return self._search(self.root, value)
    
    
    def _search(self, node: Optional[BSTNode], value: int) -> bool:
        if node is None: 
            return False 
        
        if value == node.value: 
            return True 
        
        if value < node.value: 
            return self._search(node.left, value)
        
        return self._search(node.right, value)
        
        
tree = BST()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

print(tree.search(7))   # True
print(tree.search(20))  # False
        