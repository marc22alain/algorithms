"""
The purpose of the sub-classing is to explore by edges instead of by neighbouring vertices.
Since CLRS do not show any code for accounting for edge status, we add it to this sub-class.
"""


from dfs import DFS

class DFSdraw(DFS):

    do_step_message = "Do one DFS step"

    def __init__(self, graph):
        super().__init__(graph)


    def drawNode(self, canvas, slot, node, x, y, circle_rad):
        canvas.create_oval(x - circle_rad, y - circle_rad, x + circle_rad, y + circle_rad, outline="#fff", tag="graph", fill=node.colour)
        if node.discovery_time is None:
            canvas.create_text(x, y - circle_rad * 2, text=slot["node"].getName(), fill="white", tag="graph")
        elif node.finish_time is None:
            canvas.create_text(x, y - circle_rad * 2, text=str(node.discovery_time)+"|-", fill="white", tag="graph")
        else:
            canvas.create_text(x, y - circle_rad * 2, text=str(node.discovery_time)+"|"+str(node.finish_time), fill="white", tag="graph")


    def drawEdge(self, canvas, edge, x, y, t_x, t_y, adj_x, adj_y):
        if edge.explored == True:
            canvas.create_line(x, y, t_x, t_y, fill="#ff4400", width=3, tag="graph")
        else:
            canvas.create_line(x, y, t_x, t_y, fill="#666", width=2, tag="graph")


    # override the DFS method
    def _doPrep(self):
        # do all of the usual stuff
        super()._doPrep()
        # add a decoration to the edges
        for e in self.graph.getEdges():
             e.explored = False


    # override the DFS method
    def DFSstart(self):
        for vertex in self.vertex_list:
            print("starting new tree")
            if vertex.colour == self.WHITE:
                self.iterators.append(self.DFSvisit(vertex))
                yield self.time


    # override the DFS method
    def DFSvisit(self, vertex):
        self.time += 1
        vertex.discovery_time = self.time
        vertex.colour = self.GRAY
        yield self.time
        for edge in vertex.getAllEdges():
            if edge.explored != True:
                edge.explored = True
                if edge.getEnds()[0] != vertex:
                    if edge.getEnds()[0].colour == self.WHITE:
                        edge.getEnds()[0].pi = vertex
                        self.iterators.append(self.DFSvisit(edge.getEnds()[0]))
                        # yield self.time
                else:
                    if edge.getEnds()[1].colour == self.WHITE:
                        edge.getEnds()[1].pi = vertex
                        self.iterators.append(self.DFSvisit(edge.getEnds()[1]))
                yield self.time
        vertex.colour = self.BLACK
        self.time += 1
        vertex.finish_time = self.time
        yield self.time
