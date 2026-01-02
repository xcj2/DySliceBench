#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
3
0 0 1 0 0 1 1 1
0 0 1 0 2 1 1 2
-1 0 1 0 0 1 0 -1

output:
1.0000000000
1.4142135624
0.0000000000
"""

import sys

EPS = 1e-9


class Segment(object):
    __slots__ = ('source', 'target')

    def __init__(self, source, target):
        self.source = complex(source)
        self.target = complex(target)


def cross(a, b):
    return a.real * b.imag - a.imag * b.real


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def get_distance_lp(l, p):
    return abs(cross(l.target - l.source, p - l.source) / abs(l.target - l.source))


def get_distance_sp(s, p):
    if dot(s.target - s.source, p - s.source) < 0:
        return abs(p - s.source)
    elif dot(s.source - s.target, p - s.target) < 0:
        return abs(p - s.target)
    else:
        return get_distance_lp(s, p)


def check_ccw(p0, p1, p2):
    a, b = p1 - p0, p2 - p0
    if cross(a, b) > EPS:
        flag = 1
    elif cross(a, b) < -1 * EPS:
        flag = -1
    elif dot(a, b) < -1 * EPS:
        flag = 2
    elif abs(a) < abs(b):
        flag = -2
    else:
        flag = 0
    return flag


def check_intersection(p0, p1, p2, p3):
    intersected = (check_ccw(p0, p1, p2) * check_ccw(p0, p1, p3) <= 0) and \
                  (check_ccw(p2, p3, p0) * check_ccw(p2, p3, p1) <= 0)

    return intersected


def calc_distance(_lines):
    for line in _lines:
        line_axis = tuple(map(int, line))
        p0, p1, p2, p3 = (x + y * 1j for x, y in zip(line_axis[::2], line_axis[1::2]))
        s1, s2 = Segment(p0, p1), Segment(p2, p3)
        
        intersected = check_intersection(s1.source, s1.target, s2.source, s2.target)
        if intersected:
            distance = 0
        else:
            distance = min(min(get_distance_sp(s1, s2.source), get_distance_sp(s1, s2.target)),
                           min(get_distance_sp(s2, s1.source), get_distance_sp(s2, s1.target)))
            
        print('{ans:.10f}'.format(ans=distance))
        
    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    questions = int(_input[0])
    lines = map(lambda x: x.split(), _input[1:])
    calc_distance(lines)