import os
import sys
import unittest

from make_graphs import *

path = os.getcwd().split("/")
print path

# new_path = ""
# for i in xrange(1, len(path) - 1):
#     new_path += "/" + path[i]
# # print new_path

# sys.path.append(new_path)

# from ..dfs import DFS

from .. import gne


dfs = DFS(tree()["graph"])

for i in xrange(15):
	print dfs.doStep()