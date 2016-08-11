import abc


class Algorithm(metaclass=abc.ABCMeta):

    # __metaclass__ = abc.ABCMeta

    operations_count = 0

    has_terminated = False

    @abc.abstractmethod
    def assertValid(self):
        pass


    @abc.abstractmethod
    def doStep(self):
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


    def hasTerminated(self) -> bool:
        """
        Returns whether the algorithm has terminated.
        """
        return self.has_terminated


    @abc.abstractmethod
    def _checkTermination(self):
        """
        Useful when the algorithm is run with doStep(), the algorithm will evaluate whether
        it has terminated, and update the 'is_complete' attribute if required.
        """
        pass
