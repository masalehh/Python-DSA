def max_depth(root):
    if not root:
        return 0 
    
    left = max_depth(root.left)
    right = max_depth(root.right)
    
    return 1 + max(left, right)


"""
        1 (returns 3)
       / \
      2   3
   (2)   (1)
     /
    4
   (1)
   
   
max_depth(1)
│
├── max_depth(2)
│   │
│   ├── max_depth(4)
│   │   ├── max_depth(None) → 0
│   │   └── max_depth(None) → 0
│   │
│   └── returns 1
│
│   ├── max_depth(None) → 0
│   └── returns 2
│
├── max_depth(3)
│   ├── max_depth(None) → 0
│   └── max_depth(None) → 0
│
└── returns 1

returns 3


Complexity

Time: O(n)

Space: O(h)
"""