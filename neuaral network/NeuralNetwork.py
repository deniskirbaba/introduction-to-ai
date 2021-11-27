import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x - x**2


class NeuralNetwork:
    def __init__(self, x, y, number_of_hidden_neurons):
        self.input = x
        self.weights1 = np.random.rand(number_of_hidden_neurons, self.input.shape[0])
        self.weights2 = np.random.rand(1, number_of_hidden_neurons)
        self.b1 = np.random.rand(number_of_hidden_neurons, 1)
        self.b2 = np.random.rand(y.shape[0], 1)
        self.y = y
        self.output = np.zeros(y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.weights1, self.input) + self.b1)
        self.output = sigmoid(np.dot(self.weights2, self.layer1) + self.b2)
        print(self.output)

    def backprop(self, learning_rate):
        # application of the chain rule to find derivative of the loss function
        d_weights2 = learning_rate * np.dot(-2 * (self.y - self.output) * sigmoid_derivative(self.output), self.layer1.T)
        d_weights1 = learning_rate * np.dot(np.dot(np.dot(-2 * (self.y - self.output) * sigmoid_derivative(self.output), sigmoid_derivative(self.layer1).T), self.weights2.T), self.input.T)
        d_b2 = learning_rate * -2 * (self.y - self.output) * sigmoid_derivative(self.output)
        d_b1 = learning_rate * np.dot(np.dot(-2 * (self.y - self.output) * sigmoid_derivative(self.output), sigmoid_derivative(self.layer1).T), self.weights2.T)
        # update the weight with the derivative (slope) of the loss function
        self.weights1 -= d_weights1
        self.weights2 -= d_weights2
        self.b1 -= d_b1
        self.b2 -= d_b2


def main():
    nn = NeuralNetwork(np.array(np.mat('0; 0; 1')), np.array(np.mat('0')), 4)
    nn.feedforward()
    nn.backprop(1)


if __name__ == "__main__":
	main()