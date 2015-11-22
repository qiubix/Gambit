import unittest

from Amazon import AmazonGraphAnalyzer


# TODO: import graph - check number of nodes and edges
# TODO: count connected components
# TODO: get biggest connected component (cound no of nodes and edges)
# TODO: get mean assortativity
# TODO: get Pearson assortativity

class TestImportGraph(unittest.TestCase):

    def setUp(self):
        self.analyzer = AmazonGraphAnalyzer()
        self.analyzer.importGraph("test-ungraph.txt")

    def test_import_graph(self):
        self.assertEquals(self.analyzer.numberOfNodes(), 4)
        self.assertEquals(self.analyzer.numberOfEdges(), 5)


if __name__ == '__main__':
    unittest.main()
