from collections import deque 
from typing import Dict, List, Set 

def bfs(graph: Dict[int, List[int]], start: int) -> Set[int]:
    visited: Set[int] = {start} 
    queue = deque([start]) 
    
    
    while queue:
        node = queue.popleft() 
        print(node) 
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) 
                
                
    return visited 


"""
Time: O(V + E)
Space: O(V)


Interview Questions You Should Be Able to Answer
Why does BFS use a queue?
Why do we need a visited set?
Why mark a node visited before enqueueing?
How do we traverse a disconnected graph?
Why does BFS find the shortest path in an unweighted graph?
What is the time complexity?
"""
