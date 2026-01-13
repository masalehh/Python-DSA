def postorder_recursive(root):
    result = [] 
    
    def postorder(node):
        if not node:
            return 
        
        postorder(node.left)
        postorder(node.right)
        result.append(node.value)
    
    postorder(root)
    return result 

"""
“The parent depends on children results, so postorder is required.”
        1
       / \
      2   3
     / \
    4   5

[4, 5, 2, 3, 1]


"""