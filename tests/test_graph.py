import os
import sys
import unittest

from make_graphs import *

path = os.getcwd().split("/")

new_path = ""
for i in xrange(1, len(path) - 1):
    new_path += "/" + path[i]

sys.path.append(new_path)

from gne import Graph, Node, Edge


class GraphTest(unittest.TestCase):

    def test_addEdge_rule1(self):
        self.assertRaises(ValueError, rule1Violation1)





if __name__ == "__main__":
    unittest.main()