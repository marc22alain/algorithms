"""
CLRS define a disjoint set, having the following operations:
    - Make-Set(v), which makes a set containing v
    - Find-Set(v), which finds the set that contains v
    - Union(u,v), which joins the previously disjoint sets that contained u and v

CLRS propose several underlying data structures to implement a disjoint set:
    - linked list
    - rooted trees

Countable operations are:
    - comparisons (value, node)
    - assignments (value, node)
    - mathematical (addition)

This implementation does not use ?any? Python data structures.
"""


class DisjointSet(object):
    """ Implements the disjoint set described by CLRS."""
    def __init__(self, union_by_rank = True, path_compression = True):
        self.union_by_rank = union_by_rank
        self.path_compression = path_compression
        self.operations_count = 0
        self.unique_objects = 0


    def findSet(self, x):
        """FindSet takes an object and returns the object that is 'representative'
        of the set. Can be considered the root object of its tree."""
        # no countable operations here
        assert type(x) == type(x.p), "not a valid parent"
        if self.path_compression == True:
            return self._findSetPathCompressionTrue(x)
        else:
            return self._findSetPathCompressionFalse(x)


    def _findSetPathCompressionTrue(self, x):
        # nice little recursive tree traverse
        # count the value comparison as 1 step
        self.addOpCount(1)
        if x.p is not x:
            # count the value assignment 1 step
            self.addOpCount(1)
            x.p = self.findSet(x.p)
        return x.p


    def _findSetPathCompressionFalse(self, x):
        # nice little recursive tree traverse
        # count the value comparison as 1 step
        self.addOpCount(1)
        if x.p is not x:
            return self.findSet(x.p)
        else:
            return x


    def makeSet(self, x):
        # make set is always 2 operations
        # count the node assignment as 1 step
        # assert type(x.p) != type(x), "this node has already been assignd to a set"
        try:
            a = x.p
            print "nde OK"
            raise TypeError("Node %s has already been assigned to a set" % x.__str__())
        except AttributeError as e:
            # print e
            x.p = x
            self.addOpCount(1)
            if self.union_by_rank == True:
                # count the value assignment 1 step
                self.addOpCount(1)
                x.rank = 0


    def union(self, x, y):
        # no countable operations here
        if self.union_by_rank == True:
            self._linkByRankTrue(self.findSet(x), self.findSet(y))
        else:
            self._linkByRankFalse(self.findSet(x), self.findSet(y))
        


    def _linkByRankTrue(self, x, y):
        # count the value comparison as 1 step
        self.addOpCount(1)
        if x.rank > y.rank:
            # count the node assignment as 1 step
            self.addOpCount(1)
            y.p = x
        else:
            # count the node assignment as 1 step
            self.addOpCount(1)
            x.p = y
            # count the value comparison as 1 step
            self.addOpCount(1)
            if x.rank == y.rank:
                # count the addition operation as 1 step
                self.addOpCount(1)
                y.rank += 1


    def _linkByRankFalse(self, x, y):
        # count the parent assignment 1 step
        self.addOpCount(1)
        y.p = x


    def getTimeComplexity(self):
        # no countable operations here
        return self.operations_count


    def addOpCount(self, num):
        # no countable operations here
        self.operations_count += num
