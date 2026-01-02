#!/usr/bin/env python3
# CGL_1_B: Points/Vectors - Reflection


def dprod(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * x2 + y1 * y2


def proj(p1, p2, p):
    x1, y1 = p1
    x2, y2 = p2
    x, y = p

    v1 = (x2-x1, y2-y1)
    v2 = (x-x1, y-y1)
    r = dprod(v1, v2) / dprod(v1, v1)

    return (x1 + r*v1[0], y1 + r*v1[1])


def refl(p1, p2, p):
    px, py = p
    hx, hy = proj(p1, p2, p)
    return (px + 2.0*(hx - px), py + 2.0*(hy - py))


def run():
    x1, y1, x2, y2 = [int(i) for i in input().split()]
    q = int(input())

    for _ in range(q):
        x, y = [int(i) for i in input().split()]
        print("{:.10f} {:.10f}".format(*refl((x1, y1), (x2, y2), (x, y))))


if __name__ == '__main__':
    run()

