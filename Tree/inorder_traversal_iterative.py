class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value 
        self.left = left 
        self.right = right 


def inorder_traversal(root):
    stack = [] 
    result = [] 
    curr = root 
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left 
            """
            Remember this sentence:

            “Push nodes while going left. When you can’t go left, pop, visit, and go right.”
            """
        curr = stack.pop() 
        result.append(curr.val)
        curr = curr.right 
    return result 

"""
#in order traversal 
        1
       / \
      2   3
     / \
    4   5
    
    # inorder result 
    [4, 2, 5, 1, 3]

"""