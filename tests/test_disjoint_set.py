import os
import sys
import unittest


path = os.getcwd().split("/")
# print path

new_path = ""
for i in xrange(1, len(path) - 1):
    new_path += "/" + path[i]
# print new_path

sys.path.append(new_path)

import disjoint_set as DJS
from gne import Node


ds_none = DJS.DisjointSet(False, False)
ds_all = DJS.DisjointSet()


class TestDisjointSet(unittest.TestCase):

    def setUp(self):
        self.x = Node()
        self.y = Node()

    def tearDown(self):
        ds_none.operations_count = 0
        ds_all.operations_count = 0

    def test_findItself(self):
        self.x.p = self.x
        self.assertEqual(self.x, ds_none.findSet(self.x))
        self.assertEqual(self.x, ds_all.findSet(self.x))
        self.assertEqual(ds_none.getTimeComplexity(), 1)
        self.assertEqual(ds_all.getTimeComplexity(), 1)

    @unittest.skip("not sure what this test should challenge now")
    def test_NOTfindItself(self):
        # !!! since having removed base class attribute x.p and now have it in 
        # the makeSet() method, the purpose of this test is lost !!!

        # note that the following line confirms that setUp() is doing its thing
        # self.x.p = self.x
        exception_count = 0
        try:
            ds_none.findSet(self.x)
        except AssertionError as e:
            self.assertEqual("not a valid parent", e.__str__())
            exception_count += 1
        try:
            ds_all.findSet(self.x)
        except AssertionError as e:
            self.assertEqual("not a valid parent", e.__str__())
            exception_count += 1
        self.assertEqual(exception_count, 2)
        self.assertEqual(ds_none.getTimeComplexity(), 0)
        self.assertEqual(ds_all.getTimeComplexity(), 0)


    def test_makeSetNONE(self):
        ds_none.makeSet(self.x)
        self.assertEqual(self.x, ds_none.findSet(self.x))
        self.assertEqual(ds_none.getTimeComplexity(), 2)


    def test_makeSetALL(self):
        ds_all.makeSet(self.x)
        self.assertEqual(self.x, ds_all.findSet(self.x))
        self.assertEqual(ds_all.getTimeComplexity(), 3)


     

if __name__ == "__main__":
    unittest.main()