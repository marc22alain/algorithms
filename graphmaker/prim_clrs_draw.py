from prim_clrs import PrimCLRS


class PrimCLRSDraw(PrimCLRS):

    do_step_message = "Do one CLRS Prim step"

    def __init__(self, graph):
        super().__init__(graph)

    def drawNode(self, canvas, slot, node, x, y, circle_rad):
        canvas.create_oval(x - circle_rad, y - circle_rad, x + circle_rad, y + circle_rad, outline="#fff", tag="graph")
        canvas.create_text(x, y - circle_rad * 2, text=node.key, fill="white", tag="graph")


    def drawEdge(self, canvas, edge, x, y, t_x, t_y, adj_x, adj_y):
        u, v = edge.getEnds()
        if (u.pi == v) or (v.pi == u):
            canvas.create_line(x, y, t_x, t_y, fill="#ff5500", tag="graph")
            canvas.create_text(((x + t_x) / 2) + adj_x, ((y + t_y) / 2) - adj_y, text=edge.getWeight(), fill="#ff5500", tag="graph")
        else:
            canvas.create_line(x, y, t_x, t_y, fill="#333", tag="graph")
            canvas.create_text(((x + t_x) / 2) + adj_x, ((y + t_y) / 2) - adj_y, text=edge.getWeight(), fill="#333", tag="graph")

