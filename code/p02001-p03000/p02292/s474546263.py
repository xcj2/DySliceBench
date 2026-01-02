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
    a = p1 - p0
    b = p2 - p0
    if cross(a, b) > EPS:
        return 'COUNTER_CLOCKWISE'
    if cross(a, b) < -EPS:
        return 'CLOCKWISE'
    if dot(a, b) < -EPS:
        return 'ONLINE_BACK'
    if a.norm() < b.norm():
        return 'ONLINE_FRONT'
    return 'ON_SEGMENT'


if __name__ == '__main__':
    x0, y0, x1, y1 = [int(v) for v in input().split()]
    p0 = Point(x0, y0)
    p1 = Point(x1, y1)
    q = int(input())
    ans = []
    for i in range(q):
        x2, y2 = [int(v) for v in input().split()]
        p2 = Point(x2, y2)
        ans.append(ccw(p0, p1, p2))

    for v in ans:
        print(v)
