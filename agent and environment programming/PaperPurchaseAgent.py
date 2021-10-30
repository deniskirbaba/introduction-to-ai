from Agent import Agent


class PaperPurchaseAgent(Agent):
    def __init__(self, env):
        self.env = env
        self.spent = 0
        percepts = env.initial_percepts()
        self.ave = self.last_price = percepts['price']  # estimate of the average price of a paper
        self.instock = percepts['instock']

    def go(self, n):
        for i in range(n):
            if self.last_price < 0.9 * self.ave and self.instock < 60:
                tobuy = 48
            elif self.instock < 12:
                tobuy = 12
            else:
                tobuy = 0
            self.spent += tobuy * self.last_price
            percepts = self.env.do({'buy': tobuy})
            self.last_price = percepts["price"]
            self.ave = self.ave + (self.last_price - self.ave) * 0.05
            self.instock = percepts["instock"]
