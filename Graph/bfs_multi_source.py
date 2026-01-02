from collections import deque 

def dfs_multi_source(starts, graph):
    visited = set(starts)
    queue = deque(starts)
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)