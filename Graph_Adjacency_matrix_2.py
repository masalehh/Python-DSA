class AdjacencyMatrix:
    def __init__(self, directed=False) -> None:
        self.vertics = [] 
        self.index = {}
        self.matrix = []
        self.directed = directed 
        
    def _add_vertix(self, v):
        if v not in self.index:
            self.index[v] = len(self.vertics)
            self.vertics.append(v) 
            
            for row in self.matrix:
                row.append(0) 
                
            self.matrix.append([0] * len(self.vertics))
            
    def add_edge(self, u, v, weight=1):
        self._add_vertix(u)
        self._add_vertix(v)
        
        i, j = self.index[u], self.index[v]
        self.matrix[i][j] = weight
        if not self.directed:
            self.matrix[j][i] = weight 
            
            
    def display(self):
        print("\nAdjacency Matrix:")
        print("   ", *self.vertics)
        for i, row in enumerate(self.matrix):
            print(f"{self.vertics[i]} ", row) 
            

graph_type = input("Directed graph? (y/n): ").lower()
directed = graph_type == 'y'
graph = AdjacencyMatrix(directed=directed)

while True:
    edge = input("Enter edge (A to B) or 'q' for quit: ").strip() 
    if edge.lower() == 'q':
        break 
    try:
        u, v = edge.split(" to ")
        graph.add_edge(u.strip(), v.strip())
    except ValueError:
        print("Invalid format, use: A to B")
        
        
graph.display() 