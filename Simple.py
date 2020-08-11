from Perceptron import Perceptron
from Points import Point
import matplotlib.pyplot as plt

trainPoints = []
testPoints = []
P = Perceptron()

def f(x):
    # y = mx + b
    return(x + 2)

# Generate training Data points
for i in range(300):
    trainp = Point()
    trainPoints.append((trainp.x, trainp.y, trainp.label))

# Generate testing Data Points
for i in range(100):
    testp = Point()
    testPoints.append((testp.x, testp.y, testp.label))

# Training
for data in trainPoints:
    px, py, label = data
    point = (px,py)

    #Comment line out to plot untrained perceptron
    #P.train(point, label)

# Guessing
for data in testPoints:
    px, py, label = data
    point = (px,py)
    guess = P.guess(point)

# If Guess is right plot point in Green Else plot in Red
    if guess == label:
        plt.plot(px, py, '-or', color='green')
    else:
        plt.plot(px, py, '-or', color='red')

## TODO: Create line in which all points below are -1 (Off)
## All points above are 1 (on)
# intercepts= (-50, f(50))
#
# print (intercepts)
# plt.plot(range(50),  'or')

plt.show()
