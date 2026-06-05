class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
        if vertex2 not in self.graph:
            self.graph[vertex2] = []
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def print_graph(self):
        print(self.graph)


# Contoh penggunaan
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.print_graph()
