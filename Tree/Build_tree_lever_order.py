from collections import deque 


class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right 
        
        
def build_tree(values):
    if not values or values[0] is None:
        return None 
    
    root = TreeNode(values[0]) 
    queue = deque([root]) 
    i = 1 
    
    while queue and i < len(values):
        node = queue.popleft() 
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i]) 
            queue.append(node.left) 
        i += 1 
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right) 
        i += 1 
        
        
    return root 
         
            
"""
You are given below list to build a tree: 
[1, 2, 3, None, 4, 5, 6]
output tree will looks like: 
        1
       / \
      2   3
       \  / \
        4 5  6
        
        
🔹 Main Loop (Important Part)
while queue and i < len(values):


✔ Continue while:

There are nodes waiting to get children

We still have values to process

🔹 One-Line Summary (Interview Ready)

This function constructs a binary tree from a level-order array using BFS, where None represents missing nodes.

"""