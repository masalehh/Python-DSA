from typing import Dict, List, Set, TypeVar

T = TypeVar('T')

def dfs_full(graph: Dict[T, List[T]]) -> None:
    visited: Set[T] = set() 
    
    def dfs(node: T) -> None:
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited: 
                dfs(neighbor)
                
    for node in graph:
        if node not in visited:
            dfs(node)
                