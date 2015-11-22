import unittest

from sample.networkBuilder import make_graph1


class TestMakeGraph1(unittest.TestCase):

    def test_make_graph1(self):
        G = make_graph1()
        self.assertEquals(G.number_of_nodes(), 13)
        self.assertEquals(G.number_of_edges(), 4)

if __name__ == '__main__':
    unittest.main()
