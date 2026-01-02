#!/usr/bin/env python3
# CGL_3_A: Polygon - Area


def area(ps):
    p0, p1, *ps = ps
    area = 0.0

    x0, y0 = p0
    x1, y1 = p1
    v1 = (x1-x0, y1-y0)
    for p2 in ps:
        x2, y2 = p2
        v2 = (x2-x0, y2-y0)
        area += cross(v1, v2)
        v1 = v2

    return area / 2


def cross(v0, v1):
    x0, y0 = v0
    x1, y1 = v1
    return x0*y1 - x1*y0


def run():
    n = int(input())
    ps = []
    for _ in range(n):
        x, y = [int(i) for i in input().split()]
        ps.append((x, y))

    print("{:.1f}".format(area(ps)))


def show():
    import matplotlib.pyplot as plt
    n = int(input())
    xs = []
    ys = []
    for _ in range(n):
        x, y = [int(i) for i in input().split()]
        xs.append(x)
        ys.append(y)

    plt.plot(xs, ys)
    plt.show()


if __name__ == '__main__':
    run()

