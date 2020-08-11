import random

# Generate random points
class Point():
    def __init__(self, x_=None, y_=None):
        if x_ and y_ is not None:
            self.x = x_
            self.y = y_
        else:
            self.x, self.y = random.randrange(-50, 50, 1), random.randrange(-50, 50, 1)

            if (self.x >= self.y):
                self.label = 1
            else:
                self.label = -1
