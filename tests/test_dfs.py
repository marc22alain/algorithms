"""
There are a few properties of every valid DFS search that should be consistent.
	- every vertex is assigned a discovery time and a finish time
	- since every vertex is assigned two time values, the number of time value assignments is 2 times the number of vertices
	- since the time is incremented by one with every vertex discovery/finish, every such time should be unique and hence every
	  integer from 1 to 2n (n is the number of vertices) should be assigned to some vertex

This script tests the base implemention as well as the sub-classed implementation of DFS.
"""

#import os
#import sys
import unittest

import make_graphs as mg

#path = os.getcwd().split("/")
#print(path)
#
#new_path = ""
#for i in range(1, len(path) - 1):
#    new_path += "/" + path[i]
#print(new_path)
#
#sys.path.append(new_path)

from dfs import DFS
from graphmaker.dfs_draw import DFSdraw
from gne import Graph


class TestDFS(unittest.TestCase):

    def test_tree(self):
        dfs = DFS_class(mg.makeTree()["graph"])
        dfs.doComplete()
        self.assertEqual(True, dfs.hasTerminated())
        actual = totalTimes(dfs.graph)
        expected = sum(x for x in range((2 * len(dfs.graph.getNodes())) + 1))
        self.assertEqual(actual, expected)

    def test_triangles1(self):
        dfs = DFS_class(mg.makeTriangles1()["graph"])
        dfs.doComplete()
        self.assertEqual(True, dfs.hasTerminated())
        actual = totalTimes(dfs.graph)
        expected = sum(x for x in range((2 * len(dfs.graph.getNodes())) + 1))
        self.assertEqual(actual, expected)



def totalTimes(graph: Graph) -> int:
    # the use of a set() enforces the rule that every time value occurrence should be unique
    total = set()
    for n in list(graph.getNodes().values()):
        total.add(n.discovery_time)
        total.add(n.finish_time)
        assert (n.discovery_time + n.finish_time) % 2 == 1, "time values out of sequence"
    return sum(total)


if __name__ == "__main__":
    DFS_class = DFS
    unittest.main()
    DFS_class = DFSdraw
    unittest.main()
