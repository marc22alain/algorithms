import os
import sys
import unittest

from make_graphs import *

path = os.getcwd().split("/")

new_path = ""
for i in xrange(1, len(path) - 1):
    new_path += "/" + path[i]

sys.path.append(new_path)

# from gne import Graph, Node, Edge
from floyd_warshall import FloydWarshall



class TestFloydWarshall(unittest.TestCase):

    def test_simple(self):
        graph = simpleDirectedWeightedNeg1()
        fw = FloydWarshall(graph)





if __name__ == "__main__":
    unittest.main()