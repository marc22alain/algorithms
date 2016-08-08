


class OpCounter(object):
    """ For composing algorithms and data structures that account for their
	time complexity."""
    def __init__(self):
        self.operations_count = 0


    def getTimeComplexity(self):
        return self.operations_count


    def addOpCount(self, num):
        self.operations_count += num


    def reset(self):
        self.operations_count = 0
