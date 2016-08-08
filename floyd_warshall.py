from graph_algorithm import GraphAlgorithm



class FloydWarshall(GraphAlgorithm):
    def __init__(self, graph):
        super(FloydWarshall, self).__init__(graph)
        self.A = set()

    # def _doPrep(self):
        # must set up a look-up table and put in the inputted edges 
        # 3D table makes for significant memory requirement !    n^3 data points
        # and one more for holding the parents; what does that one looks like ?



