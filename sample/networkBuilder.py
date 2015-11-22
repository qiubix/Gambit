import networkx as nx
import matplotlib.pyplot as plot


def make_graph1():
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    G.add_edge(1, 2)
    e = (2, 3)
    G.add_edge(*e)
    G.add_edges_from([(3, 4), (3, 5)])
    return G


# G = make_graph1()
# print G.number_of_nodes()
# print G.number_of_edges()
# nx.draw(G)

# plot.show()
