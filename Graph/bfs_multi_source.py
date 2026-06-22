from collections import deque
from typing import Hashable


def dfs_multi_source(
        starts: list[Hashable],
        graph: dict[Hashable, list[Hashable]]
) -> set[Hashable]:
    """
        Perform BFS starting from multiple source nodes.

        Args:
            starts: List of starting nodes, for considering disconnected graph.
            graph: Adjacency list representation of the graph.

        Returns:
            A set containing all reachable nodes.
        """

    # Mark all source nodes as visited initially
    visited = set(starts)

    # Put all source nodes into the queue
    queue = deque(starts)
    
    while queue:
        # Process the next node in BFS order
        node = queue.popleft()

        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # First time seeing this neighbor
                visited.add(neighbor)
                queue.append(neighbor)

    return visited