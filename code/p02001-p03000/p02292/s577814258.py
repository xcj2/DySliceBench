#!/usr/bin/python3

import array
from fractions import Fraction
import math
import os
import sys


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

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def abs2(self):
        return self.x * self.x + self.y * self.y

    def __abs__(self):
        return math.sqrt(float(self.abs2()))

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


def main():
    x1, y1, x2, y2 = read_ints()
    Q = read_int()
    for _ in range(Q):
        x, y = read_ints()
        print(solve(Vec(x1, y1), Vec(x2, y2), Vec(x, y)))


CCW = 'COUNTER_CLOCKWISE'
CW = 'CLOCKWISE'
OLB = 'ONLINE_BACK'
OLF = 'ONLINE_FRONT'
OL = 'ON_SEGMENT'


def solve(u, v, a):
    v -= u
    a -= u
    c = v.cross(a)
    if c > 0:
        return CCW
    if c < 0:
        return CW
    d = v.dot(a)
    if d < 0:
        return OLB
    if v.abs2() < a.abs2():
        return OLF
    return OL


###############################################################################
# AUXILIARY FUNCTIONS

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

