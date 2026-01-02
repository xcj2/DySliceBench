class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __sub__(self, p):
        x_sub = self.x - p.x
        y_sub = self.y - p.y
        return Point(x_sub, y_sub)

class Vector:
    def __init__(self, p):
        self.x = p.x
        self.y = p.y
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

def cross(v1, v2):
    return v1.x * v2.y - v1.y * v2.x

def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

def ccw(p0, p1, p2):
    a = Vector(p1 - p0)
    b = Vector(p2 - p0)
    cross_ab = cross(a, b)
    if cross_ab > 0:
        return 1
    elif cross_ab < 0:
        return -1
    elif dot(a, b) < 0:
        return 1
    elif a.norm() < b.norm():
        return -1
    else:
        return 0

def intersect(p1, p2, p3, p4):
    if (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0) and \
       (ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0):
        print('1')
    else:
        print('0')

import sys

file_input = sys.stdin

sq = file_input.readline()

for line in file_input:
    x_p0, y_p0, x_p1, y_p1, x_p2, y_p2, x_p3, y_p3 = map(int, line.split())
    p0 = Point(x_p0, y_p0)
    p1 = Point(x_p1, y_p1)
    p2 = Point(x_p2, y_p2)
    p3 = Point(x_p3, y_p3)
    intersect(p0, p1, p2, p3)