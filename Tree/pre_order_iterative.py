class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
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
        
        if node.right:
            stack.append(node.right)
            
        if node.left:
            stack.append(node.left)
    return result 