n, k = [int(i) for i in input().split()]

# Create the pascal triangle
pascal = [[0 for i in range(j+1)] for j in range(2001)]
pascal[0][0] = 1
for i in range(2000):
    for j in range(i+1):
        pascal[i+1][j] += pascal[i][j]
        pascal[i+1][j+1] += pascal[i][j]


class Mod(object):
    def __init__(self, base):
        self.base = base
        self.x = 0

    def add(self, y):
        self.x += y % self.base
        self.x %= self.base

    def sub(self, y):
        self.x -= y % self.base
        self.x %= self.base

    def mul(self, y):
        self.x *= y % self.base
        self.x %= self.base


def comb(x, y):
    if x < y or (x == 0 and y != 0) or y < 0:
        return 0
    return pascal[x][y]


def f2(x, y):
    return comb(x+y-1, y-1)


def f(x, y):
    if x == 0 and y == 0:
        return 1
    return f2(x-y, y)


if __name__ == "__main__":
    BASE = int(1e+9 + 7)
    for i in range(1, k+1):
        count = Mod(BASE)
        count.add(f(k, i) * f(n-k, i-1))
        count.add(f(k, i) * f(n-k, i))
        count.add(f(k, i) * f(n-k, i))
        count.add(f(k, i) * f(n-k, i+1))
        print(count.x)
