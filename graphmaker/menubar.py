# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:17:23 2016

@author: marc_alain
"""
from tkinter import *
from tkinter import ttk

from dfs import DFS

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
        self.sub_menu_algos.add_command(label='Floyd-Warshall', command=self.loadFloydWarshall)


    def loadDFS(self):
        self.graphmaker.addDoStepButton("Do one DFS step", self.doDFSStep)
        # adding the DOSTEP control
        # separator
        # self.graphmaker.row_num += 1
        # ttk.Separator(self.graphmaker.DefineFrame,orient=HORIZONTAL).grid(row=self.graphmaker.row_num, column=0, columnspan=2, sticky="ew", pady=10)
        # # do DFS step
        # self.graphmaker.row_num += 1
        # self.graphmaker.do_step_button = Button(self.graphmaker.DefineFrame,text="Do one DFS step",command=self.doDFSStep, width=28)
        # self.graphmaker.do_step_button.grid(row=self.graphmaker.row_num, column=0, columnspan=2, pady=5)
        # TODO: decorate the drawing function

    def loadFloydWarshall(self):
        print("algorithm")


    def doDFSStep(self):
        print("doing one step")
        try:
            if self.graphmaker.dfs == None:
                self.graphmaker.dfs = DFS(self.graphmaker.graph)
        except AttributeError:
            self.graphmaker.dfs = DFS(self.graphmaker.graph)
        print(self.graphmaker.dfs.doStep())
        self.graphmaker.drawGraph()