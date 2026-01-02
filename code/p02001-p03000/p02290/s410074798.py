#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
0 0 3 4
1
2 5

output:
3.1200000000 4.1600000000
"""

import sys


def solve(_prj_info):
    for point in _prj_info:
        xp, yp = map(int, point)
        p = xp + yp * 1j
        hypo = p - p1
        prj = p1 + base_vector * project(base_vector, hypo)
        print('{:.10f} {:.10f}'.format(prj.real, prj.imag))

    return _prj_info


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def project(a, b):
    return dot(a, b) / dot(a, a)


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    base_info = _input[0].split()
    q_num = int(_input[1])
    prj_points = map(lambda x: x.split(), _input[2:])

    x1, y1, x2, y2 = map(int, base_info)
    p1, p2 = x1 + y1 * 1j, x2 + y2 * 1j
    base_vector = p2 - p1
    res = solve(prj_points)