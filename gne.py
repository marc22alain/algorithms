"""
Graph - Node - Edge

Motivation is to be able to simply code graph search algorithms, such as Prim, Kruskall, Dijkstra, Bellman-Ford.
Create the graphs, display them, run the algorithms, and show the results.
Oh and do unit testing on them too.
Also to instrument to calculate complexity.
Will need to also provide support for sorting nodes and edges, in right time-complexity.

directed != undirected, but the Node and Edge classes are implicitly directed by the ordering of nodes in tuples defining edges

Rules:
    1. each Node must have a unique name.
"""


class Graph(object):
    """Graphs are cool."""
    def __init__(self):
        self.name = "joe"
        self.nodes = {}
        self.edges = set()

    def addNodeList(self, nodes):
        for n in nodes:
            self.addNode(n)

    def addNode(self, node):
        assert type(node) in [ type(PosNode()), type(Node()) ]
        assert node.getName() not in self.nodes
        # self.nodes.append(node)
        self.nodes[node.getName()] = node

    def getNodes(self):
        return self.nodes

    def getNodeNames(self):
        names = "nodes: "
        for name in self.nodes.keys():
            names += name
            names += ", "
        return names[:-2]

    def addEdgeSet(self, edges):
        for e in edges:
            self.addEdge(e)

    def addEdgeList(self, edges):
        for e in edges:
            self.addEdge(e)

    def addEdge(self, edge):
        """ expecting a tuple: (source_node, target_node) """
        source_node = edge.ends[0]
        target_node = edge.ends[1]
        source_node.addOutEdge(edge)
        target_node.addInEdge(edge)
        self.edges.add(edge)
        for n in [source_node, target_node]:
            if n.getName() in self.nodes:
                if n is not self.nodes[n.getName()]:
                    raise ValueError("Node name refers to two different Nodes - in violation of Rule #1")
            else:
                self.addNode(n)
        # try:
        #     self.addNode(source_node)
        # except AssertionError:
        #     print "attempted to add node already stored"
        # try:
        #     self.addNode(target_node)
        # except AssertionError:
        #     print "attempted to add node already stored"

    def addEdgeByNames(self, node_name_tuple):
        print "Don't try to do this... EVER"
        # ... it will eventually violate Rule #1
        # self.addEdge( Edge( Node(node_name_tuple[0]), Node(node_name_tuple[1]) ) )

    def getEdges(self):
        return self.edges

    def graphSelfTest(self):
        """This will perform some self-diagnostic tests on the nodes and edges
         to determine its characterisitcs. Sub-classed graphs can then 
         determine if they are receiving correct input."""
         # such as:
         #  - is this a tree ? every node but root has 1 parent
         #      if yes, then do more on tree diagnoses
         #  - is the graph cyclic ?
         #  - does it have negative cycles ?
        pass

    def printElements(self):
        print "graph = Graph()"
        node_list = []
        for n in self.nodes.values():
            name = n.getName()
            print "%s = Node('%s')" %  (name, name)
            node_list.append(name)
        print "graph.addNodeList(%s)" % node_list
        for e in self.edges:
            s, t = e.getEnds()
            w = e.getWeight()
            print "graph.addEdge(Edge((%s,%s),%s))" % (s.getName(), t.getName(), w)



class Node(object):
    """Every node must have a unique hashable name."""
    def __init__(self, name="fred", value=0):
        self.name = name
        self.value = value
        self.in_edges = set()
        self.out_edges = set()
        # # .p and .x are used for the CLRS DisjointSet
        # self.p = None
        # self.x = None

    def getName(self):
        return self.name

    def addInEdge(self, edge):
        self.in_edges.add(edge)

    def addOutEdge(self, edge):
        self.out_edges.add(edge)

    def getAllEdges(self):
        """Returns a union of sets."""
        return self.in_edges | self.out_edges

    def getInEdges(self):
        return self.in_edges

    def getOutEdges(self):
        return self.out_edges

    def getNeighbours(self):
        """Returns all neighbouring vertices."""
        neighbours = set()
        for edge in self.getAllEdges():
            ends = edge.getEnds()
            neighbours.add(ends[0])
            neighbours.add(ends[1])
        neighbours.remove(self)
        return neighbours


class Edge(object):
    """
    Edge class constructor takes a tuple of Nodes for edge definition, and a possible value.
    """
    def __init__(self, edge, value=1):
        self.weight = 1
        # source vs target node is by index in the tuple
        node = Node()
        assert type(edge[0]) == type(node), "requires nodes for the Edge constructor"
        assert type(edge[1]) == type(node), "requires nodes for the Edge constructor"
        self.ends = edge
        self.value = value

    def getEnds(self):
    	return self.ends

    def getWeight(self):
    	return self.value




class PosNode(Node):
    def __init__(self, name="fred", value=0):
        Node.__init__(self, name, value=0)
        self.position = ()

    def setPosition(self, position):
        """ position in an n-dimensional tuple """
        self.position = position

    def getPosition(self):
        return self.position
