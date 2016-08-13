"""
From CLRS page 604:

DFS(G)
1 for each vertex u in G.V
2	u.color = WHITE
3	u.pi = NIL
4 time = 0
5 for each vertex u in G.V
6 	if u.color == WHITE
7		DFS-VISIT(G, u)

DFS-VISIT(G, u)
1 time = time + 1	// white vertex u has just been discovered
2 u.d = time
3 u.color = GRAY
4 for each v in G.Adj[u]	// explore edge (u, v)
5	if v.color == WHITE
6		v.pi = u
7		DFS-VISIT(G, v)
8 u.color = BLACK	// blacken u; it i finished
9 time = time + 1
10 u.f = time

NOTE: CLRS do not show any code for accounting for edge status, yet they do colour
the edges when illustrating how the algorithm works.

The DFS class quietly adds two attributes to the Node class: Node.colour; Node.pi.
It also adds one attribute to the Edge class: Edge.explored.
Alternative would be to explicitly sub-class the Node and Edge classes.
"""


from graph_algorithm import GraphAlgorithm
from algorithm_exceptions import AlgorithmTerminatedException

# colour constants ... I don't yet know what will work best

class DFS(GraphAlgorithm):


    WHITE = "white"
    GRAY = "#666"
    BLACK = "black"


    def __init__(self, graph):
        self.time = 0
        self.iterators = []
        super(DFS, self).__init__(graph)

    def _doPrep(self):
        """ The DFS class quietly adds two attributes to the Node class: Node.colour; Node.pi.
        It adds one attribute to the Edge class: Edge.explored. """
        self.vertex_list = list(self.graph.getNodes().values())
        self.next_vertex = self.vertex_list[0]
        self.next_vertex_index = 1
        for vertex in self.vertex_list:
            vertex.colour = self.WHITE
            vertex.pi = None
            vertex.discovery_time = None
            vertex.finish_time = None
        self.iterators.append(self.DFSstart())


    def doStep(self):
        # print("number of iterators = " + str(len(self.iterators)))
        if self.hasTerminated() is False:
            served = False
            while served == False:
                try:
                    # We are treating the list of iterators as a stack.
                    result = next(self.iterators[-1])
                    served = True
                except StopIteration:
                    self.iterators.pop(-1)
                    # print("popping one iterator")
            # now check if done
            self._checkTermination()
        else:
            raise AlgorithmTerminatedException("DFS has already terminated")


    def DFSstart(self):
        for vertex in self.vertex_list:
            print("starting new tree")
            if vertex.colour == self.WHITE:
                self.iterators.append(self.DFSvisit(vertex))
                yield self.time


    def DFSvisit(self, vertex):
        self.time += 1
        vertex.discovery_time = self.time
        vertex.colour = self.GRAY
        for neighbour in vertex.getNeighbours():
            if neighbour.colour == self.WHITE:
                neighbour.pi = vertex
                self.iterators.append(self.DFSvisit(neighbour))
                yield self.time
        yield self.time
        vertex.colour = self.BLACK
        self.time += 1
        vertex.finish_time = self.time
        yield self.time


    def doComplete(self):
        while self.hasTerminated() is False:
            self.doStep()

    def assertValid(self):
        pass

    def _checkTermination(self):
        # DFS has terminated when every node has been discovered and finished.
        if self.time == 2 * len(self.graph.getNodes()):
            self.has_terminated = True


    def selectFirstVertex(self, vertex: str ="root"):
        # TODO: if there is a node called 'root', place it at the head of the list
        pass
