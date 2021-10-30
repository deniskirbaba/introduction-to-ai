import matplotlib.pyplot as plt


class PlotPrices(object):
    """
    set up a graph for the history of prices and quantities in stock
    """
    def __init__(self, ag, env):
        self.ag = ag
        self.env = env
        #plt.ion()
        plt.xlabel("time")
        plt.ylabel("stock                                  price")

    def plot_run(self):
        num = len(self.env.stock_history)
        plt.plot(range(num), self.env.stock_history)
        plt.plot(range(num), self.env.price_history)
        plt.show()
