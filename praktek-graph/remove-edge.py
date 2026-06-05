class Graph:
    def __init__(self):
        self.graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            self.graph[vertex2].remove(vertex1)

    def print_graph(self):
        print(self.graph)


# Contoh penggunaan
graph = Graph()
print("Graph sebelum menghapus edge:")
graph.print_graph()
graph.remove_edge("A", "B")
print("Graph setelah menghapus edge antara A dan B:")
graph.print_graph()
