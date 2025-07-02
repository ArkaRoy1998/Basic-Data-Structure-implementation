# Create graph instance
g = Undirected_Graph()

# Add vertices
for v in ["A", "B", "C", "D", "E", "F"]:
    g.add_vertex(v)

# Add edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("E", "F")  # Disconnected component

# Test has_vertex
assert g.has_vertex("A") is True
assert g.has_vertex("Z") is False

# Test has_edge
assert g.has_edge("A", "B") is True
assert g.has_edge("A", "D") is False

# Test neighbors
assert set(g.neighbours("A")) == {"B", "C"}

# Test BFS and DFS
bfs_result = g.BFS("A")
dfs_result = g.DFS("A")
assert set(bfs_result) == {"A", "B", "C", "D"}
assert set(dfs_result) == {"A", "B", "C", "D"}

# Test connected components
assert g.connected_components() == 2

# Remove a vertex and test again
g.remove_vertex("B")
assert g.has_vertex("B") is False
assert g.has_edge("A", "B") is False
assert g.connected_components() == 3

print("All test cases passed!")

