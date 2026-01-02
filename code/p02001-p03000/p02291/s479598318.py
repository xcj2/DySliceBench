#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
0 0 3 4
3
2 5
1 4
0 3

output:
4.2400000000 3.3200000000
3.5600000000 2.0800000000
2.8800000000 0.8400000000
"""

import sys


def solve(_prj_info):
    for point in _prj_info:
        xp, yp = map(int, point)
        p = xp + yp * 1j
        hypo = p - p1
        prj = p1 + base * project(base, hypo)
        ref = p + (prj - p) * 2.0
        print('{0:.10f} {1:.10f}'.format(ref.real, ref.imag))

    return _prj_info


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


# abs(prj)/abs(base)
def project(a, b):
    return dot(a, b) / dot(a, a)


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    base_info = _input[0].split()
    q_num = int(_input[1])
    prj_points = map(lambda x: x.split(), _input[2:])

    x1, y1, x2, y2 = map(int, base_info)
    p1, p2 = x1 + y1 * 1j, x2 + y2 * 1j
    base = p2 - p1
    res = solve(prj_points)