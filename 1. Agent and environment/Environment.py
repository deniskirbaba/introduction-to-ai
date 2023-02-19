from Displayable import Displayable


class Environment(Displayable):
    """
    Environment take agent's actions, update their inner state and returns the next perception.
    """

    def initial_percepts(self):
        """
        returns initial percepts for agent
        """
        raise NotImplementedError("initial_percepts")  # abstract method

    def do(self, action):
        """
        performs an action in the environment, returns the next perception
        """
        raise NotImplementedError("do")  # abstract method
