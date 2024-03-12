class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if v2 not in self.vertices[v1]:
                self.vertices[v1].append(v2)
            if v1 not in self.vertices[v2]:
                self.vertices[v2].append(v1)
        else:
            print("One or both vertices not found.")
    
    def display(self):
        for vertex, edges in self.vertices.items():
            print(vertex, ":", edges)

# Create an instance of the graph
my_graph = Graph()

# Add vertices
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

# Add edges
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'D')
my_graph.add_edge('D', 'A')

# Display the graph
my_graph.display()
