#!/usr/bin/env python3
# CGL_3_C: Polygon - Polygon-Point Containment

from enum import Enum


class Position(Enum):
    OUTSIDE = 0
    BORDER = 1
    INSIDE = 2


class Polygon:
    def __init__(self, ps):
        self.ps = ps
        self.convex_poligons = divide(ps)

    def position(self, p):
        if p in self.ps:
            return Position.BORDER

        pos = [position(*c, p) for c in self.convex_poligons]
        if all([x == Position.OUTSIDE for x in pos]):
            return Position.OUTSIDE
        elif any([x == Position.INSIDE for x in pos]):
            return Position.INSIDE
        elif len([x for x in pos if x == Position.BORDER]) > 1:
            return Position.INSIDE
        else:
            return Position.BORDER


def divide(ps):
    if len(ps) < 3:
        return []

    p0, p1, p2, *ps = ps
    if not ccw(p0, p1, p2):
        return divide([p1, p2] + ps + [p0])

    for p in ps:
        if position(p0, p1, p2, p) != Position.OUTSIDE:
            return divide([p1, p2] + ps + [p0])

    return [(p0, p1, p2)] + divide([p0, p2] + ps)


def ccw(p0, p1, p2):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    v1 = (x1-x0, y1-y0)
    v2 = (x2-x1, y2-y1)
    return dot(orthogonal(v1), v2) > 0


def dot(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * x2 + y1 * y2


def cross(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * y2 - y1 * x2


def orthogonal(v):
    x, y = v
    return -y, x


def position(p0, p1, p2, p):
    x, y = p
    ps = [p0, p1, p2]
    online = False
    for i in range(3):
        pa = ps[i]
        pb = ps[(i+1) % 3]
        pc = ps[(i+2) % 3]
        xa, ya = pa
        xb, yb = pb
        xc, yc = pc
        vab = (xb-xa, yb-ya)
        vac = (xc-xa, yc-ya)
        vp = (x-xa, y-ya)
        c = cross(vab, vp) * cross(vp, vac)
        if c == 0:
            online = True
        elif c < 0:
            return Position.OUTSIDE

    if online:
        return Position.BORDER
    else:
        return Position.INSIDE


def run():
    g = int(input())

    ps = []
    for _ in range(g):
        x, y = [int(i) for i in input().split()]
        ps.append((x, y))

    poly = Polygon(ps)

    n = int(input())
    for _ in range(n):
        qx, qy = [int(i) for i in input().split()]

        pos = poly.position((qx, qy))
        print(pos.value)


if __name__ == '__main__':
    run()

