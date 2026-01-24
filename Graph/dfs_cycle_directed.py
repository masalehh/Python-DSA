def has_cycle_directed(graph):
    visited = set() 
    path = set() 
    
    def dfs(node):
        visited.add(node)
        path.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True 
            elif neighbor in path:
                return True 
        path.remove(node)
        return False 
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True 
    return False 


"""
Graph with cycle 
{
  A: [B],
  B: [C],
  C: [A]
}

A → B → C → D        A : [B, C, D]
      ↑     |        B : [C, D]
      └─────┘        C : [D]
                     D : [B]

Graph with no cycle 
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': []
}

one brach has cycle and another branch not 
A → B → C
↓
D → E → D   (cycle)
graph = {
    'A': ['B', 'D'],
    'B': ['C'],
    'C': [],
    'D': ['E'],
    'E': ['D']
}

Interview-grade takeaway

“visited prevents reprocessing nodes, but path detects back-edges, which define cycles in directed graphs.”

Time & space complexity

Time: O(V + E)
Space: O(V)

===Edge Cases=== 
Interview answer

“Disconnected graphs are handled because we run DFS from every unvisited node.”

Interview answer

“A self-loop is a cycle by definition, and it’s detected because the node appears in the recursion stack.”
“A single node with no outgoing edges cannot form a cycle, so the algorithm correctly returns false.”
"""

