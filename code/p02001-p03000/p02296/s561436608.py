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

    def norm(self):
        return pow(self.x, 2) + pow(self.y, 2)

    def abs(self):
        return math.sqrt(self.norm())

    def __repr__(self):
        return f"({self.x},{self.y})"


class Vector(Point):
    __slots__ = ['x', 'y', 'pt1', 'pt2']

    def __init__(self, pt1: Point, pt2: Point):
        super().__init__(pt2.x - pt1.x, pt2.y - pt1.y)
        self.pt1 = pt1
        self.pt2 = pt2

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def __repr__(self):
        return f"{self.pt1},{self.pt2}"


class Segment(Vector):
    __slots__ = ['x', 'y', 'pt1', 'pt2']

    def __init__(self, pt1: Point, pt2: Point):
        super().__init__(pt1, pt2)

    def projection(self, pt: Point)-> Point:
        t = self.dot(Vector(self.pt1, pt)) / self.norm()
        return self.pt1 + self * t

    def reflection(self, pt: Point) -> Point:
        return self.projection(pt) * 2 - pt

    def is_intersected_with(self, other) -> bool:
        if (self.point_geometry(other.pt1) * self.point_geometry(other.pt2)) <= 0\
                and other.point_geometry(self.pt1) * other.point_geometry(self.pt2) <= 0:
            return True
        else:
            return False

    def point_geometry(self, pt: Point) -> int:
        """
        [-2:"Online Back", -1:"Counter Clockwise", 0:"On Segment", 1:"Clockwise",  2:"Online Front"]
        """
        vec_pt1_to_pt = Vector(self.pt1, pt)
        cross = self.cross(vec_pt1_to_pt)
        if cross > 0:
            return -1   # counter clockwise
        elif cross < 0:
            return 1    # clockwise
        else:           # cross == 0
            dot = self.dot(vec_pt1_to_pt)
            if dot < 0:
                return -2    # online back
            else:       # dot > 0
                if self.abs() < vec_pt1_to_pt.abs():
                    return 2    # online front
                else:
                    return 0    # on segment

    def cross_point(self, other) -> Point:
        d1 = abs(self.cross(Vector(self.pt1, other.pt1)))       # / self.abs()
        d2 = abs(self.cross(Vector(self.pt1, other.pt2)))       # / self.abs()
        t = d1 / (d1 + d2)
        return other.pt1 + other * t

    def distance_to_point(self, pt: Point) -> Union[int, float]:
        vec_pt1_to_pt = Vector(self.pt1, pt)
        if self.dot(vec_pt1_to_pt) <= 0:
            return vec_pt1_to_pt.abs()
        vec_pt2_to_pt = Vector(self.pt2, pt)
        if Vector.dot(self * -1, vec_pt2_to_pt) <= 0:
            return vec_pt2_to_pt.abs()
        return (self.projection(pt) - pt).abs()

    def segment_distance(self, other) -> Union[int, float]:
        if self.is_intersected_with(other):
            return 0.0
        else:
            return min(
                self.distance_to_point(other.pt1),
                self.distance_to_point(other.pt2),
                other.distance_to_point(self.pt1),
                other.distance_to_point(self.pt2)
            )

    def __repr__(self):
        return f"{self.pt1},{self.pt2}"


def main():
    num_query = int(input())
    for i in range(num_query):
        p0_x, p0_y, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y = map(int, input().split())
        seg_1 = Segment(Point(p0_x, p0_y), Point(p1_x, p1_y))
        seg_2 = Segment(Point(p2_x, p2_y), Point(p3_x, p3_y))

        print(f'{seg_1.segment_distance(seg_2):.10f}')
    return


main()
