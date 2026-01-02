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


def ccw(p0, p1, p2):
    COUNTER_CLOCKWISE = 1
    CLOCKWISE = -1
    ONLINE_BACK = 2
    ONLINE_FRONT = -2
    ON_SEGMENT = 0
    a = p1 - p0
    b = p2 - p0
    if cross(a, b) > EPS:
        return COUNTER_CLOCKWISE
    if cross(a, b) < -EPS:
        return CLOCKWISE
    if dot(a, b) < -EPS:
        return ONLINE_BACK
    if a.norm() < b.norm():
        return ONLINE_FRONT
    return ON_SEGMENT


def intersect(s1, s2):
    p1 = s1.p1
    p2 = s1.p2
    p3 = s2.p1
    p4 = s2.p2
    return (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and
            ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)


def getDistanceLP(l, p):
    v = l.p2 - l.p1
    return abs(cross(v, p - l.p1) / v.abs())


def getDistanceSP(s, p):
    if dot(s.p2 - s.p1, p - s.p1) < 0:
        v = p - s.p1
        return v.abs()
    if dot(s.p1 - s.p2, p - s.p2) < 0:
        v = p - s.p2
        return v.abs()
    return getDistanceLP(s, p)


def getDistance(s1, s2):
    if intersect(s1, s2):
        return 0
    return min(
        getDistanceSP(s1, s2.p1),
        getDistanceSP(s1, s2.p2),
        getDistanceSP(s2, s1.p1),
        getDistanceSP(s2, s1.p2)
    )


if __name__ == '__main__':
    q = int(input())
    ans = []
    for i in range(q):
        x0, y0, x1, y1, x2, y2, x3, y3 = [int(v) for v in input().split()]
        s1 = Segment(Point(x0, y0), Point(x1, y1))
        s2 = Segment(Point(x2, y2), Point(x3, y3))
        ans.append(getDistance(s1, s2))

    for v in ans:
        print('{0:.10f}'.format(v))
