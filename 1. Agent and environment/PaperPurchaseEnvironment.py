import random
from Environment import Environment


class PaperPurchaseEnvironment(Environment):
    prices = [234, 234, 234, 234, 255, 255, 275, 275, 211, 211, 211,
              234, 234, 234, 234, 199, 199, 275, 275, 234, 234, 234, 234, 255,
              255, 260, 260, 265, 265, 265, 265, 270, 270, 255, 255, 260, 260,
              265, 265, 150, 150, 265, 265, 270, 270, 255, 255, 260, 260, 265,
              265, 265, 265, 270, 270, 211, 211, 255, 255, 260, 260, 265, 265,
              260, 265, 270, 270, 205, 255, 255, 260, 260, 265, 265, 265, 265,
              270, 270]
    max_price_addon = 20  # max of random value added to get the final price

    def __init__(self):
        self.time = 0
        self.stock = 20
        self.stock_history = []
        self.price_history = []

    def initial_percepts(self):
        self.stock_history.append(self.stock)
        price = self.prices[0] + random.randrange(self.max_price_addon)
        self.price_history.append(price)
        return {'price': price,
                'instock': self.stock}

    def do(self, action):
        """
        performs the buy action and returns the perception of price and stock
        """
        used = pick_from_dist({6: 0.1, 5: 0.1, 4: 0.2, 3: 0.3, 2: 0.2, 1: 0.1})
        bought = action['buy']
        self.stock = self.stock + bought - used
        self.stock_history.append(self.stock)
        self.time += 1
        price = (self.prices[self.time % len(self.prices)]  # repeating pattern
                 + random.randrange(self.max_price_addon)  # + randomize
                 + self.time // 2)  # + inflation
        self.price_history.append(price)
        return {'price': price,
                'instock': self.stock}


def pick_from_dist(item_prob_dist):
    """
    returns a value from a distribution item_prob_dist - dictionary item:probability, where sum of probabilities = 1
    returns an element selected in proportion to its probability
    """
    ranreal = random.random()
    for (it, prob) in item_prob_dist.items():
        if ranreal < prob:
            return it
        else:
            ranreal -= prob
    raise RuntimeError(str(item_prob_dist) + " is not a probability distribution")
