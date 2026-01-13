def postorder_iterative(root):
    if not root:
        return [] 
    
    stack = [root]
    result = [] 
    
    while stack:
        node = stack.pop() 
        result.append(node.value) 
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
            
    return result[::-1]

        
"""
        1
       / \
      2   3
     / \
    4   5

[4, 5, 2, 3, 1]
Big Idea Behind This Code 💡

This code actually does:
Root → Right → Left   (a modified preorder)
Then it reverses the result to get:
Left → Right → Root   (postorder)

"""