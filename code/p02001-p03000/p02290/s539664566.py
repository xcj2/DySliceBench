import math

def equals(a, b):
    return abs(a - b) < 1e-10


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


def project(s, p):
    base = s.p2 - s.p1
    r = dot(p - s.p1, base) / base.norm()
    return s.p1 + base * r


if __name__ == '__main__':
    x1, y1, x2, y2 = [int(v) for v in input().split()]
    s = Segment(Point(x1, y1), Point(x2, y2))
    q = int(input())
    ans = []
    for i in range(q):
        x, y = [int(v) for v in input().split()]
        p = Point(x, y)
        ans.append(project(s, p))

    for v in ans:
        print('{0:.10f} {1:.10f}'.format(v.x, v.y))
