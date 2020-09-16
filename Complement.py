import networkx as nx

G = nx.Graph()

G.add_nodes_from([1, 2, 3])

G.add_edges_from([(1, 2), (2, 3)])

# The complement G' is G with all edges not in G
complement = nx.complement(G)

# Notice that the edges added earlier are missing from G'
print(f"G nodes: {list(G.nodes)}", f"| G edges: {list(G.edges)}")
print(f"G' nodes: {list(complement.nodes)}",
      f"| G' edges: {list(complement.edges)}")
