"""
Dijkstra's algorithm finds the shortest path from a single source to all other
vertices in the graph. It is correct when fed a directed graph with non-negative edges.
works only when there are no negative cycles (so it may
be possible for some edges to have non-negative weight).

Dijkstra's is described as using a greedy algorithm, as the next vertex it chooses to 
process is the closest (left) to explore. 

Q is a min-priority queue of vertices keyed by their 'd' value.
vertices have two special properties:
    - 'pi', which is in fact the vertex's predecessor in the shortest path
    - 'd', which is the estimate of the shortest path from source s to that 
      vertex

S holds the vertices 'whose final shortest-path weights from the source s have 
already been determined'. The algorithm begins with s, as s.d = 0.

Notes:
    - 'relaxation' is a common procedure, shared also by Bellman-Ford
    - G.Adj is the adjacency list that defines the graph
    - hand-drawn example seems to question the need for the queue picking the
      least v.d, as long as v.d < infinity, a path addition can be made;
      perhaps there are corner cases (or the proof) that require this condition.
    - the first vertex to be pulled is the source vertex, since it is assigned v.d = 0

Questions::
    - does Extract-Min() sort after the head is popped off, or before, 'cause
      the Q has to be sorted again after Relax() is performed; a key update
      in the for... loop would be perfect



CLRS pseudo-code, page 658:
DIJKSTRA(G, w, s):
1   Initialize-Single-Source(G, s)
2   S = {empty}
3   Q = G.V
4   while Q is not empty
5       u = Extract-Min(Q)
6       S = S union {u}
7       for each vertex v in G.Adj[u]
8           Relax(u, v, w)
"""

from tests.make_graphs import makeSingleEdge, dijkstraChallenge1

from graph_algorithm import GraphAlgorithm
from graph_functions import relax, initializeSingleSource, extractMin

# temporary
from gne import Graph, Node, Edge


class Dijkstra(GraphAlgorithm):
    def __init__(self, graph, weights, source):
        # the gne implementation already has a full edge definition for the weights;
        # this is redundant
        self.weights = weights
        self.source = source
        super(Dijkstra, self).__init__(graph)


    def assertValid(self):
        # |S| == |V| at end
        return "not implemented yet"


    def _doPrep(self):
        # initialize is a standard CLRS routine
        initializeSingleSource(self.graph, self.source)
        # initialize the set that will hold the processed vertices
        self.S = set()
        self.Q = self.graph.getNodes().values()


    def doStep(self):
        # Choose: doStep() executes one iteration of the while loop or one
        # iteration of the for loop
        return "not implemented yet"


    def doComplete(self):
        while len(self.Q) > 0:
            u , self.Q = extractMin(self.Q, "d")
            self.S.add(u)
            for edge in u.getOutEdges():
                relax(u, edge.getEnds()[1], edge.getWeight())

    def printS(self):
        for v in self.S:
            print(v.getName() + ": " + str(v.d))


# perhaps Extract-Min should be implemented in graph_functions,
# but would then need to pass an extra argument for the lambda key
# def extractMin(Q):
#     q = sorted(Q, key=lambda v: v.d)
#     return q.pop(0), q


args = dijkstraChallenge1()
d = Dijkstra(args[0], args[1], args[2])
d.doComplete()
d.printS()