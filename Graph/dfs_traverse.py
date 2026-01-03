def dfs_traverse(start, graph):
    visited = set() 
    
    def dfs_helper(node):
        visited.add(node)
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)
    dfs_helper(start)  