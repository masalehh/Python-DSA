class InvalidVertexError(Exception):
    pass


class AdjacencyMatrixGraph:
    def __init__(self, num_vertics, directed=False) -> None:
        if not isinstance(num_vertics, int) or num_vertics <= 0:
            raise ValueError("num_vertices must be a positive integer")
        
        self.num_vertices = num_vertics
        self.directed = directed 
        
        self.matrix = [
            [0 for _ in range(num_vertics)]
            for _ in range(num_vertics)
        ]
      
    def _set_edge(self, u: int, v: int, weight: int):
        self.matrix[u][v] = weight 
        if not self.directed:
            self.matrix[v][u] = weight 
            
            
    def add_edge(self, u, v, weight=1):
        self._validate_vertex(u)
        self._validate_vertex(v) 
        if weight == 0:
            raise ValueError("Weight cannot be 0 (rederved for no edge)")
        
        self.matrix[u][v] = weight 
        
        self._set_edge(u, v, weight)
      
            
    def remove_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        
        self._set_edge(u, v, 0)  
     
            
    def has_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        
        return self.matrix[u][v] != 0 
    
    
    def neighbors(self, u):
        self._validate_vertex(u)
        return [
            v for v in range(self.num_vertices)
            if self.matrix[u][v] != 0 
        ]
        
        
    def display(self):
        for row in self.matrix:
            print(row) 
            
    
    def adjacency_matrix(self):
        # Immutable, just return a copy
        return [row[:] for row in self.matrix] 
    
            
    def _validate_vertex(self, v):
        if not isinstance(v, int):
            raise InvalidVertexError("Vertex must be an integer")
        if v < 0 or v >= self.num_vertices:
            raise InvalidVertexError(
                                     f"Vertex {v} out of bounds [0, {self.num_vertices - 1}]"
                            ) 
            
            
graph = AdjacencyMatrixGraph(4, directed=False)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)

graph.display()

print(graph.has_edge(0, 1))     # True
print(graph.has_edge(1, 2))     # False 
print(graph.neighbors(0))       # [1, 2]