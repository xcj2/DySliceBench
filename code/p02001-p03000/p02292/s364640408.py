import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)
    def __floordiv__(self, other):
        return Point(self.x / other, self.y / other)
    def __repr__(self):
        return str(self.x) + ' ' + str(self.y)

class Vector(Point):
    pass

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Segment(Line):
    pass

def points_to_vector(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return Vector(x, y)

def vector(p):
    return Vector(p.x, p.y)

def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

def cross(v1, v2):
    return v1.x * v2.y - v1.y * v2.x

def norm(v):
    return v.x**2 + v.y**2

def distance(v):
    return math.sqrt(norm(v))

def project(s, p):
    base = points_to_vector(s.p1, s.p2)
    hypo = points_to_vector(p, s.p1)
    r = dot(hypo, base) / norm(base)
    return s.p1 + base * r

def reflect(s, p):
    return p + (project(s, p) -p) * 2

def ccw(p0, p1, p2):
    EPS = 1e-10
    v1 = p1 - p0
    v2 = p2 - p0
    if cross(v1, v2) > EPS:
        return 'COUNTER_CLOCKWISE'
    elif cross(v1, v2) < -EPS:
        return 'CLOCKWISE'
    elif dot(v1, v2) < -EPS:
        return 'ONLINE_BACK'
    elif norm(v1) < norm(v2):
        return 'ONLINE_FRONT'
    else:
        return 'ON_SEGMENT'

import sys
# sys.stdin = open('input.txt')

temp = list(map(int, input().split()))
p0 = Point(temp[0], temp[1])
p1 = Point(temp[2], temp[3])
q = int(input())
for i in range(q):
    x, y = map(int, input().split())
    p2 = Point(x, y)
    print(ccw(p0, p1, p2))

