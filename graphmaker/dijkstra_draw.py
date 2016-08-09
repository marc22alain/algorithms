from dijkstra import Dijkstra

class DijkstraDraw(Dijkstra):
    def __init__(self, graph):
        super(DijkstraDraw, self).__init__(graph)
        self.do_step_message = "Do one Dijkstra step"


    def drawNode(self, canvas, slot, node, x, y, circle_rad):
        canvas.create_oval(x - circle_rad, y - circle_rad, x + circle_rad, y + circle_rad, outline="#fff", tag="graph", fill=node.colour)
        # if node.discovery_time is None:
        #     canvas.create_text(x, y - circle_rad * 2, text=slot["node"].getName(), fill="white", tag="graph")
        # elif node.finish_time is None:
        #     canvas.create_text(x, y - circle_rad * 2, text=str(node.discovery_time)+"|-", fill="white", tag="graph")
        # else:
        canvas.create_text(x, y - circle_rad * 2, text=node.d, fill="white", tag="graph")


    def drawEdge(self, canvas, edge, x, y, t_x, t_y, adj_x, adj_y):
        canvas.create_line(x, y, t_x, t_y, fill="#ff5500", tag="graph")