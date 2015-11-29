import networkx as nx
import time
import operator
import matplotlib.pyplot as plt
import math
from networkx.algorithms.centrality import betweenness



class AmazonGraphAnalyzer:
    def __init__(self):
        self.amazonGraph = nx.Graph()

    def importGraph(self, inputFileName):
        V = []
        i = 0
        fileName = open(inputFileName, 'rb')
        for line in fileName:
            i += 1
            if line.split()[0] != '#':
                v = (int(line.split()[0]), int(line.split()[1]))
                V.append(v)
            if i == 7302110:
                break

        amazonGraph = nx.Graph(V)

        #amazonGraph = nx.read_edgelist(fileName)
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

    def getAverageDegreeOfFirstNodeNeighbours(self):
        averageNeighbourDegrees = nx.average_degree_connectivity(self.amazonGraph)
        return averageNeighbourDegrees

    def drawData(self):
        averageNeighbourDegrees = self.getAverageDegreeOfFirstNodeNeighbours()
        plt.plot(averageNeighbourDegrees.keys(), averageNeighbourDegrees.values(), 'ro')
        plt.show()


def histogram(G):
    sorted_degree = sorted(G.degree().items(), key=operator.itemgetter(1))
    degree = []
    histo = []
    X = []
    maxdeg = 0
    for val in G.degree().values():
        if maxdeg < val:
            maxdeg = val
    for i in range(0, maxdeg + 1):
        histo.append(0)
        X.append(i)
    for key, val in sorted_degree:
        if val > 0:
            degree.append(val)
            histo[val] += 1
    plt.loglog(X, histo)
    suma = 0
    for i in degree:
        suma += math.log(2 * i)

    print 1 / suma * len(degree) + 1
    plt.show()


if __name__ == '__main__':
    analyzer = AmazonGraphAnalyzer()

    start = time.time()
    amazonGraph = analyzer.importGraph("com-amazon.ungraph.txt")
    print "import time:", time.time() - start

    print "Amazon product co-purchasing network"
    # histogram(amazonGraph)

    start = time.time()
    print nx.info(amazonGraph)
    # print "Graph degree: ", amazonGraph.degree()
    print "Amazon graph has:", analyzer.getNumberOfNodes(), "nodes"
    print "Amazon graph has:", analyzer.getNumberOfEdges(), "edges"
    print "time:", time.time() - start

    analyzer.drawData()

    print "BC: ", betweenness.betweenness_centrality(amazonGraph)

    start = time.time()
    print "Number of connected components: ", analyzer.getNumberOfConnectedComponents()
    print "time:", time.time() - start

    start = time.time()
    print "Largest CC size: ", len(analyzer.getLargestConnectedComponent())
    print "time:", time.time() - start

    start = time.time()
    print "Pearson coefficient:", analyzer.calculatePearsonCorrelationCoefficient()
    print "time:", time.time() - start

    start = time.time()
    print "Degree assortativity coefficient", analyzer.calculateDegreeAssortativityCoefficient()
    print "time:", time.time() - start
