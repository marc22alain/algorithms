import abc


class Algorithm:

    __metaclass__ = abc.ABCMeta

    operations_count = 0

    @abc.abstractmethod
    def assertValid(self):
        pass


    @abc.abstractmethod
    def doStep(self) -> bool:
        """
        Assuming that there is one loop that drives the algorithm.
        Data structures are in a new state after each step, and we want to see their new state.
        """
        pass


    @abc.abstractmethod
    def doComplete(self):
        """
        For when you just want to get to the end result.
        """
        pass


    @abc.abstractmethod
    def _doPrep(self):
        """
        Assuming that there is some preliminary work that is not of interest to watch occur.
        """
        pass