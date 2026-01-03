from typing import List, Dict, Set, TypeVar

T = TypeVar('T')

def has_path(graph: Dict[T, List[T]], src: T, dst: T) -> bool:
    visited: Set[T] = set() 
    
    def dfs(node: T) -> bool:
        if node == dst:
            return True 
        
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True 
        return False 
    
    return dfs(src)
    