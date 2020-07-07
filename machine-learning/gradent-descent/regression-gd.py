import math
import matplotlib.pyplot as pl


def cost(a, x):
    ans = 0
    for i in range(len(a)):
        if (i == 0):
            ans += a[i]
        else:
            ans += x[i - 1] * a[i]
    return ans

def lossFunction(X, Y, h):
    loss = 0.0
    m = len(X)
    for i in range(m):
        loss += ((cost(h, X[i]) - Y[i]) ** 2) / m * 1.0
    return loss


def derivative(X, Y, h, i_th):
    e = 1e-6
    old_h = h
    old_h[i_th] += e
    pos = lossFunction(X, Y, old_h)
    # print(old_h)
    old_h = h
    old_h[i_th] -= 2 * e
    # print(old_h)

    neg = lossFunction(X, Y, old_h)
    # print(pos, neg)
    old_h[i_th] += e

    # print((pos - neg) / (2 * e))
    return (pos - neg) / (2 * e)


def train(X, Y, h, numberIt, alpha):
    for it in range(numberIt):
        old_h = h
        # print("lossfunction %f" % (lossFunction(X, Y, h)))
        H = []
        for i in range(len(h)):
            g = derivative(X, Y, old_h, i)
            H.append(old_h[i] - alpha * g)
        # print(" ", h)

        h = H
    return (h, numberIt)


def train02(X, Y, h, numberIt, alpha):
    for it in range(numberIt):
        m = len(X)
        g0 = 0
        g1 = 0
        for i in range(m):
            g0 += alpha * (cost(h, X[i]) - Y[i])
            g1 += alpha * (cost(h, X[i]) - Y[i]) * X[i]
        h[0] -= g0 / m
        h[1] -= g1 / m
    return (h, numberIt)


if __name__ == "__main__":
    X = []
    Y = []
    # X.append(2)
    # Y.append(6)
    f = open("dataset.txt", "r")
    raw_data = f.readlines()
    for line in raw_data:
        x0, y = map(int, line.split(" "))
        X.append([x0])
        Y.append(y)

    h = [0, 0]
    (h, it) = train(X, Y, h, 100000,  1e-5)
    print("answer = ", h)
    print("lost cost = ", lossFunction(X, Y, h))

    pl.scatter(X, Y)
    Y_predict = []
    for x in X:
        Y_predict.append(cost(h, x))
    pl.plot(X, Y_predict, '-r', label='model ' +
            str(h[0]) + " + " + str(h[1]) + "x")
    pl.title('Model')
    pl.xlabel('x', color='#1C2833')
    pl.ylabel('y', color='#1C2833')
    pl.grid()
    pl.show()
