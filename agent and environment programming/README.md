# Realization of a paper buying agent. #

The agent observes the world and performs actions in the environment, he also has an internal state, which he
updates.
The agent does not have access to the pricing model, but can only observe the current price and quantity of the goods for
warehouse. He must decide how much to buy.
An agent's state of belief is an estimate of the average price of the paper and the total amount of money that the agent
spent.

The environment accepts the actions of agents, updates its internal state and returns perceptions.
