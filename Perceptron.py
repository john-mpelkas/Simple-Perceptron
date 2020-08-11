import numpy as np
import math
#Activation function
def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

class Perceptron():
    def __init__(self):
        seed = [-1, 1]
        self.weights = [np.random.choice(seed), np.random.choice(seed)]
        self.lr = 0.25

# Perceptron Guess
    def guess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        output = sign(sum)
        return (output)

# Adjusting weights
    def train(self, inputs, label):
        guess = self.guess(inputs)
        error = label - guess
        for i in range(len(self.weights)):
             self.weights[i] += error * inputs[i]
