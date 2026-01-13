"""
Docstring for Python-DSA.Tree.level_order_traversals
When to use?

Level by level

Distance

Minimum depth

"""

from collections import deque 

def level_order(root):
    if not root:
        return [] 
    
    queue = deque([root]) 
    result = [] 
    
    while queue:
        level = [] 
        for _ in range(len(queue)):
            node = queue.popleft() 
            level.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 
                
        result.append(level)
        
    return result 

"""
“BFS processes nodes level by level using a queue.”

For all traversals:

Time: O(n) — every node visited once

Space:

DFS recursion → O(h) (tree height)

BFS queue → O(w) (max width)
"""

"""
Interview Traps (Pay Attention)

❌ Writing code without stating traversal choice
❌ Using global variables unnecessarily
❌ Forgetting base case
❌ Confusing inorder usefulness for non-BST

Any one of these = rejection risk.
"""

"""
        1
       / \
      2   3
     / \
    4   5
[
  [1],
  [2, 3],
  [4, 5]
]

example: 2 

            1
           / \
          2   3
         / \ / \
        4  5 6  7

[
  [1],
  [2, 3],
  [4, 5, 6, 7]
]

"""