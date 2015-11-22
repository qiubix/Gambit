import networkx as nx


class AmazonGraphAnalyzer:

    def __init__(self):
        self.amazonGraph = nx.Graph()

    def importGraph(self, inputFileName):
        fileName = open(inputFileName, 'rb')
        amazonGraph = nx.read_edgelist(fileName)
        self.amazonGraph = amazonGraph
        return amazonGraph

    def getNumberOfNodes(self):
        return self.amazonGraph.number_of_nodes()

    def getNumberOfEdges(self):
        return self.amazonGraph.number_of_edges()

    def getNumberOfConnectedComponents(self):
        return nx.number_connected_components(self.amazonGraph)

    def getLargestConnectedComponent(self):
        return max(nx.connected_component_subgraphs(self.amazonGraph), key=len)

    def calculatePearsonCorrelationCoefficient(self):
        return nx.degree_pearson_correlation_coefficient(self.amazonGraph)

    def calculateDegreeAssortativityCoefficient(self):
        return nx.degree_assortativity_coefficient(self.amazonGraph)

    def exportToPajek(self):
        nx.write_pajek(self.amazonGraph, 'amazon-graph.net')

if __name__ == '__main__':
    analyzer = AmazonGraphAnalyzer()
    amazonGraph = analyzer.importGraph("com-amazon.ungraph.txt")
    print "Amazon product co-purchasing network"
    print nx.info(amazonGraph)
    print "Amazon graph has:", analyzer.getNumberOfNodes(), "nodes"
    print "Amazon graph has:", analyzer.getNumberOfEdges(), "edges"
    print "Number of connected components: ", analyzer.getNumberOfConnectedComponents()
    print "Largest CC size: ", len(analyzer.getLargestConnectedComponent())
    print "Pearson coefficient:", analyzer.calculatePearsonCorrelationCoefficient()
