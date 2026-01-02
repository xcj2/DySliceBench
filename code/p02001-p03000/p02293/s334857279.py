import math


class Point:
    EPS = 1 << 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return Point(self.x*other.x, self.y*other.y)

    def __floordiv__(self, other):
        return Point(self.x/other.x, self.y/other.y)

    def __abs__(self):
        return math.sqrt(self.norm())

    def norm(self):
        return self.x**2 + self.y**2

    def __eq__(self, other):
        EPS = self.__class__.EPS
        return abs(self.x-other.x) < EPS and abs(self.x-other.x) < EPS


class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def cross(self, other):
        return self.x*other.y - self.y*other.x

    def isOrthogonal(self, a, b):
        return a.dot(b) == 0.0

    def isParallel(self, a, b):
        return a.cross(b) == 0.0

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return Vector(self.x*other.x, self.y*other.y)

    def __floordiv__(self, other):
        return Vector(self.x/other.x, self.y/other.y)


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def isOrthogonal(s1, s2):
        return (s1.p2-s1.p1).dot(s2.p2-s2.p1) == 0.0

    def isParallel(s1, s2):
        return (s1.p2-s1.p1).cross(s2.p2-s2.p1) == 0.0


class Line(Segment):
    pass


class Circle:
    def __init__(self, c, r):
        self.c = c
        self.r = r


class Polygon:
    def __init__(self, *points):
        self.points = points


n = int(input())
for i in range(n):
    q = list(map(int, input().split()))
    s = []
    for j in range(2):
        p0 = Vector(*q[j*4:j*4+2])
        p1 = Vector(*q[j*4+2:j*4+4])
        s.append(Segment(p0, p1))
    if Segment.isOrthogonal(*s):
        print(1)
    elif Segment.isParallel(*s):
        print(2)
    else:
        print(0)

