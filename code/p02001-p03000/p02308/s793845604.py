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


class Circle:
    def __init__(self, c=Point(), r=0):
        self.c = c
        self.r = r


def dot(a, b):
    return a.x * b.x + a.y * b.y


def cross(a, b):
    return a.x * b.y - a.y * b.x


def project(s, p):
    base = s.p2 - s.p1
    r = dot(p - s.p1, base) / base.norm()
    return s.p1 + base * r


def getCrossPoint(c, l):
    pr = project(l, c.c)
    e = (l.p2 - l.p1) / (l.p2 - l.p1).abs()
    base = math.sqrt(c.r * c.r - (pr - c.c).norm())
    return (pr + e * base, pr - e * base)


if __name__ == '__main__':
    cx, cy, r =  [int(v) for v in input().split()]
    c = Circle(Point(cx, cy), r)
    q = int(input())
    ans = []
    for i in range(q):
        x1, y1, x2, y2 = [int(v) for v in input().split()]
        l = Segment(Point(x1, y1), Point(x2, y2))
        v1, v2 = getCrossPoint(c, l)
        if v2 < v1:
            v1, v2 = v2, v1
        ans.append([v1.x, v1.y, v2.x, v2.y])

    for v in ans:
        print('{0[0]:.8f} {0[1]:.8f} {0[2]:.8f} {0[3]:.8f}'.format(v))
