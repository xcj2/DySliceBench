#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
7
2 1
0 0
1 2
2 2
4 2
1 3
3 3

output:
5
0 0
2 1
4 2
3 3
1 3

The operator module functions allow multiple levels of sorting. For example, to sort by grade then by age:

sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
"""

import sys
from operator import attrgetter

EPS = 1e-9


def cross(a, b):
    return a.real * b.imag - a.imag * b.real


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def check_ccw(p0, p1, p2):
    a, b = p1 - p0, p2 - p0
    if cross(a, b) > EPS:
        # print('COUNTER_CLOCKWISE')
        flag = 1
    elif cross(a, b) < -1 * EPS:
        # print('CLOCKWISE')
        flag = -1
    elif dot(a, b) < -1 * EPS:
        # print('ONLINE_BACK')
        flag = 2
    elif abs(a) < abs(b):
        # print('ONLINE_FRONT')
        flag = -2
    else:
        # print('ON_SEGMENT')
        flag = 0
    return flag


def convex_check_Andrew(_polygon):
    upper, lower = list(), list()
    _polygon.sort(key=attrgetter('real', 'imag'))

    upper.extend((_polygon[0], _polygon[1]))
    lower.extend((_polygon[-1], _polygon[-2]))

    for i in range(2, points):
        n1 = len(upper)
        while n1 >= 2 and check_ccw(upper[n1 - 2], upper[n1 - 1], _polygon[i]) == 1:
            n1 -= 1
            upper.pop()
        upper.append(_polygon[i])

    for j in range(points - 3, -1, -1):
        n2 = len(lower)
        while n2 >= 2 and check_ccw(lower[n2 - 2], lower[n2 - 1], _polygon[j]) == 1:
            n2 -= 1
            lower.pop()
        lower.append(_polygon[j])

    # print(upper, lower)
    lower.reverse()
    # lower.sort(key=attrgetter('imag', 'real'))
    lower_min = min(lower, key=attrgetter('imag', 'real'))
    # print(lower_min)
    min_index = lower.index(lower_min)
    lower_right = lower[min_index:]
    lower_left = lower[:min_index]
    for k in range(len(upper) - 2, 0, -1):
        lower_right.append(upper[k])
    return lower_right + lower_left


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    points = int(_input[0])
    p_info = map(lambda x: x.split(), _input[1:])

    polygon = [int(x) + int(y) * 1j for x, y in p_info]
    ans = convex_check_Andrew(polygon)
    print(len(ans))
    for ele in ans:
        print(int(ele.real), int(ele.imag))