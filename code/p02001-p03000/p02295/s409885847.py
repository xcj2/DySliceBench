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


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def dot(a, b):
    return a.x * b.x + a.y * b.y


def cross(a, b):
    return a.x * b.y - a.y * b.x


def getCrossPoint(s1, s2):
    base = s2.p2 - s2.p1
    d1 = abs(cross(base, s1.p1 - s2.p1))
    d2 = abs(cross(base, s1.p2 - s2.p1))
    t = d1 / (d1 + d2)
    return s1.p1 + (s1.p2 - s1.p1) * t


if __name__ == '__main__':
    q = int(input())
    ans = []
    for i in range(q):
        x0, y0, x1, y1, x2, y2, x3, y3 = [int(v) for v in input().split()]
        s1 = Segment(Point(x0, y0), Point(x1, y1))
        s2 = Segment(Point(x2, y2), Point(x3, y3))
        ans.append(getCrossPoint(s1, s2))

    for v in ans:
        print('{0:.10f} {1:.10f}'.format(v.x, v.y))
