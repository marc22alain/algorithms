"""
This is not the CLRS implementation of Prim's MST.
Unlike the CLRS implementation, this one will grow the tree one edge at a time.
The loop invariant is as follows: consider the vertex partitions T, V - T; 
every added edge will be the least valued edge between the two partitions.
Prim implementation below will grow edge set A until a spanning tree is formed.

TODO: benchmark performance against the CLRS implementation !
"""

from graph_algorithm import GraphAlgorithm
from graph_functions import extractMin
from algorithm_exceptions import AlgorithmTerminatedException


class Prim(GraphAlgorithm):
    def __init__(self, graph):
        # self.Q = ["empty"]
        self.covered = set()
        self.A = set()
        super().__init__(graph)
    

    def assertValid(self):
        pass


    def _doPrep(self):
        # pick a starting vertex and add it to the list of covered vertices
        r = list(self.graph.getNodes().values())[0]
        self.covered.add(r)
        # add all edges incident to the newly added vertex for consideration in the spanning tree
        self.ordered_edges = list(r.getAllEdges())
        for e in self.graph.getEdges():
            e.included = False


    def doStep(self):
        if self.hasTerminated() == False:
            served = False
            while served == False:
                # let's be greedy: pick the cheapest edge incident to the covered vertices, then see if we can use it
                e, self.ordered_edges = extractMin(self.ordered_edges, "value")
                u, v = e.getEnds()
                # the algorithm is for undirected graphs, so the not-covered vertex might be either of u or v
                # if both u and v are already covered, then the loop discards this edge and picks the next cheapest one
                if u not in self.covered:
                    # add u to the covered vertex set and add its incident edges for consideration in the spaning tree
                    self.covered.add(u)
                    # this conversion from list to set to list ensures no edge duplicates in the final list
                    self.ordered_edges = list(set(self.ordered_edges) | u.getAllEdges())
                    served = True
                elif v not in self.covered:
                    self.covered.add(v)
                    self.ordered_edges = list(set(self.ordered_edges) | v.getAllEdges())
                    served = True
            self.A.add(e)
            e.included = True
            self._checkTermination()
        else:
            raise AlgorithmTerminatedException("Prim has already terminated")


    def doComplete(self):
        while self.hasTerminated() == False:
        	self.doStep()


    # this method is common to all MST algorithms
    def getMSTdata(self):
        total = 0
        num_edges = len(self.A)
        for e in self.A:
            total += e.getWeight()
        return total, num_edges


    def _checkTermination(self):
        # This Prim implementation will have terminated when there is an MST, when the number
        # of edges is one less than the number of nodes.
        if len(self.A) == len(self.graph.getNodes()) - 1:
            self.has_terminated = True
