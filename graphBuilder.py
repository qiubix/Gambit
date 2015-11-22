import os
import networkx as nx


def importGraph(inputFileName):
    # print os.curdir
    # print os.listdir(os.curdir)
    fileName = open(inputFileName, 'rb')
    graph = nx.read_edgelist(fileName)
    return graph

if __name__ == '__main__':
    graph = importGraph("com-amazon.ungraph.txt")
    print graph.number_of_nodes(), "nodes"
    print graph.number_of_edges(), "edges"
