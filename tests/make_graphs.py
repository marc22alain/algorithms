import os
import sys

path = os.getcwd().split("/")
# print path

new_path = ""
for i in range(1, len(path) - 1):
    new_path += "/" + path[i]
# print new_path

sys.path.append(new_path)

from gne import Graph, Node, Edge


def makeSingleEdge():
    a = Node("a")
    b = Node("b")
    graph = Graph()
    graph.addNode(a)
    graph.addNode(b)
    graph.addEdge(Edge((a,b), 2))
    MSTweight = 2
    return {"graph": graph}


def makeTwoEdge():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    graph = Graph()
    graph.addNode(a)
    graph.addNode(b)
    graph.addNode(c)
    graph.addEdge(Edge((a,b), 2))
    graph.addEdge(Edge((a,c), 1))
    MSTweight = 3
    return {"graph": graph}


def makeThreeEdge():
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
    MSTweight = 5
    return {"graph": graph}

def makeDijkstraChallenge1():
    s = Node("s")
    t = Node("t")
    x = Node("x")
    y = Node("y")
    z = Node("z")
    graph = Graph()
    graph.addNodeList([s, t, x, y, z])
    graph.addEdgeList([Edge((s, t), 10), Edge((s, y), 5)])
    graph.addEdgeList([Edge((t, y), 2), Edge((t, x), 1)])
    graph.addEdgeList([Edge((x, z), 4)])
    graph.addEdgeList([Edge((y, t), 3), Edge((y, x), 9), Edge((y, z), 2)])
    graph.addEdgeList([Edge((z, s), 7), Edge((z, x), 6)])
    return {"graph":graph, "weights":[], "source":s, "shortest-paths":{"s": 0, "t": 8, "x": 9, "y": 5, "z": 7}}

def makeBellmanFordChallenge2():
    # since dijkstraChallenge1 == bellmanFordChallenge
    s = Node("s")
    t = Node("t")
    x = Node("x")
    y = Node("y")
    z = Node("z")
    graph = Graph()
    graph.addNodeList([s, t, x, y, z])
    graph.addEdgeList([Edge((s, t), 10), Edge((s, y), 5)])
    graph.addEdgeList([Edge((t, y), -4), Edge((t, x), 1)])
    graph.addEdgeList([Edge((x, z), 4)])
    graph.addEdgeList([Edge((y, t), 3), Edge((y, x), 9), Edge((y, z), 2)])
    graph.addEdgeList([Edge((z, s), 7), Edge((z, x), 6)])
    return {"graph":graph, "weights":[], "source":s, "shortest-paths":{"s": 0, "t": 8, "x": 9, "y": 5, "z": 7}}

def makeDAG1():
    graph = Graph()
    graph.addEdge(Edge((Node('a'),Node('b'),2.0)))
    return {"graph": graph}


def makeuGraph1():
    """Example from CLRS, figure 23.4, for demo of Kruskal's algorithm."""
    graph = Graph()
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    graph.addNodeList([a, b, c, d, e, f, g, h, i])
    graph.addEdge(Edge((c,d),7.0))
    graph.addEdge(Edge((i,c),2.0))
    graph.addEdge(Edge((d,e),9.0))
    graph.addEdge(Edge((d,f),14.0))
    graph.addEdge(Edge((e,f),10.0))
    graph.addEdge(Edge((b,h),11.0))
    graph.addEdge(Edge((f,g),2.0))
    graph.addEdge(Edge((h,i),7.0))
    graph.addEdge(Edge((g,h),1.0))
    graph.addEdge(Edge((h,a),8.0))
    graph.addEdge(Edge((g,i),6.0))
    graph.addEdge(Edge((a,b),4.0))
    graph.addEdge(Edge((b,c),8.0))
    graph.addEdge(Edge((c,f),4.0))
    return {"graph": graph, "shortest_path": 37, "num_edges": 8}

def makeRule1Violation1():
    graph = Graph()
    a = Node("a")
    aa = Node("a")
    b = Node("b")
    graph.addEdge(Edge((a,b),1))
    graph.addEdge(Edge((b,aa),1))
    return "oops"

def makeDirectedWeightedNeg1():
    """Example from CLRS, figure 25.2, for use with APSP algorithms."""
    graph = Graph()
    n1 = Node('n1')
    n3 = Node('n3')
    n2 = Node('n2')
    n5 = Node('n5')
    n4 = Node('n4')
    n6 = Node('n6')
    graph.addNodeList([n1, n3, n2, n5, n4, n6])
    graph.addEdge(Edge((n4,n1),-4.0))
    graph.addEdge(Edge((n5,n2),7.0))
    graph.addEdge(Edge((n2,n1),1.0))
    graph.addEdge(Edge((n6,n2),5.0))
    graph.addEdge(Edge((n3,n2),2.0))
    graph.addEdge(Edge((n6,n3),10.0))
    graph.addEdge(Edge((n3,n6),-8.0))
    graph.addEdge(Edge((n2,n4),2.0))
    graph.addEdge(Edge((n1,n5),-1.0))
    graph.addEdge(Edge((n4,n5),3.0))
    return {"graph": graph, "shortest_path": 0, "num_edges": 10}

def makeSimpleDirectedWeightedNeg1():
    graph = Graph()
    n1 = Node("n1")
    n3 = Node("n3")
    n2 = Node("n2")
    n5 = Node("n5")
    n4 = Node("n4")
    graph.addNodeList([n1, n3, n2, n5, n4])
    graph.addEdge(Edge((n5,n4),1.0))
    graph.addEdge(Edge((n1,n4),7.0))
    graph.addEdge(Edge((n1,n2),3.0))
    graph.addEdge(Edge((n2,n3),3.0))
    graph.addEdge(Edge((n3,n4),1.0))
    graph.addEdge(Edge((n2,n5),-2.0))
    shortest_paths = [[0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0]]
    parents = [[0, 0, 0, 0, 0],\
               [0, 0, 0, 0, 0],\
               [0, 0, 0, 0, 0]]     
    return {"graph": graph, "shortest_path": shortest_paths, "num_edges": 6, "parents": parents}

def makeTriangles1():
    graph = Graph()
    A = Node('A')
    C = Node('C')
    B = Node('B')
    E = Node('E')
    D = Node('D')
    F = Node('F')
    graph.addNodeList([A, C, B, E, D, F])
    graph.addEdge(Edge((A,B),3.0))
    graph.addEdge(Edge((C,D),2.0))
    graph.addEdge(Edge((A,C),5.0))
    graph.addEdge(Edge((D,B),1.0))
    graph.addEdge(Edge((B,C),8.0))
    graph.addEdge(Edge((E,C),7.0))
    return {"graph": graph, "shortest_path": 0, "num_edges": 6}


def makeTriangles2():
    graph = Graph()
    a = Node('a')
    c = Node('c')
    b = Node('b')
    e = Node('e')
    d = Node('d')
    g = Node('g')
    f = Node('f')
    i = Node('i')
    h = Node('h')
    j = Node('j')
    graph.addNodeList([a, c, b, e, d, g, f, i, h, j])
    graph.addEdge(Edge((i,j),1.0))
    graph.addEdge(Edge((f,g),1.0))
    graph.addEdge(Edge((a,b),1.0))
    graph.addEdge(Edge((g,i),1.0))
    graph.addEdge(Edge((b,c),1.0))
    graph.addEdge(Edge((c,d),1.0))
    graph.addEdge(Edge((g,h),1.0))
    graph.addEdge(Edge((d,b),1.0))
    graph.addEdge(Edge((c,e),1.0))
    graph.addEdge(Edge((f,h),1.0))
    graph.addEdge(Edge((e,b),1.0))
    graph.addEdge(Edge((f,i),1.0))
    graph.addEdge(Edge((c,i),1.0))
    graph.addEdge(Edge((j,f),1.0))
    return {"graph": graph, "shortest_path": 0, "num_edges": 14}

def makeMultiCycle():
    graph = Graph()
    a = Node('a')
    c = Node('c')
    b = Node('b')
    e = Node('e')
    d = Node('d')
    g = Node('g')
    f = Node('f')
    h = Node('h')
    k = Node('k')
    ij = Node('ij')
    graph.addNodeList([a, c, b, e, d, g, f, h, k, ij])
    graph.addEdge(Edge((f,h),1.0))
    graph.addEdge(Edge((e,h),1.0))
    graph.addEdge(Edge((c,k),1.0))
    graph.addEdge(Edge((f,b),1.0))
    graph.addEdge(Edge((k,ij),1.0))
    graph.addEdge(Edge((ij,c),1.0))
    graph.addEdge(Edge((a,b),1.0))
    graph.addEdge(Edge((b,c),1.0))
    graph.addEdge(Edge((g,c),1.0))
    graph.addEdge(Edge((c,d),1.0))
    graph.addEdge(Edge((d,e),1.0))
    graph.addEdge(Edge((b,g),1.0))
    return {"graph": graph, "shortest_path": 0, "num_edges": 12}


def makeTree():
    graph = Graph()
    a = Node('a')
    c = Node('c')
    b = Node('b')
    e = Node('e')
    d = Node('d')
    g = Node('g')
    f = Node('f')
    i = Node('i')
    h = Node('h')
    k = Node('k')
    j = Node('j')
    m = Node('m')
    l = Node('l')
    n = Node('n')
    root = Node('root')
    graph.addNodeList([a, c, b, e, d, g, f, i, h, k, j, m, l, n, root])
    graph.addEdge(Edge((g,l),4.0))
    graph.addEdge(Edge((b,f),8.0))
    graph.addEdge(Edge((d,i),6.0))
    graph.addEdge(Edge((c,g),2.0))
    graph.addEdge(Edge((root,a),2.0))
    graph.addEdge(Edge((c,h),3.0))
    graph.addEdge(Edge((root,b),4.0))
    graph.addEdge(Edge((h,n),23.0))
    graph.addEdge(Edge((a,c),3.0))
    graph.addEdge(Edge((g,k),91.0))
    graph.addEdge(Edge((a,d),7.0))
    graph.addEdge(Edge((h,m),54.0))
    graph.addEdge(Edge((b,e),7.0))
    graph.addEdge(Edge((e,j),6.0))
    return {"graph": graph, "shortest_path": 0, "num_edges": 14}
