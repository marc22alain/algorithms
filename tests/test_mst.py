"""
Properties of MST that we should be testing for:
    - that the tree spans all vertices
    - that the edges in the tree are a minimum span, in number of edges and in weight of edges
"""


import os
import sys
import unittest

from make_graphs import *

# path = os.getcwd().split("/")
# # print path

# new_path = ""
# for i in range(1, len(path) - 1):
#     new_path += "/" + path[i]
# # print new_path

# sys.path.append(new_path)

from kruskal import Kruskal
from prim import Prim
from prim_clrs import PrimCLRS
from gne import Graph, Node, Edge
from algorithm_exceptions import AlgorithmTerminatedException


class TestMST(unittest.TestCase):

    def setUp(self):
        self.k1 = graph_class(self.makeSingleEdge())
        self.k2 = graph_class(self.makeTwoEdge())
        self.k3 = graph_class(self.makeThreeEdge())
        if graph_class == PrimCLRS:
            # since PrimCLRS iterates over all the vertices to do its thing,
            # it requires one more iteration than the algorithms iterating
            # over the edges; these add one edge to the spanning tree
            # per iteration, and for spanning tree S, |S| = |V| - 1
            self.k1.doStep()
            self.k2.doStep()
            self.k3.doStep()
        

    # @ unittest.skip("j")
    def test_singleStep(self):
        self.k1.doStep()
        total, num_edges = self.k1.getMSTdata()
        self.assertEqual(total, 2)
        self.assertEqual(num_edges, 1)

        self.k2.doStep()
        total, num_edges = self.k2.getMSTdata()
        self.assertEqual(total, 1)
        self.assertEqual(num_edges, 1)

        self.k3.doStep()
        total, num_edges = self.k3.getMSTdata()
        self.assertEqual(total, 1)
        self.assertEqual(num_edges, 1)

    # @ unittest.skip("j")
    def test_twoSteps(self):
        self.k2.doStep()
        self.k2.doStep()
        total, num_edges = self.k2.getMSTdata()
        self.assertEqual(total, 3)
        self.assertEqual(num_edges, 2)

        self.k3.doStep()
        self.k3.doStep()
        total, num_edges = self.k3.getMSTdata()
        self.assertEqual(total, 5)
        self.assertEqual(num_edges, 2)


    # @ unittest.skip("j")
    def test_threeSteps(self):
        self.k3.doStep()
        self.k3.doStep()
        # confirm that the assertion is raised
        self.assertRaises(AlgorithmTerminatedException, self.k3.doStep)
        total, num_edges = self.k3.getMSTdata()
        self.assertEqual(total, 5)
        self.assertEqual(num_edges, 2)

#    @ unittest.skip("j")
    def test_doComplete(self):
        self.k1.doComplete()
        total, num_edges = self.k1.getMSTdata()
        self.assertEqual(total, 2)
        self.assertEqual(num_edges, 1)

        self.k2.doComplete()
        total, num_edges = self.k2.getMSTdata()
        self.assertEqual(total, 3)
        self.assertEqual(num_edges, 2)

        self.k3.doComplete()
        total, num_edges = self.k3.getMSTdata()
        self.assertEqual(total, 5)
        self.assertEqual(num_edges, 2)


#    @ unittest.skip("j")
    def test_CLRS_example1(self):
        test_structure = makeuGraph1()
        edges = test_structure["graph"].getEdges()
        self.assertEqual(len(edges), 14)
        nodes = test_structure["graph"].getNodes()
        self.assertEqual(len(nodes), 9)

        self.k4 = graph_class(test_structure["graph"])
        self.k4.doComplete()
        total, num_edges = self.k4.getMSTdata()
        self.assertEqual(num_edges, test_structure["num_edges"])
        self.assertEqual(total, test_structure["shortest_path"])


    def makeSingleEdge(self):
        a = Node("a")
        b = Node("b")
        graph = Graph()
        graph.addNode(a)
        graph.addNode(b)
        graph.addEdge(Edge((a,b), 2))
        return graph


    def makeTwoEdge(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        graph = Graph()
        graph.addNode(a)
        graph.addNode(b)
        graph.addNode(c)
        graph.addEdge(Edge((a,b), 2))
        graph.addEdge(Edge((a,c), 1))
        return graph


    def makeThreeEdge(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        graph = Graph()
        graph.addNode(a)
        graph.addNode(b)
        graph.addNode(c)
        graph.addEdge(Edge((a,b), 5))
        graph.addEdge(Edge((c,b), 4))
        graph.addEdge(Edge((a,c), 1))
        return graph



if __name__ == "__main__":
    # repeat for next MST algorithm
    graph_class = Kruskal
    unittest.main()
    # repeat for next MST algorithm
    graph_class = PrimCLRS
    unittest.main()
    # repeat for next MST algorithm
    graph_class = Prim
    unittest.main()
    