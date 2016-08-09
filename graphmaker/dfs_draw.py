from dfs import DFS

class DFSdraw(DFS):
    def __init__(self, graph):
        super(DFSdraw, self).__init__(graph)
        self.do_step_message = "Do one DFS step"


    def drawNode(self, canvas, slot, node, x, y, circle_rad):
        canvas.create_oval(x - circle_rad, y - circle_rad, x + circle_rad, y + circle_rad, outline="#fff", tag="graph", fill=node.colour)
        if node.discovery_time is None:
            canvas.create_text(x, y - circle_rad * 2, text=slot["node"].getName(), fill="white", tag="graph")
        elif node.finish_time is None:
            canvas.create_text(x, y - circle_rad * 2, text=str(node.discovery_time)+"|-", fill="white", tag="graph")
        else:
            canvas.create_text(x, y - circle_rad * 2, text=str(node.discovery_time)+"|"+str(node.finish_time), fill="white", tag="graph")


    def drawEdge(self, canvas, x, y, t_x, t_y, adj_x, adj_y):
        canvas.create_line(x, y, t_x, t_y, fill="#ff5500", tag="graph")