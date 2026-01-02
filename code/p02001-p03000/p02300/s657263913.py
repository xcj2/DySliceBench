from sys import stdin
import math
from collections import deque

EPS = 1e-10

class Vector:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # can't  apply "number * Vector" but "Vector * number"
    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __truediv__(self, k):
        return Vector(self.x / k, self.y / k)

    def __gt__(self, other):
        return self.x > other.x and self.y > other.yb

    def __lt__(self, other):
        return self.x < other.x and self.y < other.yb

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # usually cross operation return Vector but it returns scalor
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def norm(self):
        return self.x * self.x + self.y * self.y

    def abs(self):
        return math.sqrt(self.norm())

    def rotate(self, theta):
        return Vector(self.x * math.cos(theta)
                               - self.y * math.sin(theta),
                               self.x * math.sin(theta)
                               + self.y * math.cos(theta))

class Point(Vector):
    def __init__(self, *args, **kargs):
        return super().__init__(*args, **kargs)

class Segment:
    def __init__(self, p1=Point(0, 0), p2=Point(1, 1)):
        self.p1 = p1
        self.p2 = p2

class Line(Segment):
    def __init__(self, *args, **kargs):
        return super().__init__(*args, **kargs)

def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    if a.cross(b) > EPS:
        return 1
    elif a.cross(b) < -EPS:
        return -1
    elif a.dot(b) < -EPS:
        return 2
    elif a.norm() < b.norm():
        return -2
    else:
        return 0

def convex_hull(P):
    n = len(P)
    A = sorted(P, key=lambda p: (p.x, p.y))
    U = deque([])
    L = deque([])
    for i in range(n):
        if i < 2:
            U.append(A[i])
        else:
            while ccw(U[-2], U[-1], A[i]) == 1:
                U.pop()
                if len(U) == 1:
                    break
            U.append(A[i])

    for i in range(n-1, -1, -1):
        if i > n-3:
            L.append(A[i])
        else:
            while ccw(L[-2], L[-1], A[i]) == 1:
                L.pop()
                if len(L) == 1:
                    break
            L.append(A[i])

    U.pop()
    U.popleft()
    return U + L

def read_polygon(n):
    P = []
    for _ in range(n):
        line = stdin.readline().strip().split()
        p = Vector(int(line[0]), int(line[1]))
        P.append(p)
    return P

def __main():
    n = int(input())
    P = read_polygon(n)
    P_rev = convex_hull(P)
    while min(P_rev, key=lambda p: (p.y, p.x)) != P_rev[-1]:
        P_rev.appendleft(P_rev.pop())
    print(len(P_rev))
    for i in reversed(P_rev):
        print("{0} {1}".format(i.x, i.y))

if __name__ == '__main__':
    __main()
