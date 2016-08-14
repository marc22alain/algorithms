# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:17:23 2016

@author: marc_alain
"""
from tkinter import *
from tkinter import ttk

from dfs_draw import DFSdraw
from dijkstra_draw import DijkstraDraw
from kruskal_draw import KruskalDraw
from prim_clrs_draw import PrimCLRSDraw
from prim_draw import PrimDraw

class MenuBar(object):
    def __init__(self, graphmaker):
        self.graphmaker = graphmaker
        self.top = self.graphmaker.winfo_toplevel()
        self.menuBar = Menu(self.top)
        self.top['menu'] = self.menuBar
        self.makeGraphManage()
        self.makeAlgorithms()


    def makeGraphManage(self):
        self.sub_menu_graph_manage = Menu(self.menuBar)
        self.menuBar.add_cascade(label='Graph', menu=self.sub_menu_graph_manage)
        self.sub_menu_graph_manage.add_command(label='Clear all elements', command=self.graphmaker.clearAll)
        self.sub_menu_graph_manage.add_command(label='Print all elements', command=self.graphmaker.printElements)


    def makeAlgorithms(self):
        self.sub_menu_algos = Menu(self.menuBar)
        self.menuBar.add_cascade(label='Algorithms', menu=self.sub_menu_algos)
        self.sub_menu_algos.add_command(label='DFS', command=self.loadDFS)
        self.sub_menu_algos.add_command(label='Dijkstra', command=self.loadDijkstra)
        self.sub_menu_algos.add_command(label='Kruskal', command=self.loadKruskal)
        self.sub_menu_algos.add_command(label='Prim-CLRS', command=self.loadPrimCLRS)
        self.sub_menu_algos.add_command(label='Prim', command=self.loadPrim)
        # self.sub_menu_algos.add_command(label='Floyd-Warshall', command=self.loadFloydWarshall)


    def loadDFS(self):
        self.graphmaker.registerAlgorithm(DFSdraw)

    def loadDijkstra(self):
        self.graphmaker.registerAlgorithm(DijkstraDraw)

    def loadKruskal(self):
        self.graphmaker.registerAlgorithm(KruskalDraw)

    def loadPrimCLRS(self):
        self.graphmaker.registerAlgorithm(PrimCLRSDraw)

    def loadPrim(self):
        self.graphmaker.registerAlgorithm(PrimDraw)

    def loadFloydWarshall(self):
        print("algorithm")



