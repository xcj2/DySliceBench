#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
3
0 0 2 0 1 1 1 -1
0 0 1 1 0 1 1 0
0 0 1 1 1 0 0 1

output:
1.0000000000 0.0000000000
0.5000000000 0.5000000000
0.5000000000 0.5000000000
"""

import sys
from collections import namedtuple


def cross(a, b):
    return a.real * b.imag - a.imag * b.real


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def get_cross_point(s1, s2):
    base_vector = s2.target - s2.source
    d1 = abs(cross(base_vector, s1.source - s2.source))
    d2 = abs(cross(base_vector, s1.target - s2.source))
    t = d1 / (d1 + d2)
    cross_point = s1.source + (s1.target - s1.source) * t
    print('{real:.10f} {imag:.10f}'.format(real=cross_point.real, imag=cross_point.imag))

    return None


def solve(_segments):
    for segment in _segments:
        segment = tuple(map(int, segment))
        p0, p1, p2, p3 = (x + y * 1j for x, y in zip(segment[::2], segment[1::2]))
        s1, s2 = Segment(p0, p1), Segment(p2, p3)
        get_cross_point(s1, s2)

    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    l_num = int(_input[0])
    segments = map(lambda x: x.split(), _input[1:])
    Segment = namedtuple('Segment', ('source', 'target'))
    solve(segments)