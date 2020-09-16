import networkx as nx

G = nx.path_graph(3)
H = nx.path_graph(4)

# The composition of G and H is the simple union G U H that allows
# G and H to share nodes
# See Union.py for restrictions of the union method
compose = nx.compose(G, H)

# Note that the compose method makes it easy to combine graphs but
# difficult to reverse the result. So it may not be a better
# choice than the union method in some cases
print(f"G nodes: {list(G.nodes)}", f"| G edges: {list(G.edges)}")
print(f"H nodes: {list(H.nodes)}", f"| H edges: {list(H.edges)}")
print(f"G U H nodes: {list(compose.nodes)}",
      f"| G U H edges: {list(compose.edges)}")
