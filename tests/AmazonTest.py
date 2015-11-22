import unittest

from graphBuilder import importGraph


class TestImportGraph(unittest.TestCase):

    def test_import_graph(self):
        graph = importGraph("test-ungraph.txt")
        self.assertEquals(graph.number_of_nodes(), 4)
        self.assertEquals(graph.number_of_edges(), 5)


if __name__ == '__main__':
    unittest.main()
