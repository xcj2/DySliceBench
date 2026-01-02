#!/usr/bin/env python3
# CGL_2_D: Segments/Lines - Distance

from math import sqrt


class Segment:
    def __init__(self, p0, p1):
        self.end_points = (p0, p1)

    def another(self, p):
        if p == self.end_points[0]:
            return self.end_points[1]
        else:
            return self.end_points[0]

    def distance(self, other):
        def _distance(p, seg):
            p0 = seg._closest_point(p)
            p1 = seg.another(p0)
            x, y = p
            x0, y0 = p0
            x1, y1 = p1
            vp = (x-x0, y-y0)
            vseg = (x1-x0, y1-y0)
            if dot(vp, vseg) <= 0:
                return length(vp)
            else:
                x, y = vp
                return length(projection(vp, orthogonal(vseg)))

        if self.intersect(other):
            return 0.0

        dists = []
        for p0 in self.end_points:
            dists.append(_distance(p0, other))
        for p1 in other.end_points:
            dists.append(_distance(p1, self))

        return min(dists)

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

    def _closest_point(self, p):
        p0, p1 = self.end_points
        x, y = p
        x0, y0 = p0
        x1, y1 = p1
        if length((x0-x, y0-y)) < length((x1-x, y1-y)):
            return p0
        else:
            return p1

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


def projection(p, v):
    x, y = v
    r = dot(p, v) / dot(v, v)
    return (x*r, y*r)


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

        s0 = Segment((x0, y0), (x1, y1))
        s1 = Segment((x2, y2), (x3, y3))

        print("{:.10f}".format(s0.distance(s1)))


if __name__ == '__main__':
    run()

