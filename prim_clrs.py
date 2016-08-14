"""
CLRS pseudo-code, page 634:

A = {}

MST-PRIM(G, w, r)
1    for each u in G.V
2        u.key = infinity
3        u.pi = nil
4    r.key = 0
5    Q = G.V
6    while Q is not empty
7        u = Extract-Min(Q)
8        for each v in G.Adj[u]
9            if v in Q and w(u,v) < v.key
10               v.pi = u
11               v.key = w(u,v)

A = {(v,v.pi): v in V - {r}}
"""


from graph_algorithm import GraphAlgorithm
from graph_functions import extractMin
from algorithm_exceptions import AlgorithmTerminatedException


class PrimCLRS(GraphAlgorithm):
    def __init__(self, graph):
        self.Q = ["empty"]
        self.A = set()
        super().__init__(graph)
    

    def assertValid(self):
        pass


    def _doPrep(self):
        for u in self.graph.getNodes().values():
            u.key = float("infinity")
            u.pi = None
        r = list(self.graph.getNodes().values())[0]
        r.key = 0
        self.Q = list(self.graph.getNodes().values())


    def doStep(self):
        if self.hasTerminated() == False:
            u, self.Q = extractMin(self.Q, "key")
            neighbours = u.getAllEdges()
            for e in neighbours:
                if e.getEnds()[0] is not u:
                    v = e.getEnds()[0]
                    if v in self.Q and e.getWeight() < v.key:
                        v.pi = u
                        v.key = e.getWeight()
                else:
                    v = e.getEnds()[1]
                    if v in self.Q and e.getWeight() < v.key:
                        v.pi = u
                        v.key = e.getWeight()
            self._checkTermination()
        else:
            raise AlgorithmTerminatedException("Prim has already terminated")


    def doComplete(self):
        while self.hasTerminated() == False:
        	self.doStep()


    # this method also exists in Kruskal
    def getMSTdata(self) -> (int, int):
        total = 0
        for v in list(self.graph.getNodes().values()):
        	total += v.key
        	for e in v.getAllEdges():
        		if (e.getEnds() == (v, v.pi)) or (e.getEnds() == (v.pi, v)):
        			self.A.add(e)

        num_edges = len(self.A)
        return total, num_edges


    def _checkTermination(self):
        # CLRS Prim has terminated when all vertices have been pulled from the min heap.
        if len(self.Q) == 0:
            self.has_terminated = True
