import random


def cost(a, x):
    ans = 0
    for i in range(len(a)):
        ans += x[i] * a[i]
    return ans


if __name__ == "__main__":
    a = [2, 4]
    for i in range(50):

        x0 = random.randint(0, 600)
        print(x0, cost(a, [1, x0]) + random.randint(0, 4))
