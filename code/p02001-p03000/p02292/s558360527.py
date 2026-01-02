#!/usr/bin/env python3
# CGL_1_C: Points/Vectors - Counter-Clockwise

from enum import Enum
from math import sqrt


class Position(Enum):
    COUNTER_CLOCKWISE = 0
    CLOCKWISE = 1
    ONLINE_BACK = 2
    ONLINE_FRONT = 3
    ON_SEGMENT = 4


def dot(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * x2 + y1 * y2


def length(v):
    x, y = v
    return sqrt(x**2 + y**2)


def orthogonal(v):
    x, y = v
    return -y, x


def ccw(v1, v2):
    d1 = dot(v1, v2)
    d2 = dot(orthogonal(v1), v2)

    if d2 > 0:
        return Position.COUNTER_CLOCKWISE
    elif d2 < 0:
        return Position.CLOCKWISE
    elif d1 < 0:
        return Position.ONLINE_BACK
    else:
        if length(v1) >= length(v2):
            return Position.ON_SEGMENT
        else:
            return Position.ONLINE_FRONT


def run():
    x0, y0, x1, y1 = [int(i) for i in input().split()]
    q = int(input())

    for _ in range(q):
        x2, y2 = [int(i) for i in input().split()]
        pos = ccw((x1-x0, y1-y0), (x2-x0, y2-y0))
        print(pos.name)


if __name__ == '__main__':
    run()

