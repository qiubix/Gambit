import networkx as nx

import time


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
    print "time:", time.time() - start

    print "Amazon product co-purchasing network"

    start = time.time()
    print nx.info(amazonGraph)
    print "Amazon graph has:", analyzer.getNumberOfNodes(), "nodes"
    print "Amazon graph has:", analyzer.getNumberOfEdges(), "edges"
    print "time:", time.time() - start

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
