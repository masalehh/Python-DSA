def dfs_has_cycle(graph):
    visited = set() 
    
    def dfs(node, parent):
        visited.add(node) 
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True 
            elif neighbor != parent:
                return True 
        return False 
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True 
    return False 



"""graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}


A —— B
|    |
D —— C


     E
   /  \
  P    Q
  /\   / \
  R T--U  S 
  
        E
      /   \
     P     Q
    / \     /\
   R   T — U  S
   
   graph = {
    'E': ['P', 'Q'],
    'P': ['E', 'R', 'T'],
    'R': ['P'],
    'T': ['P', 'U'],
    'U': ['T', 'Q'],
    'Q': ['E', 'U', 'S'],
    'S': ['Q']
}


   Dry Run: 
   | Step | Node  | Parent | Action                                 | Visited            |
| ---- | ----- | ------ | -------------------------------------- | ------------------ |
| 1    | E     | None   | visit E                                | {E}                |
| 2    | P     | E      | visit P                                | {E, P}             |
| 3    | R     | P      | visit R                                | {E, P, R}          |
| 4    | R     | P      | only neighbor is parent → return False | {E, P, R}          |
| 5    | T     | P      | visit T                                | {E, P, R, T}       |
| 6    | U     | T      | visit U                                | {E, P, R, T, U}    |
| 7    | Q     | U      | visit Q                                | {E, P, R, T, U, Q} |
| 8    | Q → E | U      | **E visited & not parent → CYCLE**     | {E, P, R, T, U, Q} |


dfs(E, None)
└── dfs(P, E)
    └── dfs(T, P)
        └── dfs(U, T)
            └── dfs(Q, U)
            

Interview one-liner 🧠

“During DFS, if I encounter a visited neighbor that is not my parent, I have found a cycle in an undirected graph.”
   """
