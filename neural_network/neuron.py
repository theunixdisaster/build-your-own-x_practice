import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)

def mse(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, x):
        activation_input = np.dot(x, self.weights) + self.bias
        return sigmoid(activation_input)


if __name__ == "__main__":
    w = np.array([0, 1])
    b = 4
    x = np.array([2, 3])

    n = Neuron(w, b)
    val = n.feedforward(x)
    print(val)
