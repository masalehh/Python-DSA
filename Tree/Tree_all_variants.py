
"""
trees.py
========
Collection of Tree Data Structure implementations in Python.

Includes:
1. Generic Tree
2. Binary Tree
3. Binary Search Tree (BST)
4. AVL Tree (Self-Balancing BST)
5. N-ary Tree
6. Trie (Prefix Tree)

Author: Abdullah Saleh + ChatGPT
"""

# ------------------------------
# 1. Generic Tree
# ------------------------------

class TreeNode:
    """Generic Tree Node: Can have any number of children."""
    def __init__(self, value) -> None:
        self.value = value 
        self.children = [] 
        
        
    def add_child(self, child_node):
        """Adds a child node."""
        self.children.append(child_node)
        
        
    def display(self, level=0):
        """Recursively prints tree structure."""
        print(" " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)
            
            
    
# ------------------------------
# 2. Binary Tree
# ------------------------------        
class BinaryTree:
    """Binary Tree Node: Max two children (left, right)."""
    def __init__(self, value) -> None:
        self.value = value 
        self.right = None 
        self.left = None 
        
    
    def preorder(self):
        """Preorder Traversal: Root -> Left -> Right"""
        print(self.value, end=" ")
        if self.left:
            self.left.preorder() 
        if self.right:
            self.right.preorder() 
            
    
    def inorder(self):
        """Inorder Traversal: Left -> Root -> Right"""
        if self.left:
            self.left.inorder() 
        print(self.value, end=" ")
        if self.right:
            self.right.inorder() 
            
    
    def postorder(self):
        """Postorder Traversal: Left -> Right -> Root"""
        if self.left:
            self.left.postorder() 
        if self.right:
            self.right.postorder() 
        print(self.value, end=" ")



# ------------------------------
# 3. Binary Search Tree
# ------------------------------
class BST:
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
                self.left = BST(value) 
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value) 
        
        
    def search(self, value):
        """Searches for a value in BST."""
        if value == self.value:
            return True 
        elif value < self.value and self.left:
            return self.left.search(value) 
        elif value > self.value and self.right:
            return self.right.search(value)
        return False 
    

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
        
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right)) 
        
        balance = self.get_balance(root)
        
        
        # Balance Cases 
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
    
    
    
# ------------------------------
# 5. N-ary Tree
# ------------------------------
class NaryNode:
    """N-ary Tree Node: Fixed number of children."""
    def __init__(self, value, n) -> None:
        self.value = value 
        self.children = [None] * n 
        
    
    def add_child(self, index, child_node):
        """Adds child at a specific index."""
        if 0 <= index < len(self.children):
            self.children[index] = child_node 
        
        
        
# ------------------------------
# 6. Trie
# ------------------------------
class TrieNode:
    """Node in a Trie (Prefix Tree)."""
    def __init__(self) -> None:
        self.children = {} 
        self.is_end_of_word = False 
        
        

class Trie:
    """Trie implementation for prefix-based search."""
    def __init__(self):
        self.root = TrieNode()
        
    
    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode() 
            node = node.children[char]
        node.is_end_of_word = True 
        
        
    def search(self, word):
        """Search for a full word in the trie."""
        node = self.root 
        for char in word:
            if char not in node.children:
                return False 
            node = node.children[char]
        return node.is_end_of_word 
            


# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":
    """ print("\n--- Generic Tree ---")
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(TreeNode("Grandchild 1"))
    root.display()

    print("\n--- Binary Tree ---")
    b_root = BinaryTree(1)
    b_root.left = BinaryTree(2)
    b_root.right = BinaryTree(3)
    #b_root.preorder()
    #b_root.postorder() 
    b_root.inorder() 

    print("\n\n--- BST ---")
    bst_root = BST(10)
    for val in [5, 15, 2, 7]:
        bst_root.insert(val)
    print(bst_root.search(70))  # True 

    print("\n--- AVL Tree ---")
    avl = AVLTree()
    avl_root = None
    for val in [10, 20, 30, 40, 50, 25]:
        avl_root = avl.insert(avl_root, val)
    print("AVL root:", avl_root.value)

    print("\n--- N-ary Tree ---")
    n_root = NaryNode("NRoot", 3)
    n_root.add_child(0, NaryNode("C1", 3))
    n_root.add_child(1, NaryNode("C2", 3))
    print(n_root.children[1].value)
    """
    
    print("\n--- Trie ---")
    trie = Trie()
    trie.insert("cat")
    trie.insert("car")
    print(trie.search("cat"))  # True
    print(trie.search("can"))  # False