from collections import deque 

def bfs_target(start, target, graph):
    visited = set([start])
    queue = deque([(start, 0)])
    
    while queue:
        node, distance = queue.popleft() 
        if node == target:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
                
    return -1 
    