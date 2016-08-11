"""
Kruskall's algorithm produces a minimum spanning tree for an undirected graph G(V,E) with w(e) -> R.
Procedure:
    1. sort all n edges by weight (pick any efficient method) into a list
    2. for i in 1 to n:
    3.     pop first edge in list
    4.     if the two node ends are in separate sub-trees, then add the edge to the MST

Supporting data structures:
    a. a list of edges sorted by weight
        CLRS use a binary search tree for efficiency
    b. some structure to hold the forest; a Python set would do well
        CLRS use a disjoint set, to hold the trees of the forest
        since CLRS only propose the disjoint set, it could easily be used to compose
        the Kruskal, not just be present as a separate resource... 
        ... except that the DJS has features that are available through its constructor !

CLRS pseudo-code, page 631:
MST-KRUSKAL (G, w)
1    A = {empty}
2    for each vertex in G.V
3        MakeSet(v)
4    sort the edges of G:E into nondecreasing order by weight w
5    for each edge (u,v) in G.E, taken in nondecreasing order by weight
6        if FindSet(u) != FindSet(v)
7            A = A union {(u,v)}
8            Union(u,v)
9    return A
"""

from graph_algorithm import GraphAlgorithm
import disjoint_set as DJS
from algorithm_exceptions import AlgorithmTerminatedException


ds_all = DJS.DisjointSet()

class Kruskal(GraphAlgorithm):
    def __init__(self, graph):
        super(Kruskal, self).__init__(graph)
        self.A = set()


    def assertValid(self):
        """
        Assertions: completed MST has n - 1 edges
        """
        # |A| <= |V| - 1 ... this is shared with many other algorithms !
        # ... could also be called the 'acyclic' test (though it is necessary, this property is not sufficient)

        # assertions_summary = ""
        # if len(MST) == n - 1:
            # assertions_summary += "MST has n - 1 edges"
        # else:
            # assertions_summary += "MST has k edges while it should have n - 1"
        # return assertions_summary
        pass


    def _doPrep(self):
        """
        Does three things:
            - makes a set forest
            - sorts the edges by weight
            - decorates the Edge class with E.included, for later use by graph_maker
        """
        # need to assert that the iterable delivers Nodes !
        # in the meantime, assume its a dict
        nodes = self.graph.getNodes().values()
        for n in nodes:
            ds_all.makeSet(n)
        # have not even bothered to wrap this in a pseudo-implementation of a BST
        self.ordered_edges = sorted(list(self.graph.getEdges()), key=lambda edge: edge.getWeight())
        for e in self.graph.getEdges():
            e.included = False


    def doStep(self) -> bool:
        if self.hasTerminated() is False:
            served = False
            while served == False:
                e = self.ordered_edges.pop(0)
                u = e.getEnds()[0]
                v = e.getEnds()[1]
                if ds_all.findSet(u) is not ds_all.findSet(v):
                    ds_all.union(u, v)
                    self.A.add(e)
                    e.included = True
                    served = True
            self._checkTermination()
        else:
            raise AlgorithmTerminatedException("Kruskal has already terminated")


    def doComplete(self):
        for e in self.ordered_edges:
            u = e.getEnds()[0]
            v = e.getEnds()[1]
            if ds_all.findSet(u) is not ds_all.findSet(v):
                ds_all.union(u, v)
                self.A.add(e)
                e.included = True
        return self.A


    def getMSTdata(self):
        total = 0
        num_edges = len(self.A)
        for e in self.A:
            total += e.getWeight()
        return total, num_edges


    def _checkTermination(self):
        # Kruskal has terminated there is an MST, when the number of edges is one less than
        # the number of nodes.
        if len(self.A) == len(self.graph.getNodes()) - 1:
            self.has_terminated = True

