from collections import defaultdict
from typing import Dict, List, Tuple, Any


class Graph:
    """
        Graph representation using an adjacency list.

        Attributes:
            directed (bool): Whether the graph is directed.
            adj (defaultdict): Dictionary mapping each node to a list of (neighbor, weight) pairs.
    """
    def __init__(self, directed: bool = False) -> None:
        """
                    Initialize a new graph.

                    Args:
                        directed (bool): If True, creates a directed graph.
                                        If False, creates an undirected graph. Defaults to False.
                """
        self.directed = directed
        self.adj: Dict[Any, List[Tuple[Any, int]]] = defaultdict(list)

    def add_edge(self, u: Any, v: Any, weight: int = 1) -> None:
        """
        Add an edge to the graph.

        Args:
            u (Any): The starting node.
            v (Any): The ending node.
            weight (int): Edge weight. Defaults to 1.
        """
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))


    def nodes(self) -> List[Any]:
        """
        Get all nodes in the graph.

        Returns:
            List[Any]: A list of nodes.
        """
        node_set = set(self.adj.keys())
        for u in self.adj:
            for v, _ in self.adj[u]:
                node_set.add(v)
        return list(node_set)

    def __repr__(self) -> str:
        """
        Return a string representation of the graph.

        Returns:
            str: Graph type and number of vertices and edges.
        """
        edge_count = sum(len(neighbors) for neighbors in self.adj.values())
        kind = "Directed" if self.directed else "Undirected"
        return f"<Graph {kind}, |V|={len(self.nodes())}, |E|={edge_count}>"


if __name__ == "__main__":
    graph = Graph(directed=False)
    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 7)
    graph.add_edge("B", "D", 3)

    print(graph)        # <Graph Undirected, |V|=4, |E|=6>
    print(graph.adj)    # defaultdict(<class 'list'>, {'A': [('B', 5), ('C', 7)], 'B': [('A', 5), ('D', 3)], 'C': [('A', 7)], 'D': [('B', 3)]})
    print(graph.nodes())  # ['C', 'B', 'D', 'A']


