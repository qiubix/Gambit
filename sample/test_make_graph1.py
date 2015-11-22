from unittest import TestCase

from sample.networkBuilder import make_graph1


class TestMakeGraph1(TestCase):

    def test_make_graph1(self):
        G = make_graph1()
        self.assertEquals(G.number_of_nodes(), 13)
        self.assertEquals(G.number_of_edges(), 4)
