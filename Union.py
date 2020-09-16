import networkx as nx

G = nx.Graph()
H = nx.Graph()

# Notice that add_edges_from(...) makes the nodes needed to create the edges
# Also, both graphs must be disjoint (not have nodes in common) for the
# union method to work
G.add_edges_from([(1, 2), (3, 4), (4, 5)])
H.add_edges_from([(6, 7), (7, 8)])

# The union G U H is a graph that has the edges of both G and H
union = nx.union(G, H)

# Notice the graph has G and H's nodes and edges
print(f"G nodes: {list(G.nodes)}", f"| G edges: {list(G.edges)}")
print(f"H nodes: {list(H.nodes)}", f"| H edges: {list(H.edges)}")
print(f"G U H nodes: {list(union.nodes)}",
      f"| G U H edges: {list(union.edges)}")
