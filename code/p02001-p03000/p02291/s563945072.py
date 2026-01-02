import math
from typing import Union


class Point(object):
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float]):
        return Point(self.x * other, self.y * other)

    def __repr__(self):
        return f"({self.x},{self.y})"


class Segment(object):
    __slots__ = ['pt1', 'pt2', 'vector']

    def __init__(self, x: Point, y: Point):
        self.pt1 = x
        self.pt2 = y
        self.vector = self.pt2 - self.pt1

    def dot(self, other):
        return self.vector.x * other.vector.x + self.vector.y * other.vector.y

    def cross(self, other):
        return self.vector.x * other.vector.y - self.vector.y * other.vector.x

    def norm(self):
        return pow(self.vector.x, 2) + pow(self.vector.y, 2)

    def abs(self):
        return math.sqrt(self.norm())

    def projection(self, pt: Point)-> Point:
        t = self.dot(Segment(self.pt1, pt)) / pow(self.abs(), 2)
        return Point(self.pt1.x + t * self.vector.x, self.pt1.y + t * self.vector.y)

    def reflection(self, pt: Point) -> Point:
        return self.projection(pt) * 2 - pt

    def __repr__(self):
        return f"{self.pt1},{self.pt2},{self.vector}"


def main():
    p0_x, p0_y, p1_x, p1_y = map(int, input().split())
    seg = Segment(Point(p0_x, p0_y), Point(p1_x, p1_y))
    num_query = int(input())
    for i in range(num_query):
        pt_x, pt_y = map(int, input().split())
        reflection = seg.reflection(Point(pt_x, pt_y))
        print("{:.10f} {:.10f}".format(reflection.x, reflection.y))
    return


main()
