from collections import deque
from typing import Hashable


def bfs_target(
        start: Hashable,
        target: Hashable,
        graph: dict[Hashable,
        list[Hashable]]
) -> int:
    """
        Find the shortest distance from start to target using BFS.

        Args:
            start: Starting node.
            target: Node we want to reach.
            graph: Adjacency list representation of the graph.

        Returns:
            Number of edges in the shortest path from start to target.
            Returns -1 if the target is unreachable.
        """


    visited: set[Hashable] = {start}

    queue: deque[tuple[Hashable, int]] = deque([(start, 0)])
    
    while queue:
        # Get the next node to process
        node, distance = queue.popleft()

        # Target found
        if node == target:
            return distance

        # Explore all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                # Neighbor is one edge farther away
                queue.append((neighbor, distance + 1))

    # Target was never reached
    return -1 
    