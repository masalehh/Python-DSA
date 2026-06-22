from typing import TypeVar

T = TypeVar("T")

def dfs(start: T, graph: dict[T, list[T]]) -> None:
    """
    Perform Depth First Search traversal starting from start node.

    Args:
        start: Starting node
        graph: Adjacency list representation of graph
    """
    visited: set[T] = set()
    
    def dfs_helper(node: T):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited: 
                dfs_helper(neighbor)
                
    dfs_helper(start) 
        
# Graph:
#
#        A
#       / \
#      B   C
#     / \   \
#    D   E   F
#
# DFS Traversal:
# A -> B -> D -> E -> C -> F

# graph = {
#     "A": ["B", "C"],
#     "B": ["D", "E"],
#     "C": ["F"],
#     "D": [],
#     "E": [],
#     "F": []


