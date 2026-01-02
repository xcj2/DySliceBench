#!/usr/bin/env python3
# CGL_7_D: Circles - Cross Points of a Circle and a line

from math import sqrt


def cross_point(circle, p1, p2):
    x0, y0, r = circle
    x1, y1 = p1
    x2, y2 = p2

    p1p2 = norm((x2-x1, y2-y1))
    op1 = norm((x0-x1, y0-y1))
    rr = r*r
    dp = dot((x0-x1, y0-y1), (x2-x1, y2-y1))

    d = dp*dp - p1p2 * (op1 - rr)

    if abs(d) < 1e-10:
        t = dp / p1p2
        return [(x1 + t*(x2-x1), y1 + t*(y2-y1))]
    elif d > 1e-10:
        t1 = (dp+sqrt(d)) / p1p2
        t2 = (dp-sqrt(d)) / p1p2
        return [(x1 + t1*(x2-x1), y1 + t1*(y2-y1)),
                (x1 + t2*(x2-x1), y1 + t2*(y2-y1))]
    else:
        return None


def norm(v):
    x, y = v
    return x**2 + y**2


def dot(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1*x2 + y1*y2


def run():
    c = [int(i) for i in input().split()]
    q = int(input())

    for _ in range(q):
        x1, y1, x2, y2 = [int(i) for i in input().split()]
        ps = cross_point(c, (x1, y1), (x2, y2))

        if ps is None:
            raise ValueError('the circle and line do not intersect')
        if len(ps) == 1:
            ps *= 2

        p1, p2 = ps
        if p1 > p2:
            p1, p2 = p2, p1

        print("{:.8f} {:.8f} {:.8f} {:.8f}".format(*p1, *p2))


if __name__ == '__main__':
    run()

