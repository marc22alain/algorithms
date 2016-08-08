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
"""


from graph_algorithm import GraphAlgorithm

# colour constants ... I don't yet know what will work best
WHITE = "white"
GRAY = "#666"
BLACK = "black"

class DFS(GraphAlgorithm):
    def __init__(self, graph):
        self.time = 0
        self.iterators = []
        super(DFS, self).__init__(graph)

    def _doPrep(self):
    	self.vertex_list = self.graph.getNodes().values()
    	self.next_vertex = self.vertex_list[0]
    	self.next_vertex_index = 1
    	for vertex in self.vertex_list:
    		vertex.colour = WHITE
    		vertex.pi = None
    	self.iterators.append(self.DFSstart())


    def doStep(self):
    	print "number of iterators = " + str(len(self.iterators))
    	served = False
    	while not served:
    		try:
    			result = next(self.iterators[-1])
    			served = True
    		except StopIteration:
    			self.iterators.pop(-1)
    			print "popping one iterator"
    	return result


    def DFSstart(self):
    	for vertex in self.vertex_list:
    		print "starting new tree"
    		if vertex.colour == WHITE:
    			self.iterators.append(self.DFSvisit(vertex))
    			yield self.time

    def DFSvisit(self, vertex):
    	self.time += 1
    	vertex.discovery_time = self.time
    	vertex.colour = GRAY
    	for neighbour in vertex.getNeighbours():
    		if neighbour.colour == WHITE:
    			neighbour.pi = vertex
		    	self.iterators.append(self.DFSvisit(neighbour))
    			yield self.time
    	yield self.time
    	vertex.colour = BLACK
    	self.time += 1
    	vertex.finish_time = self.time
    	yield self.time


    def doComplete(self):
    	self.DFSstart()

    def assertValid(self):
    	pass


    # trying to do a single step at a time
    # def doStep(self):
    # 	yield self.time
    # 	while len(self.lists[0]) == 0:
    # 		self.lists.pop(0)
    # 	u = self.lists[0].pop(0)
    # 	if u.colour == WHITE:
    # 		self.time += 1








