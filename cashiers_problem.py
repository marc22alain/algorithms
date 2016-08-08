"""
Cashier's problem is to find the least number of coins to give correct change.
The big wrinkle in the problem is that greedy strategy does not work well for all coin denomination sets.
Greedy works for {1, 5, 10, 25}, but not for {1, 8, 10}
"""

from algorithm import Algorithm

from opcounter import OpCounter

class CashiersProblemGreedy(Algorithm, OpCounter):
    def __init__(self, coin_list):
        super(CashiersProblemGreedy, self).__init__()
        self.coin_list = sorted(coin_list, reverse=True)


    def _doPrep(self):
        self.change = {}
        for i in xrange(len(self.coin_list)):
            self.change[self.coin_list[i]] = 0


    def assertValid(self):
        return "not implemented yet"


    def doStep(self):
        return "not implemented yet"


    def doComplete(self, change_owed):
        self._doPrep()
        for i in xrange(len(self.coin_list)):
            while change_owed - self.coin_list[i] >= 0:
                # add three counts for a successful comparison and two math ops
                self.addOpCount(3)
                change_owed = change_owed - self.coin_list[i]
                self.change[self.coin_list[i]] += 1
            # add one count for a failed comparison
            self.addOpCount(1)
        return self.change, self.operations_count


    def __str__(self):
        text = "operation count = %s\n" % self.operations_count
        text += "on coin list " + str(self.coin_list)
        return text




class CashiersProblemMemoed(CashiersProblemGreedy):
    """Just need to override the standard methods.
    Hoping that I don't EVER change anything in CashiersProblemGreedy!
    *** !!!!! ***
    """

    def __init__(self, coin_list):
        super(CashiersProblemMemoed, self).__init__(coin_list)
        self.change_owed = 0


    def _doPrep(self):
        self.M = [{"num_coins":0} for i in xrange(self.change_owed + 1)]
        # for i in xrange(self.change_owed + 1):
        #     self.M[i] = {"num_coins":0}


    def doComplete(self, change_owed):
        self.change_owed = change_owed
        self._doPrep()
        for i in xrange(self.change_owed + 1):
            self.recurrence(i)


    def recurrence(self, amount):
        # recurrence is change = coin + M[change - coin];
        # M holds the number of coins and thta is what is to be minimized
        if amount == 0:
            return
        else:
            min_coins = float("inf")
            for i in xrange(len(self.coin_list)):
                sub = amount - self.coin_list[i]
                if sub >= 0:
                    if 1 + self.M[sub]["num_coins"] < min_coins:
                        min_coins = 1 + self.M[sub]["num_coins"]
        self.M[amount]["num_coins"] = min_coins
        return



class CashiersProblemRecursive(CashiersProblemGreedy):
    """Just need to override the standard methods.
    Hoping that I don't EVER change anything in CashiersProblemGreedy!
    *** !!!!! ***
    """

    def __init__(self, coin_list):
        super(CashiersProblemRecursive, self).__init__(coin_list)


    def doComplete(self, change_owed):
        return self.recursion(change_owed)


    def recursion(self, change_owed):
    	if change_owed == 0:
    		return 0
        min_coins = float("inf")
        # for all coins
        for i in xrange(len(self.coin_list)):
        	# try subtracting that coin increment
            sub = change_owed - self.coin_list[i]
            if sub >= 0:
            	sub_coins = self.recursion(sub)
                if (1 + sub_coins) < min_coins:
                    min_coins = (1 + sub_coins)
        return min_coins


l1 = [1,10,8]
l2 = [1,5,10,25]

c = CashiersProblemMemoed(l1)

print c

change = c.doComplete(17)
print c.M

print
c2 = CashiersProblemRecursive(l1)
print c2.doComplete(17)