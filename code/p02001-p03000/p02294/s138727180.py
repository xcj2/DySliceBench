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

# def get_distance(s1, s2):
#     #TODO: Define intersect()
#     if insersect(s1, s2):
#         return 0
#     d1 = get_distance_sp(s1, s2.p1)
#     d2 = get_distance_sp(s1, s2.p2)
#     d3 = get_distance_sp(s2, s1.p1)
#     d4 = get_distance_sp(s2, s1.p2)
#     return min(d1, min(d2, min(d3, d4)))

def get_distance_pp(p1, p2):
    return distance(p1 - p2)

def get_distance_lp(l, p):
    return distance(cross(l.p2 - l.p1, p - l.p1)) / distance(l.p2 - l.p1)

def get_distance_sp(s, p):
    if dot(s.p2 - s.p1, p - s.p1) < 0:
        return distance(p - s.p1)
    elif dot(s.p1 - s.p2, p - s.p2) < 0:
        return distance(p - s.p2)
    else:
        return get_distance_lp(s, p)

def ccw(p0, p1, p2):
    EPS = 1e-10
    COUNTER_CLOCKWISE = 1
    CLOCKWISE = -1
    ONLINE_BACK = 2
    ONLINE_FRONT = -2
    ON_SEGMENT = 0
    v1 = p1 - p0
    v2 = p2 - p0
    if cross(v1, v2) > EPS:
        return COUNTER_CLOCKWISE
    elif cross(v1, v2) < -EPS:
        return CLOCKWISE
    elif dot(v1, v2) < -EPS:
        return ONLINE_BACK
    elif norm(v1) < norm(v2):
        return ONLINE_FRONT
    else:
        return ON_SEGMENT

def intersect_p(p1, p2, p3, p4):
    return ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0

def intersect_s(s1, s2):
    return intersect_p(s1.p1, s1.p2, s2.p1, s2.p2)


import sys
# sys.stdin = open('input.txt')

q = int(input())
for i in range(q):
    temp = list(map(int, input().split()))
    points = []
    for j in range(0, 8, 2):
        points.append(Point(temp[j], temp[j+1]))
    s1 = Segment(points[0], points[1])
    s2 = Segment(points[2], points[3])
    if intersect_s(s1, s2):
        print(1)
    else:
        print(0)
