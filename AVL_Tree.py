class AVLNode:
    """AVL Tree Node: Stores height for balancing."""
    def __init__(self, value) -> None:
        self.value = value 
        self.left = None 
        self.right = None 
        self.height = 1 
        
        
class AVLTree:
    """AVL Tree implementation: Self-balancing BST."""
    def insert(self, root, key):
        """Insert key and balance."""
        if not root:
            return AVLNode(key)
        
        if key < root.value:
            root.left = self.insert(root.left, key)
        elif key > root.value:
            root.right = self.insert(root.right, key)
        else:
            return root 
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        balance = self.get_balance(root) 
        
        # Balance cases 
        if balance > 1 and key < root.left.value:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.value:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root 

    def left_rotate(self, z):
        y = z.right 
        T2 = y.left 
        y.left = z 
        z.right = T2 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y 
    
    def right_rotate(self, z):
        y = z.left 
        T3 = y.right 
        y.right = z 
        z.left = T3 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right)) 
        
        return y 
    
    def get_height(self, root):
        return root.height if root else 0 
    
    
    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right) if root else 0 
  
        
        
if __name__ == "__main__":
    print("\n--- AVL Tree ---")
    avl = AVLTree()
    avl_root = None
    for val in [10, 20, 30, 40, 50, 25]:
        avl_root = avl.insert(avl_root, val)
    print("AVL root:", avl_root.value)
                               
            