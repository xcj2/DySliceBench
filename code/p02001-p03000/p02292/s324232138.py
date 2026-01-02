#!/usr/bin/env python3

import enum


EPS = 1e-10


class PointsRelation(enum.Enum):
    counter_clockwise = 1
    clockwise = 2
    online_back = 3
    on_segment = 4
    online_front = 5


def inner_product(v1, v2):
    return v1.real * v2.real + v1.imag * v2.imag


def outer_product(v1, v2):
    return v1.real * v2.imag - v1.imag * v2.real


def judge_relation(p0, p1, p2):
    v1 = p1 - p0
    v2 = p2 - p0
    op = outer_product(v1, v2)
    if op > EPS:
        return PointsRelation.counter_clockwise
    elif op < -EPS:
        return PointsRelation.clockwise
    elif inner_product(v1, v2) < -EPS:
        return PointsRelation.online_back
    elif abs(v1) < abs(v2):
        return PointsRelation.online_front
    else:
        return PointsRelation.on_segment


def main():
    x_p0, y_p0, x_p1, y_p1 = map(float, input().split())
    p0 = complex(x_p0, y_p0)
    p1 = complex(x_p1, y_p1)
    q = int(input())
    for _ in range(q):
        p2 = complex(*map(float, input().split()))
        ans = judge_relation(p0, p1, p2)
        if ans == PointsRelation.counter_clockwise:
            print("COUNTER_CLOCKWISE")
        elif ans == PointsRelation.clockwise:
            print("CLOCKWISE")
        elif ans == PointsRelation.online_back:
            print("ONLINE_BACK")
        elif ans == PointsRelation.online_front:
            print("ONLINE_FRONT")
        else:
            print("ON_SEGMENT")


if __name__ == '__main__':
    main()