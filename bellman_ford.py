"""
Bellman-Ford solves the single-source-shortest-paths problem in the general 
case, i.e. with graphs having some negative-weighted edges.

In short, it relaxes the whole graph for n - 1 times (n = |G.V|). Then it
checks to see whether any edges can be relaxed again. This finds the negative
cycles.
The n - 1 is the magic number because this is the maximum number of edges that
do not automatically produce a cycle.

Bellman-Ford(G, w, s)
1   Initialize-Single-Source(G, s)
2   for i = 1 to |G.V| - 1
3       for each edge (u, v) in G.E
4           Relax(u, v, w)
5   for each edge (u, v) in G.E
6       if v.d > u.w + w(u, v)
7           return False
8   return True 
"""


from tests.make_graphs import dijkstraChallenge1, bellmanFordChallenge2

from graph_algorithm import GraphAlgorithm

from graph_functions import relax, initializeSingleSource



class BellmanFord(GraphAlgorithm):
    def __init__(self, graph, weights, source):
        # the gne implementation already has a full edge definition for the weights;
        # this is redundant
        self.weights = weights
        self.source = source
        super(BellmanFord, self).__init__(graph)


    def assertValid(self):
        return "not implemented yet"


    def _doPrep(self):
        initializeSingleSource(self.graph, self.source)


    def doStep(self):
        return "not implemented yet"


    def doComplete(self):
        for i in xrange(len(self.graph.getNodes().values())):
            for s in self.graph.getEdges():
                u = s.getEnds()[0]
                v = s.getEnds()[1]
                w = s.getWeight()
                relax(u, v, w)
        for s in self.graph.getEdges():
            u = s.getEnds()[0]
            v = s.getEnds()[1]
            w = s.getWeight()
            if v.d > u.d + w:
                return False
        return True



args = dijkstraChallenge1()
b = BellmanFord(args[0], args[1], args[2])
print b.doComplete()

args = bellmanFordChallenge2()
b = BellmanFord(args[0], args[1], args[2])
print b.doComplete()