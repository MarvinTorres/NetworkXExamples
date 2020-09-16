import networkx as nx

G = nx.Graph()
H = nx.Graph()

# Both graphs must have the same nodes for the difference method to work
G.add_nodes_from([1, 2, 3, 4])
H.add_nodes_from(G)

# Give G and H the same edges, then add an extra edge to G
G.add_edges_from([(1, 2), (2, 3), (3, 4)])
H.add_edges_from(G.edges)
G.add_edge(1, 4)

# The difference G-H is G without the edges in H
difference = nx.difference(G, H)

# Notice that the only edge is the extra one added earlier
print(f"G nodes: {list(G.nodes)}", f"| G edges: {list(G.edges)}")
print(f"H nodes: {list(H.nodes)}", f"| H edges: {list(H.edges)}")
print(f"G-H nodes: {list(difference.nodes)}",
      f"| G-H edges: {list(difference.edges)}")
