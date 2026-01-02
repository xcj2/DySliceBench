#!/usr/bin/python3

import array
from fractions import Fraction
import math
import os
import sys


def main():
    N = read_int()
    P = [Vec(x, y) for x, y in [read_ints() for _ in range(N)]]
    Q = read_int()
    for _ in range(Q):
        x, y = read_ints()
        print(solve(N, P, Vec(x, y)))


INSIDE = 2
ON_EDGE = 1
OUTSIDE = 0


def solve(N, P, A):
    P = [p - A for p in P]

    min_v = Vec(-1, 0)
    for p in P:
        if p == Vec(0, 0):
            return ON_EDGE

        v = Vec(p.x, p.y)
        if v.y == 0:
            continue
        if v.y < 0:
            v = -v

        if min_v.cross(v) < 0:
            min_v = v

    assert min_v != Vec(-1, 0)

    u = min_v + Vec(1, 0)

    neg_count = 0
    for i in range(N):
        a = P[i]
        b = P[(i + 1) % N]

        c_a = u.cross(a)
        c_b = u.cross(b)
        assert c_a != 0
        assert c_b != 0
        if c_a * c_b > 0:
            continue

        ba = b - a
        k = Fraction(a.cross(ba), u.cross(ba))
        if k == 0:
            return ON_EDGE
        if k < 0:
            neg_count += 1

    if neg_count % 2 == 1:
        return INSIDE
    return OUTSIDE


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

