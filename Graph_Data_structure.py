# We implement Graph as an adjacency list:
# The adjacency list is represented as a dictionary
class Undirected_Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self,v):
            if v in self.adjacency_list:
                raise ValueError(f"Vertex '{v}' already exists.")
            self.adjacency_list[v] = []

    def add_edge(self, v, w):
        if v in self.adjacency_list and w in self.adjacency_list:
            if w not in self.adjacency_list[v] and v not in self.adjacency_list[w]:
                self.adjacency_list[v].append(w)
                self.adjacency_list[w].append(v)
            else:
                raise ValueError(f"Edge '{v}-{w}' already exists.")
        else:
            raise ValueError(f"One or both vertices '{v}' and '{w}' do not exist.")

    def remove_vertex(self,u): # first remove u from every list where it existed as a vertex and then remove key value pair for u
        if u in self.adjacency_list:
            del self.adjacency_list[u]
        else:
            raise ValueError (f"Vertex {u} does not exist.")

        for key in self.adjacency_list:
            if u in self.adjacency_list[key]:
                self.adjacency_list[key].remove(u)

    def has_vertex(self, v):
        return v in self.adjacency_list

    def has_edge(self, u, v):
        return u in self.adjacency_list and v in self.adjacency_list[u]

    def neighbours(self,v):
        return self.adjacency_list[v]


    def BFS(self,start):

        queue = []
        visited = set()
        visited.add(start)
        queue.append(start)
        result = []  # To store the actual traversal order
        while queue:
            current = queue.pop(0)
            result.append(current)
            for vertex in self.adjacency_list[current]:
                if vertex not in visited and vertex not in queue:
                    queue.append(vertex)
                    visited.add(vertex)

        return result

    def DFS(self, start):
        stack = []
        visited = set()
        result = []

        stack.append(start)

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                result.append(current)

                # Push neighbors onto stack (optional: reversed for consistent order)
                for vertex in reversed(self.adjacency_list[current]):
                    if vertex not in visited:
                        stack.append(vertex)

        return result

    def _bfs_mark_connected(self, start, visited):
        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop(0)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    def connected_components(self):
            visited = set()
            count = 0

            for vertex in self.adjacency_list:
                if vertex not in visited:
                    self._bfs_mark_connected(vertex, visited)
                    count += 1

            return count





