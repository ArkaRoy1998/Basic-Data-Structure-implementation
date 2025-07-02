# Basic-Data-Structure-implementation

The Graph_Data_structure.py provides a simple Python implementation of an **undirected, unweighted graph** using an **adjacency list**. It includes methods for basic graph operations, traversal, and connected component analysis.

## Features

- Add/remove vertices and edges
- Check existence of vertices/edges
- Get neighbors of a vertex
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Count connected components

## Example

```python
g = Undirected_Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")

print(g.BFS("A"))  # ['A', 'B']
print(g.DFS("A"))  # ['A', 'B']
print(g.connected_component())  # 1

