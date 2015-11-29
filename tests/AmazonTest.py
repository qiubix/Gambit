import networkx as nx
import unittest

from Amazon import AmazonGraphAnalyzer


# + import graph - check number of nodes and edges
# + count connected components
# + get biggest connected component (cound no of nodes and edges)
# + get mean assortativity
# + get Pearson assortativity

class TestImportGraph(unittest.TestCase):

    def setUp(self):
        self.analyzer = AmazonGraphAnalyzer()
        self.analyzer.importGraph("test-ungraph.txt")

    def test_import_graph(self):
        self.assertEquals(self.analyzer.getNumberOfNodes(), 6)
        self.assertEquals(self.analyzer.getNumberOfEdges(), 7)

    def test_number_of_connected_components(self):
        self.assertEquals(self.analyzer.getNumberOfConnectedComponents(), 2)

    def test_get_largest_connected_component(self):
        largest_cc = self.analyzer.getLargestConnectedComponent()
        self.assertEquals(nx.number_of_nodes(largest_cc), 4)
        self.assertEquals(nx.number_of_edges(largest_cc), 6)

    def test_get_pearson_coefficient(self):
        coefficient = self.analyzer.calculatePearsonCorrelationCoefficient()
        self.assertEquals(coefficient, 1)

    def test_get_degree_assortativity_coefficient(self):
        coefficient = self.analyzer.calculateDegreeAssortativityCoefficient()
        self.assertEquals(coefficient, 0.999999999999998)

    def test_should_calculate_pearson_by_different_method(self):
        coefficient = self.analyzer.calculatePearson()
        self.assertEquals(coefficient, 1)

    # def test_get_list_of_first_degrees(self):
    #     node1 = self.analyzer.getAverageDegreeOfFirstNodeNeighbours()
    #     self.assertEquals(node1, 1)

if __name__ == '__main__':
    unittest.main()
