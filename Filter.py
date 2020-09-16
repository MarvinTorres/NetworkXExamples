from Graph import create_graph_with_metadata, nx

G = create_graph_with_metadata()


def bandwidth_filter(x):
    u, v, d = x
    return d['bandwidth'] >= 20


def delay_filter(x):
    u, v, d = x
    return d['delay'] <= 20


def ownership_filter(x):
    u, v, d = x
    return d['ownership'] == 'B'


# The second argument is a generator. It yields a tuple from the
# expression "for ... in ..." until no more values can be yielded.
# This expression is evaluated only on demand i.e. when the next value is requested.
# This lazy evaluation saves a ton of memory since not all the values
# have to be known at the same time.
#
# For more information on generators, visit https://wiki.python.org/moin/Generators
filtered = filter(bandwidth_filter, ((u, v, d) for u, v, d in G.edges.data()))

print("G edges and metadata:")
for edge in G.edges.data():
    print(edge)

print("Edges that meet bandwidth requirements:")
for edge in filtered:
    print(edge)

filtered = filter(delay_filter, ((u, v, d)
                                 for u, v, d in G.edges.data()))

print("Edges that meet delay requirements:")
for edge in filtered:
    print(edge)

filtered = filter(ownership_filter, ((u, v, d)
                                     for u, v, d in G.edges.data()))

print("Edges that meet ownership requirements:")
for edge in filtered:
    print(edge)

filtered = filter(bandwidth_filter, ((u, v, d)
                                     for u, v, d in G.edges.data()))

filtered = filter(ownership_filter, filtered)

print("Edges that meet both bandwidth and ownership requirements:")
for edge in filtered:
    print(edge)
