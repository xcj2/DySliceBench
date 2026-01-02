from sys import stdin
import math

class Vector:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

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

class Circle:
    def __init__(self, c=Point(0, 0), r=1):
        self.c = c
        self.r = r

def project(s, p):
    base = s.p2 - s.p1
    hypo = p - s.p1
    r = hypo.dot(base) / base.norm()
    return s.p1 + base * r

def get_cross_point(c, l):
    pr = project(l, c.c)
    e = (l.p1- l.p2) / (l.p2 - l.p1).abs()
    base = math.sqrt( c.r * c.r - (pr - c.c).norm() )
    return pr + e * base, pr - e * base

def read_and_print_results(n, c):
    for _ in range(n):
        line = stdin.readline().strip().split()
        p0 = Vector(int(line[0]), int(line[1]))
        p1 = Vector(int(line[2]), int(line[3]))
        l = Line(p0, p1)
        p2, p3 = get_cross_point(c, l)
        x1, y1 = min((p2.x, p2.y), (p3.x, p3.y))
        x2, y2 = max((p2.x, p2.y), (p3.x, p3.y))
        print("{0:0.8f} {1:0.8f} {2:0.8f} {3:0.8f}".format(x1, y1, x2, y2))

x, y, r = [ int(i) for i in input().split() ]
c = Circle(Point(x, y), r)
n = int(input())
read_and_print_results(n, c)
