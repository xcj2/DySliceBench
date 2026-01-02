#!/usr/bin/env python3

import enum


EPS = 1e-10


class LinesRelation(enum.Enum):
    other = 0
    orthogonal = 1
    parallel = 2


def inner_product(v1, v2):
    return v1.real * v2.real + v1.imag * v2.imag


def outer_product(v1, v2):
    return v1.real * v2.imag - v1.imag * v2.real


def judge_lines_relation(l1_start, l1_end, l2_start, l2_end):
    v1 = l1_end - l1_start
    v2 = l2_end - l2_start
    if abs(outer_product(v1, v2)) < EPS:
        return LinesRelation.parallel
    elif abs(inner_product(v1, v2)) < EPS:
        return LinesRelation.orthogonal
    else:
        return LinesRelation.other


def main():
    q = int(input())
    for _ in range(q):
        xp0, yp0, xp1, yp1, xp2, yp2, xp3, yp3 = map(int, input().split())
        l1_start = complex(xp0, yp0)
        l1_end = complex(xp1, yp1)
        l2_start = complex(xp2, yp2)
        l2_end = complex(xp3, yp3)
        print(judge_lines_relation(l1_start, l1_end, l2_start, l2_end).value)


if __name__ == '__main__':
    main()