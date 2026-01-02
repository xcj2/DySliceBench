import math


def dot(ux, uy, vx, vy):
    return ux*vx + uy*vy


def cross(ux, uy, vx, vy):
    return ux*vy - uy*vx


def dist_to_segment(x, y, ax, ay, bx, by):
    if dot(x - ax, y - ay, bx - ax, by - ay) < 0:
        return math.hypot(x - ax, y - ay)
    if dot(x - bx, y - by, ax - bx, ay - by) < 0:
        return math.hypot(x - bx, y - by)
    c = abs(cross(bx - ax, by - ay, x - ax, y - ay))
    return c / math.hypot(bx - ax, by - ay)


q = int(input())

for _ in range(q):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())

    c1 = cross(x1 - x0, y1 - y0, x2 - x0, y2 - y0)
    c2 = cross(x1 - x0, y1 - y0, x3 - x0, y3 - y0)
    c3 = cross(x3 - x2, y3 - y2, x0 - x2, y0 - y2)
    c4 = cross(x3 - x2, y3 - y2, x1 - x2, y1 - y2)

    if c1*c2 < 0 and c3*c4 < 0:
        d = 0.0
    else:
        d = dist_to_segment(x2, y2, x0, y0, x1, y1)
        d = min(d, dist_to_segment(x3, y3, x0, y0, x1, y1))
        d = min(d, dist_to_segment(x0, y0, x2, y2, x3, y3))
        d = min(d, dist_to_segment(x1, y1, x2, y2, x3, y3))

    print('{:.10f}'.format(d))

