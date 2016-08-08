from tkinter import *
from tkinter import ttk
from math import *
from gne import Graph, Node, Edge
import random

from dfs import DFS

from tests import make_graphs


class Application(Frame):
    def __init__(self, master=None):
        self.canvas_options = {"width":500, "height":500, "bg":"black"}
        self.slot_options = {"spacing":50, "circle":20}
        Frame.__init__(self, master)
        self.grid()
        self.createSuperWidgets()
        self.graph = Graph()
        self.slots = self.makeSlots()
        self.nodes = {}
        self.drawGraph(0)
        self.dfs = None


    def createSuperWidgets(self):
        # the canvas
        self.DrawFrame = Frame(self,bd=5)
        self.DrawFrame.grid(row=0, column=0)

        self.canvas = Canvas(self.DrawFrame, self.canvas_options)
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.selectNode)
        self.canvas.bind("<ButtonRelease-1>", self.releaseNode)
        self.canvas.bind("<B1-Motion>", self.moveNode)

        # the user input
        self.DefineFrame = Frame(self,bd=5)
        self.DefineFrame.grid(row=0, column=1)
        self.createWidgets()    


    def createWidgets(self):
        # define the GRAPH
        row_num = 0
        self.DefineGraphFrame = LabelFrame(self.DefineFrame, text='Define the Graph', padx=60, labelanchor=N, font=("Lucida Sans", 14, "bold"), fg="#222288")
        self.DefineGraphFrame.grid(row=row_num, column=0, columnspan=2)

        row_num += 1
        self.directed_check_var = BooleanVar()
        self.directed_check_label = Checkbutton(self.DefineGraphFrame, text="Directed graph", variable=self.directed_check_var)
        self.directed_check_label.grid(row=row_num, column=0)

        row_num += 1
        self.weighted_edge_check_var = BooleanVar()
        self.weighted_edge_check_label = Checkbutton(self.DefineGraphFrame, text="Weighted edge graph", variable=self.weighted_edge_check_var)
        self.weighted_edge_check_label.grid(row=row_num, column=0)

        # separator
        row_num += 1
        ttk.Separator(self.DefineFrame,orient=HORIZONTAL).grid(row=row_num, column=0, columnspan=2, sticky="ew", pady=10)

        # add a NODE
        row_num += 1
        self.AddNodeFrame = LabelFrame(self.DefineFrame, text='Add a Node', padx=10, labelanchor=N, font=("Lucida Sans", 14, "bold"), fg="#222288")
        self.AddNodeFrame.grid(row=row_num, column=0, columnspan=2)

        row_num += 1
        self.node_name_label = Label(self.AddNodeFrame, text='Node name', width=13)
        self.node_name_label.grid(row=row_num, column=0)
        self.node_name_var = StringVar()
        self.node_name_input = Entry(self.AddNodeFrame, textvariable=self.node_name_var ,width=15)
        self.node_name_input.grid(row=row_num, column=1)

        row_num += 1
        self.node_add_button = Button(self.AddNodeFrame,text="Add this node",command=self.addNode, width=28)
        self.node_add_button.grid(row=row_num, column=0, columnspan=2, pady=5)

        # separator
        row_num += 1
        ttk.Separator(self.DefineFrame,orient=HORIZONTAL).grid(row=row_num, column=0, columnspan=2, sticky="ew", pady=10)

        # add an EDGE
        row_num += 1
        self.AddEdgeFrame = LabelFrame(self.DefineFrame, text='Add an Edge', padx=10, labelanchor=N, font=("Lucida Sans", 14, "bold"), fg="#222288")
        self.AddEdgeFrame.grid(row=row_num, column=0, columnspan=2)

        row_num += 1
        self.source_node_name_label = Label(self.AddEdgeFrame, text='Source node name', width=13)
        self.source_node_name_label.grid(row=row_num, column=0)
        self.source_node_name_var = StringVar()
        self.source_node_name_input = Entry(self.AddEdgeFrame, textvariable=self.source_node_name_var ,width=15)
        self.source_node_name_input.grid(row=row_num, column=1)

        row_num += 1
        self.target_node_name_label = Label(self.AddEdgeFrame, text='Target node name')
        self.target_node_name_label.grid(row=row_num, column=0)
        self.target_node_name_var = StringVar()
        self.target_node_name_input = Entry(self.AddEdgeFrame, textvariable=self.target_node_name_var ,width=15)
        self.target_node_name_input.grid(row=row_num, column=1)

        row_num += 1
        self.edge_weight_label = Label(self.AddEdgeFrame, text='Edge weight')
        self.edge_weight_label.grid(row=row_num, column=0)
        self.edge_weight_var = DoubleVar()
        self.edge_weight_input = Entry(self.AddEdgeFrame, textvariable=self.edge_weight_var ,width=15)
        self.edge_weight_input.grid(row=row_num, column=1)
        self.edge_weight_input.insert(1,1)

        row_num += 1
        self.node_add_button = Button(self.AddEdgeFrame,text="Add this edge",command=self.addEdge, width=28)
        self.node_add_button.grid(row=row_num, column=0, columnspan=2, pady=5)

        # separator
        row_num += 1
        ttk.Separator(self.DefineFrame,orient=HORIZONTAL).grid(row=row_num, column=0, columnspan=2, sticky="ew", pady=10)

        # clear ALL ELEMENTS
        row_num += 1
        self.clear_all_button = Button(self.DefineFrame,text="Clear all elements",command=self.clearAll, width=28)
        self.clear_all_button.grid(row=row_num, column=0, columnspan=2, pady=5)

        # separator
        row_num += 1
        ttk.Separator(self.DefineFrame,orient=HORIZONTAL).grid(row=row_num, column=0, columnspan=2, sticky="ew", pady=10)

        # print ELEMENTS of GRAPH as TEXT
        row_num += 1
        self.print_element_button = Button(self.DefineFrame,text="Print graph elements as list",command=self.printElements, width=28)
        self.print_element_button.grid(row=row_num, column=0, columnspan=2, pady=5)

        # separator
        row_num += 1
        ttk.Separator(self.DefineFrame,orient=HORIZONTAL).grid(row=row_num, column=0, columnspan=2, sticky="ew", pady=10)

        # do DFS step
        row_num += 1
        self.do_step_button = Button(self.DefineFrame,text="Do one step in DFS",command=self.doStep, width=28)
        self.do_step_button.grid(row=row_num, column=0, columnspan=2, pady=5)

        # separator
        row_num += 1
        ttk.Separator(self.DefineFrame,orient=HORIZONTAL).grid(row=row_num, column=0, columnspan=2, sticky="ew", pady=10)

        row_num += 1
        self.graph_name_label = Label(self.DefineFrame, text='Graph name', width=13)
        self.graph_name_label.grid(row=row_num, column=0)
        self.graph_name_var = StringVar()
        self.graph_name_input = Entry(self.DefineFrame, textvariable=self.graph_name_var ,width=15)
        self.graph_name_input.grid(row=row_num, column=1)

        # load a graph
        row_num += 1
        self.load_graph_button = Button(self.DefineFrame,text="load graph",command=self.loadGraph, width=28)
        self.load_graph_button.grid(row=row_num, column=0, columnspan=2, pady=5)


    def drawGraph(self, frame_num=1):
        self.canvas.delete("graph")
        # check what type of graph is defined
        directed = self.directed_check_var.get()
        weighted = self.weighted_edge_check_var.get()

        circle_rad = self.slot_options["circle"] / 2
        for k, key in enumerate(self.slots):
            slot = self.slots[key]
            x = slot["coords"][0]
            y = slot["coords"][1]
            node = slot["node"]
            if node == None:
                if frame_num == 0:
                    self.canvas.create_oval(x - circle_rad, y - circle_rad, x + circle_rad, y + circle_rad, outline="#333")
            else:
                # draw the node
                try:
                    colour = node.colour
                except AttributeError:
                    colour = "black"
                self.canvas.create_oval(x - circle_rad, y - circle_rad, x + circle_rad, y + circle_rad, outline="#fff", tag="graph", fill=colour)
                self.canvas.create_text(x, y - circle_rad * 2, text=slot["node"].getName(), fill="white", tag="graph")

                # then draw the edges that it sources
                for edge in node.getOutEdges():
                    adj_x, adj_y = self.getWeightLocationAdj(edge)
                    target_node = edge.getEnds()[1]
                    t_x, t_y = self.slots[self.nodes[target_node.getName()]]["coords"]
                    self.canvas.create_line(x, y, t_x, t_y, fill="#ff5500", tag="graph")
                    if weighted == True:
                        self.canvas.create_text(((x + t_x) / 2) + adj_x, ((y + t_y) / 2) - adj_y, text=edge.getWeight(), fill="#ff5500", tag="graph")
                    if directed == True:
                        self.drawArrowHeads(edge)


    def addNode(self):
        new_node = Node(self.node_name_var.get())
        self._addNode(new_node)
        print(self.graph.getNodeNames())
        self.drawGraph()
        self.node_name_input.delete(0, "end")


    def _addNode(self, new_node):
        self.graph.addNode(new_node)
        unassigned = True
        slots = list(self.slots.keys())
        while unassigned == True:
            choice = random.choice(slots)
            node = self.slots[choice]["node"]
            if node == None:
                self.slots[choice]["node"] = new_node
                unassigned = False
            else:
                slots.pop(slots.index(choice))
        self.nodes[new_node.getName()] = choice


    def makeSlots(self):
        """ One-time set-up function to create all the slots in the canvas. """
        width = self.canvas_options["width"]
        height = self.canvas_options["height"]
        circle = self.slot_options["circle"]
        spacing = self.slot_options["spacing"]
        slots = {}
        for i in range(1, (width // spacing)):
            for j in range(1, (height // spacing)):
                slots[(i,j)] = { "coords" : (i * spacing, j * spacing), "node" : None}
        return slots

    def clearAll(self):
        """ Delete all graph elements, to start anew. """
        self.graph = Graph()
        self.nodes.clear()
        slots = list(self.slots.keys())
        for slot in slots:
            self.slots[slot]["node"] = None
        self.dfs = None
        self.drawGraph()

    def addEdge(self):
        source_name = self.source_node_name_var.get()
        assert source_name in list(self.nodes.keys())
        target_name = self.target_node_name_var.get()
        assert target_name in list(self.nodes.keys())
        weight = self.edge_weight_var.get()
        assert type(weight) == float

        source = self.slots[self.nodes[source_name]]["node"]
        target = self.slots[self.nodes[target_name]]["node"]
        self.graph.addEdge(Edge((source, target), weight))  

        self.drawGraph()
        self.source_node_name_input.delete(0, "end")
        self.target_node_name_input.delete(0, "end")

    def selectNode(self, event):
        """ canvas click event handler """
        spacing = self.slot_options["spacing"]
        slot_select = ((event.x + (spacing / 2)) / spacing, (event.y + (spacing / 2)) / spacing)
        self.node_to_move = self.slots[slot_select]["node"]

    def releaseNode(self, event):
        """ canvas click event handler """
        self.canvas.delete("in_motion")
        spacing = self.slot_options["spacing"]
        slot_select = ((event.x + (spacing / 2)) / spacing, (event.y + (spacing / 2)) / spacing)
        if self.node_to_move != None and slot_select in list(self.slots.keys()) and self.slots[slot_select]["node"] == None:
            # move node out of previous slot
            previous_slot = self.nodes[self.node_to_move.getName()]
            self.slots[previous_slot]["node"] = None
            # move node into new slot
            self.slots[slot_select]["node"] = self.node_to_move
            self.nodes[self.node_to_move.getName()] = slot_select
            self.drawGraph()

    def moveNode(self, event):
        """ canvas click event handler """
        self.canvas.delete("in_motion")
        circle_rad = self.slot_options["circle"] / 2
        x, y = event.x, event.y
        self.canvas.create_oval(x - circle_rad, y - circle_rad, x + circle_rad, y + circle_rad, outline="#999900", tag="in_motion")
        if self.node_to_move != None:
            self.canvas.create_text(x, y - circle_rad * 2, text=self.node_to_move.getName(), fill="#999900", tag="in_motion")

    def getWeightLocationAdj(self, edge):
        """ Helper method for drawGraph; returns magic numbers for placing the edge weight w/r/t the edge. """
        nodes = edge.getEnds()
        source_coords = self.slots[self.nodes[nodes[0].getName()]]["coords"]
        target_coords = self.slots[self.nodes[nodes[1].getName()]]["coords"]
        edge_length = sqrt( (source_coords[0] - target_coords[0])**2 + (source_coords[1] - target_coords[1])**2 )
        circle = self.slot_options["circle"]
        adj_y = (source_coords[0] - target_coords[0]) / edge_length * circle
        adj_x = (source_coords[1] - target_coords[1]) / edge_length * circle
        return adj_x, adj_y


    def drawArrowHeads(self, edge):
        """ Helper method for drawGraph; returns magic numbers for placing the edge weight w/r/t the edge. """
        nodes = edge.getEnds()
        source_coords = self.slots[self.nodes[nodes[0].getName()]]["coords"]
        target_coords = self.slots[self.nodes[nodes[1].getName()]]["coords"]
        edge_length = sqrt( (source_coords[0] - target_coords[0])**2 + (source_coords[1] - target_coords[1])**2 )
        circle_rad = self.slot_options["circle"] / 2

        apex_x = source_coords[0] + ((target_coords[0] - source_coords[0]) * edge_length / (edge_length + circle_rad + 6))
        apex_y = source_coords[1] + ((target_coords[1] - source_coords[1]) * edge_length / (edge_length + circle_rad + 6))
        a = 4
        self.canvas.create_oval(apex_x - a, apex_y - a, apex_x + a, apex_y + a, outline="#999000", fill="#ff5500", tag="graph")
        # rad_x = acos( (target_coords[0] - source_coords[0]) / edge_length)
        # rad_y = asin( (target_coords[1] - source_coords[1]) / edge_length)
        # self.canvas.create_line(apex_x, apex_y, apex_x + (cos(rad_x + (0.5 * pi)) * circle_rad), apex_y + (sin(rad_y + (0.5 * pi)) * circle_rad), fill="#fff000", tag="graph")
        # print "acos", str(rad_x)
        # print "asin", str(rad_y)

    def printElements(self):
        self.graph.printElements()

    def doStep(self):
        print("doing one step")
        if self.dfs == None:
            self.dfs = DFS(self.graph)
        print(self.dfs.doStep())
        self.drawGraph()

    def loadGraph(self):
        graphs = dir(make_graphs)
        if self.graph_name_var.get() not in graphs:
            print(graphs)
        else:
            graph = eval("make_graphs." + self.graph_name_var.get() + "()")["graph"]
            for n in list(graph.getNodes().values()):
                self._addNode(n)
            self.graph = graph
        self.drawGraph()


app = Application()
app.master.title("Graph maker")
app.mainloop()