import os
import sys
#import unittest

import make_graphs as mg

path = os.getcwd().split("/")
print(path)

new_path = ""
for i in range(1, len(path) - 1):
    new_path += "/" + path[i]
print(new_path)

sys.path.append(new_path)

from dfs import DFS



dfs = DFS(mg.tree()["graph"])

for i in range(15):
	print(dfs.doStep())