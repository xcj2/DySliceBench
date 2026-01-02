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


class Segment(object):
    __slots__ = ('source', 'target')

    def __init__(self, source, target):
        self.source = complex(source)
        self.target = complex(target)


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def project(s, p):
    base_vector = s.target - s.source
    prj_ratio = dot(p - s.source, base_vector) / pow(abs(base_vector), 2)
    return s.source + base_vector * prj_ratio


def solve(_prj_points):
    for point in _prj_points:
        xp, yp = map(int, point)
        p = xp + yp * 1j
        prj = project(prj_segment, p)
        print('{real:.10f} {imag:.10f}'.format(real=prj.real, imag=prj.imag))

    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()

    line = tuple(map(int, _input[0].split()))
    q_num = int(_input[1])
    p1, p2 = (x + y * 1j for x, y in zip(line[::2], line[1::2]))
    prj_segment = Segment(p1, p2)

    prj_points = map(lambda x: x.split(), _input[2:])

    solve(prj_points)