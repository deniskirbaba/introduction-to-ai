class Agent(object):
    def __init__(self, env):
        self.env = env

    def go(self, n):
        """
        agent acts during n time steps
        """
        raise NotImplementedError("go")  # abstract method
