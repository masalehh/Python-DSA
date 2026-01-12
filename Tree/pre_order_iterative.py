class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


def preorder_iterative(root):
    if not root:
        return [] 
    
    stack = [root]
    result = [] 
    
    while stack:
        node = stack.pop() 
        result.append(node.value)
        
        if node.right:                  # Right must be processed after left, thats why we pusdhed right to stack first 
            stack.append(node.right)
            
        if node.left:
            stack.append(node.left)     # left must be processed before right thats why we pushed it last as stack follows LIFO 
    return result 

"""
      1
     / \
    2   3
   / \
  4   5

"""