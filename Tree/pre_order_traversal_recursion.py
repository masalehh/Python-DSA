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

"""
        1
       / \
      2   3
     / \
    4   5
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


"""