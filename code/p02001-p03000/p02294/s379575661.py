#!/usr/bin/env python3
# CGL_2_B: Segments/Lines - Intersection

from math import sqrt


class Segment:
    def __init__(self, p0, p1):
        self.end_points = (p0, p1)

    def intersect(self, other):
        p0, p1 = self.end_points
        p2, p3 = other.end_points

        if convex(p0, p2, p1, p3):
            return True
        else:
            if (p0 in other or p1 in other
                    or p2 in self or p3 in self):
                return True

        return False

    def __contains__(self, p):
        p0, p1 = self.end_points
        x0, y0 = p0
        x1, y1 = p1
        x, y = p
        v = (x1-x0, y1-y0)
        v0 = (x-x0, y-y0)
        v1 = (x-x1, y-y1)
        if dot(orthogonal(v0), v1) == 0:
            if abs(length(v0) + length(v1) - length(v)) < 1e-10:
                return True
        return False


def dot(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * x2 + y1 * y2


def orthogonal(v):
    x, y = v
    return -y, x


def length(v):
    x, y = v
    return sqrt(x**2 + y**2)


def convex(p0, p1, p2, p3):
    ret = []
    for pa, pb, pc in zip([p0, p1, p2, p3],
                          [p1, p2, p3, p0],
                          [p2, p3, p0, p1]):
        xa, ya = pa
        xb, yb = pb
        xc, yc = pc
        v1 = (xb - xa, yb - ya)
        v2 = (xc - xb, yc - yb)
        ret.append(dot(orthogonal(v1), v2))

    return all([d > 0 for d in ret]) or all([d < 0 for d in ret])


def run():
    q = int(input())

    for _ in range(q):
        x0, y0, x1, y1, x2, y2, x3, y3 = [int(i) for i in input().split()]
        s1 = Segment((x0, y0), (x1, y1))
        s2 = Segment((x2, y2), (x3, y3))
        if s1.intersect(s2):
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    run()

