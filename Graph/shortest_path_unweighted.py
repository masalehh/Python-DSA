from collections import deque 

def bfs_shortest_path(start, graph):
    visited = set([start])
    distance = {start: 0} 
    queue = deque([start]) 
    
    while queue: 
        node = queue.popleft() 
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1 
                queue.append(neighbor)
    return distance 
                