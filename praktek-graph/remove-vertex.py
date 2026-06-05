class Graph:
    def __init__(self):
        self.graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            # Hapus vertex dari daftar tetangga
            for neighbor in self.graph[vertex]:
                self.graph[neighbor].remove(vertex)
            # Hapus vertex dari graph
            del self.graph[vertex]

    def print_graph(self):
        print(self.graph)


# Contoh penggunaan
graph = Graph()
print("Graph sebelum menghapus vertex:")
graph.print_graph()
graph.remove_vertex("C")
print("Graph setelah menghapus vertex C:")
graph.print_graph()
