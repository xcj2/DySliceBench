#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
4
0 0
3 1
2 3
0 3
3
2 1
0 2
3 2

output:
2
1
0
"""

import sys

EPS = 1e-9


def cross(a, b):
    return a.real * b.imag - a.imag * b.real


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def check_contains(g, p):
    flag = False
    for j in range(edges):
        a, b = g[j] - p, g[(j + 1) % edges] - p
        if abs(cross(a, b)) < EPS and dot(a, b) < EPS:
            return 1
        elif a.imag > b.imag:
            a, b = b, a

        if a.imag < EPS < b.imag and cross(a, b) > EPS:
            flag = not flag
    return 2 if flag else 0


def solve(_p_info):
    for point in _p_info:
        px, py = map(float, point)
        p = px + py * 1j
        print(check_contains(polygon, p))
    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    edges = int(_input[0])
    e_info = map(lambda x: x.split(), _input[1:edges + 1])
    points = int(_input[edges + 1])
    p_info = map(lambda x: x.split(), _input[edges + 2:])

    polygon = [float(x) + float(y) * 1j for x, y in e_info]
    solve(p_info)