from kruskal import Kruskal

class KruskalDraw(Kruskal):
    def __init__(self, graph):
        super(KruskalDraw, self).__init__(graph)
        self.do_step_message = "Do one Kruskal step"


    def drawNode(self, canvas, slot, node, x, y, circle_rad):
        canvas.create_oval(x - circle_rad, y - circle_rad, x + circle_rad, y + circle_rad, outline="#fff", tag="graph")
        canvas.create_text(x, y - circle_rad * 2, text=slot["node"].getName(), fill="white", tag="graph")


    def drawEdge(self, canvas, edge, x, y, t_x, t_y, adj_x, adj_y):
        if edge.included == True:
            canvas.create_line(x, y, t_x, t_y, fill="#ff5500", tag="graph")
            canvas.create_text(((x + t_x) / 2) + adj_x, ((y + t_y) / 2) - adj_y, text=edge.getWeight(), fill="#ff5500", tag="graph")
        else:
            canvas.create_line(x, y, t_x, t_y, fill="#333", tag="graph")
            canvas.create_text(((x + t_x) / 2) + adj_x, ((y + t_y) / 2) - adj_y, text=edge.getWeight(), fill="#333", tag="graph")
