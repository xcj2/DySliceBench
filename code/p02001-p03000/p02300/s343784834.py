#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    N = read_int()
    P = [Vec(x, y) for x, y in [read_ints() for _ in range(N)]]
    ans = solve(N, P)
    print(len(ans))
    for p in ans:
        print(p.x, p.y)


def solve(N, P):
    v = min(P, key=lambda p: (p.y, p.x))
    P.remove(v)

    def cmp_angle(a, b):
        return b[1].cross(a[1])

    PV = [(p, p - v) for p in P]
    key_fn = functools.cmp_to_key(cmp_angle)
    PV.sort(key=key_fn)

    hull = [v]

    i = 0
    j = 1
    while j < N - 1 and cmp_angle(PV[i], PV[j]) == 0:
        j += 1
    sub = list(PV[i : j])
    sub.sort(key=lambda pv: pv[1].abs2())
    hull += [p for p, _ in sub]
    i = j

    while i < N - 1:
        a = hull[-2]
        b = hull[-1]
        j = i + 1
        while j < N - 1 and cmp_angle(PV[i], PV[j]) == 0:
            j += 1
        sub = [(p, p - b) for p, _ in PV[i : j]]

        sub.sort(key=key_fn)

        for p, pb in sub:
            hull.append(p)
            while len(hull) >= 3:
                a = hull[-3]
                b = hull[-2]
                c = hull[-1]
                if (b - a).cross(c - b) >= 0:
                    break
                hull[-2] = c
                del hull[-1]

        i = j

    return hull


###############################################################################
# AUXILIARY FUNCTIONS

class Vec(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vec(self.x / scalar, self.y / scalar)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def __idiv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash('Vec', self.x, self.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def abs2(self):
        return self.x * self.x + self.y * self.y

    def __abs__(self):
        return math.sqrt(float(self.abs2()))

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


if __name__ == '__main__':
    main()

