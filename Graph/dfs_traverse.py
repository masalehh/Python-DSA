from typing import  List, Dict, TypeVar, Set 

T = TypeVar('T')

def dfs_traverse(start: T, graph: Dict[T, List[T]]) -> None: 
    visited: Set[T] = set() 
    
    def dfs_helper(node: T) -> None:
        visited.add(node)
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)
    dfs_helper(start)  