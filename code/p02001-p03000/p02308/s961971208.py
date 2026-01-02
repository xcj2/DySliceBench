# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_7_D

"""
import sys
from math import sqrt
from sys import stdin
input = stdin.readline


class Point(object):
    epsilon = 1e-10

    def __init__(self, x=0.0, y=0.0):
        if isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

    # ????????????
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(other * self.x, other * self.y)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

    def __eq__(self, other):
        from math import fabs
        if fabs(self.x - other.x) < Point.epsilon and fabs(self.y - other.y) < Point.epsilon:
            return True
        else:
            return False

    def norm(self):
        return self.x * self.x + self.y * self.y

    def __abs__(self):
        return sqrt(self.norm())

    def ccw(self, p0, p1):
        # ??????2???(p0, p1)?????????????????????????????????????????¢????????????
        a = Vector(p1 - p0)
        b = Vector(self - p0)
        if Vector.cross(a, b) > Point.epsilon:
            return 1 # 'COUNTER_CLOCKWISE'
        elif Vector.cross(a, b) < -Point.epsilon:
            return -1 # 'CLOCKWISE'
        elif Vector.dot(a, b) < -Point.epsilon:
            return 2 # 'ONLINE_BACK'
        elif a.norm() < b.norm():
            return -2 # 'ONLINE_FRONT'
        else:
            return 0 # 'ON_SEGMENT'

    def project(self, s):
        # ??????(Point)????????????s??????????????????????????????????????§?¨?(?°???±)????±???????
        base = Vector(s.p2 - s.p1)
        a = Vector(self - s.p1)
        r = Vector.dot(a, base)
        r /= base.norm()
        return s.p1 + base * r

    def reflect(self, s):
        # ??????s???????§°?????¨?????????????????¨???????§°??????????????§?¨?(????°?)????±???????
        proj = self.project(s)
        return self + (proj - self)*2

    def distance(self, s):
        # ????????¨??????s????????¢????¨??????????
        if Vector.dot(s.p2-s.p1, self-s.p1) < 0.0:
            return abs(self - s.p1)
        if Vector.dot(s.p1-s.p2, self-s.p2) < 0.0:
            return abs(self - s.p2)
        return abs(Vector.cross(s.p2-s.p1, self-s.p1) / abs(s.p2-s.p1))


class Vector(Point):
    def __init__(self, x=0.0, y=0.0):
        if isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
        elif isinstance(x, Point):
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y

    # ????????????
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(other * self.x, other * self.y)

    def __truediv__(self, other):
        return Vector(other / self.x, other / self.y)

    @classmethod
    def dot(cls, a, b):
        return a.x * b.x + a.y * b.y

    @classmethod
    def cross(cls, a, b):
        return a.x * b.y - a.y * b.x

    @classmethod
    def is_orthogonal(cls, a, b):
        return Vector.dot(a, b) == 0.0

    @classmethod
    def is_parallel(cls, a, b):
        return Vector.cross(a, b) == 0.0


class Segment(object):
    def __init__(self, p1=Point(), p2=Point()):
        if isinstance(p1, Point):
            self.p1 = p1
            self.p2 = p2
        elif isinstance(p1, tuple):
            self.p1 = Point(p1[0], p1[1])
            self.p2 = Point(p2[0], p2[1])

    def intersect(self, s):
        # ????????¨??????????????????????????????????????????????????????
        ans1 = s.p1.ccw(self.p1, self.p2) * s.p2.ccw(self.p1, self.p2)
        ans2 = self.p1.ccw(s.p1, s.p2) * self.p2.ccw(s.p1, s.p2)
        return ans1 <= 0 and ans2 <= 0

    def cross_point(self, s):
        # ????????¨??????????????????????????????????????§?¨?????±???????
        base = s.p2 - s.p1
        d1 = abs(Vector.cross(base, self.p1-s.p1))
        d2 = abs(Vector.cross(base, self.p2-s.p1))
        t = d1 / (d1 + d2)
        return self.p1 + (self.p2 - self.p1) * t

    def distance(self, s):
        # ????????¨?????????????????????????????¢????±???????
        if self.intersect(s):
            return 0.0
        d1 = s.p1.distance(self)
        d2 = s.p2.distance(self)
        d3 = self.p1.distance(s)
        d4 = self.p2.distance(s)
        return min(d1, d2, d3, d4)


    @classmethod
    def is_orthogonal(cls, s1, s2):
        a = Vector(s1.p2 - s1.p1)
        b = Vector(s2.p2 - s2.p1)
        return Vector.is_orthogonal(a, b)

    @classmethod
    def is_parallel(cls, s1, s2):
        a = Vector(s1.p2 - s1.p1)
        b = Vector(s2.p2 - s2.p1)
        return Vector.is_parallel(a, b)


class Line(Segment):
    pass


class Cirle(object):
    def __init__(self, x, y=Point(), r=1.0):
        if isinstance(x, Point):
            self.c = x
            self.r = y
        elif isinstance(x, tuple):
            self.c = Point(x[0], x[1])
            self.r = r

    def cross_point(self, s):
        pr = self.c.project(s)
        e = (s.p2 - s.p1) / abs(s.p2 - s.p1)
        base = sqrt(self.r * self.r - (pr - self.c).norm())
        return pr + e * base, pr - e * base


def main(args):
    x, y, r = map(int, input().split())
    q = int(input())
    c = Cirle(Point(x, y), r)
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        s = Segment(p1, p2)
        ans1, ans2 = c.cross_point(s)
        if ans1.x < ans2.x:
            print('{:.8f} {:.8f} {:.8f} {:.8f}'.format(ans1.x, ans1.y, ans2.x, ans2.y))
        elif ans1.x == ans2.x and ans1.y <= ans2.y:
            print('{:.8f} {:.8f} {:.8f} {:.8f}'.format(ans1.x, ans1.y, ans2.x, ans2.y))
        else:
            print('{:.8f} {:.8f} {:.8f} {:.8f}'.format(ans2.x, ans2.y, ans1.x, ans1.y))


if __name__ == '__main__':
    main(sys.argv[1:])