"""
This module holds various functions that, well, have nowhere else to go.
"""


def relax(u, v, w):
    """CLRS page 649.
    Relax(u, v, w)
    1   if v.d > u.d + w(u, v):
    2       v.d = u.d + w(u, v)
    3       v.pi = u
    """
    # print u.getName()
    if v.d > (u.d + w):
        v.d = u.d + w
        v.pi = u


def printPath(G, s, v):
    """CLRS 22.2: prints shortest path (from s to v) working backwards from v
    using the v.pi attribute."""
    return "not implemented yet"


def initializeSingleSource(G, s):
    """CLRS page 648, an initial step to relaxation algorithms.
    InitializeSingleSource(G, s)
    1   for each vertex v in G.V
    2       v.d = +infinity
    3       v.pi = NIL
    4   s.d = 0
    """
    nodes = G.getNodes().values()
    for n in nodes:
        if n != s:
            n.d = float("inf")
            n.pi = None
    s.d = 0

def extractMin(Q: list, attribute: str) -> (object, list):
    """CLRS defines as sorting list into a priority queue and extracting the 
    minimimum value.
    This general implementation uses the second argument (a string) to specify
    the attribute to use as key for sorting the priority queue."""
    # alternative implementation is to define class 'property' and pass that in
    q = sorted(Q, key=lambda element: element.__getattribute__(attribute))
    popped = q.pop(0)
    # print attribute(popped)
    return popped, q
