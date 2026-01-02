#!/usr/bin/python3

import array
from fractions import Fraction
import math
import os
import sys


def main():
    Q = read_int()
    for _ in range(Q):
        x0, y0, x1, y1, x2, y2, x3, y3 = read_ints()
        print(solve(Vec(x0, y0), Vec(x1, y1), Vec(x2, y2), Vec(x3, y3)))


CROSS = 1
NOT_CROSS = 0


def solve(a, b, c, d):
    p = b - a
    q = c - a
    r = d - a
    cq = p.cross(q)
    cr = p.cross(r)
    if cq == 0 and cr == 0:
        dq = p.dot(q)
        dr = p.dot(r)
        ap = p.abs2()
        aq = q.abs2()
        ar = r.abs2()
        if (dq < 0 and dr < 0) or (ap < aq and ap < ar):
            return NOT_CROSS
        return CROSS

    if cq * cr > 0:
        return NOT_CROSS

    p = d - c
    q = a - c
    r = b - c
    cq = p.cross(q)
    cr = p.cross(r)
    if cq * cr > 0:
        return NOT_CROSS

    return CROSS


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

