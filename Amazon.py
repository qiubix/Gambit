import networkx as nx


class AmazonGraphAnalyzer:

    def __init__(self):
        self.amazonGraph = nx.Graph()

    def importGraph(self, inputFileName):
        fileName = open(inputFileName, 'rb')
        amazonGraph = nx.read_edgelist(fileName)
        self.amazonGraph = amazonGraph
        return amazonGraph

    def numberOfNodes(self):
        return self.amazonGraph.number_of_nodes()

    def numberOfEdges(self):
        return self.amazonGraph.number_of_edges()

if __name__ == '__main__':
    analyzer = AmazonGraphAnalyzer()
    amazonGraph = analyzer.importGraph("com-amazon.ungraph.txt")
    print amazonGraph.number_of_nodes(), "nodes"
    print amazonGraph.number_of_edges(), "edges"
