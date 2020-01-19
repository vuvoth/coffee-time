# f(x) = x^21 - x + 5 + 6sin(x)
# find local minimum of f(x)

from math import *


def f(x):
    return x*x - x + 5 + 6 * sin(x)


def derivative(x):
    return 2 * x - 1 + 6 * cos(x)


def gradent_descent(x0, alpha):
    for it in range(1, 100):
        x = x0 - alpha * derivative(x0)
        x0 = x
        # print(x0)
        if (fabs(derivative(x0)) < 1e-6):
            return (x0, it)
    return (x0, 100)


def train(x0, alpha):
    (x1, it) = gradent_descent(x0, alpha)
    print("Solution x0 = %f cost = %f start at x0 = %f obtained after %d with learn rate = %f" %
          (x1, f(x1), x0, it, alpha))


if __name__ == "__main__":
    train(6, 0.1)
    train(-10, 0.7)
    train(10, 0.1)
    train(4, 0.1)
    train(3, 0.1)
    train(-1, 0.1)
    train(-10, 0.1)
    train(1, 0.2)
