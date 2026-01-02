#!/usr/bin/env python3
# CGL_3_B: Polygon - Is-Convex


def run():
    n = int(input())
    ps = []

    for _ in range(n):
        x, y = [int(i) for i in input().split()]
        ps.append((x, y))

    if convex(ps):
        print(1)
    else:
        print(0)


def dot(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * x2 + y1 * y2


def orthogonal(v):
    x, y = v
    return -y, x


def convex(ps0):
    p0, *ps1 = ps0
    ps1.append(p0)
    p1, *ps2 = ps1
    ps2.append(p1)
    ret = []
    for pa, pb, pc in zip(ps0, ps1, ps2):
        xa, ya = pa
        xb, yb = pb
        xc, yc = pc
        v1 = (xb - xa, yb - ya)
        v2 = (xc - xb, yc - yb)
        ret.append(dot(orthogonal(v1), v2))

    return all([d >= 0 for d in ret]) or all([d <= 0 for d in ret])


if __name__ == '__main__':
    run()

