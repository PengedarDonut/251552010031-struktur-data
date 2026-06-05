class Graph:
    def __init__(self):
        self.graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                queue.extend(self.graph[vertex])


# Contoh penggunaan
graph = Graph()
print("Traversal BFS dimulai dari vertex A:")
graph.bfs("A")
