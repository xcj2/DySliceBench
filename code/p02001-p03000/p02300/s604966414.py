#!/usr/bin/env python3
# CGL_4_A: Convex Polygon - Convex Hull

from operator import itemgetter


def cross(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * y2 - x2 * y1


def convex_hull(ps):
    ps.sort(key=itemgetter(0))
    ps.sort(key=itemgetter(1))
    p0 = ps[0]
    vs = [(p0, p0)]
    for p in ps[1:]:
        x, y = p
        p1, v1 = vs.pop()
        x1, y1 = p1
        v = (x-x1, y-y1)
        while vs and cross(v1, v) < 0:
            p1, v1 = vs.pop()
            x1, y1 = p1
            v = (x-x1, y-y1)

        vs.append((p1, v1))
        vs.append((p, v))

    for p in reversed(ps[:-1]):
        x, y = p
        p1, v1 = vs.pop()
        x1, y1 = p1
        v = (x-x1, y-y1)
        while vs and cross(v1, v) < 0:
            p1, v1 = vs.pop()
            x1, y1 = p1
            v = (x-x1, y-y1)

        vs.append((p1, v1))
        vs.append((p, v))

    return [p for p, v in vs[:-1]]


def run():
    n = int(input())
    ps = []

    for _ in range(n):
        x, y = [int(i) for i in input().split()]
        ps.append((x, y))

    convex = convex_hull(ps)

    print(len(convex))
    for p in convex:
        print('{} {}'.format(*p))


if __name__ == '__main__':
    run()

