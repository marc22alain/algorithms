import unittest

from dijkstra import Dijkstra

from make_graphs import *


class TestDijkstra(unittest.TestCase):

    def test_dijkstraChallenge1(self):
        args = dijkstraChallenge1()
        d = Dijkstra(args[0], args[1], args[2])
        d.doComplete()
        actual = d.printS()
        self.assertEquals(actual, args[3])























if __name__ == "__main__":
    unittest.main()