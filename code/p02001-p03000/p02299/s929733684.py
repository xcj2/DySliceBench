import math

EPS = 1e-10

def equals(a, b):
    return abs(a - b) < EPS


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, a):
        return Point(self.x * a, self.y * a)

    def __rmul__(self, a):
        return self * a

    def __truediv__(self, a):
        return Point(self.x / a, self.y / a)

    def norm(self):
        return self.x * self.x + self.y * self.y

    def abs(self):
        return math.sqrt(self.norm())

    def __lt__(self, p):
        if self.x != p.x:
            return self. x < p.x
        else:
            return self.y < p.y

    def __eq__(self, p):
        return equals(self.x, p.x) and equals(self.y, p.y)


def dot(a, b):
    return a.x * b.x + a.y * b.y


def cross(a, b):
    return a.x * b.y - a.y * b.x


def contains(g, p):
    n = len(g)
    isIn = False
    for i in range(n):
        a = g[i] - p
        b = g[(i + 1) % n] - p
        if abs(cross(a, b)) < EPS and dot(a, b) < EPS:
            return 1
        if a.y > b.y:
            a, b = b, a
        if a.y < EPS and EPS < b.y and cross(a, b) > EPS:
            isIn = not isIn
    if isIn:
        return 2
    else:
        return 0


if __name__ == '__main__':
    n = int(input())
    g = []
    for i in range(n):
        x, y =  [int(v) for v in input().split()]
        g.append(Point(x, y))

    q = int(input())
    ans = []
    for i in range(q):
        x, y =  [int(v) for v in input().split()]
        ans.append(contains(g, Point(x, y)))

    for v in ans:
        print(v)
