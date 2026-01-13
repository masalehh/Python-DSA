def inordertraversal(root):
    result = [] 
    
    def inorder(node):
        if not node:
            return 
        inorder(node.left) 
        result.append(node.value)
        inorder(node.right)
        
    inorder(root)
    return result


"""
        1
       / \
      2   3
     / \
    4   5
[4, 2, 5, 1, 3]


"""