class Graph:
    def __init__(self):
        self.graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}

    def search_dfs(self, start_vertex, target_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        if start_vertex == target_vertex:
            return True
        for neighbor in self.graph.get(start_vertex, []):
            if neighbor not in visited:
                if self.search_dfs(neighbor, target_vertex, visited):
                    return True
        return False


# Contoh penggunaan
graph = Graph()
start_vertex = "A"
target_vertex = "C"
found = graph.search_dfs(start_vertex, target_vertex)
if found:
    print(f"Vertex {target_vertex} ditemukan dari vertex {start_vertex}.")
else:
    print(f"Vertex {target_vertex} tidak ditemukan dari vertex {start_vertex}.")
