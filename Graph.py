import networkx as nx


def create_graph_with_weights():
    '''Create a graph with preset edge weights.'''
    edges = [('A', 'B', 0.2), ('A', 'C', 2.0), ('C', 'D', 1.3)]
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return G


def create_graph_with_metadata():
    '''Create a graph with preset edge metadata.'''
    edges = [('A', 'B', {'bandwidth': 25, 'delay': 20, 'ownership': 'A'}),
             ('A', 'C', {'bandwidth': 20, 'delay': 25, 'ownership': 'B'}),
             ('C', 'D', {'bandwidth': 15, 'delay': 10, 'ownership': 'A'})]
    G = nx.Graph()
    G.add_edges_from(edges)
    return G
