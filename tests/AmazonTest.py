import unittest

from Amazon import AmazonGraphAnalyzer


# + import graph - check number of nodes and edges
# + count connected components
# TODO: get biggest connected component (cound no of nodes and edges)
# TODO: get mean assortativity
# TODO: get Pearson assortativity

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
        self.assertEquals(len(largest_cc), 4)


if __name__ == '__main__':
    unittest.main()
