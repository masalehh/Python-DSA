class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left 
        self.right = right 
        

def preorder_traversal(root):
    result = [] 
    
    def dfs(node):
        if not node:
            return 
        result.append(node.value)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result 