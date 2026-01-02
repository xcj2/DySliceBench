#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
input = stdin.readline
import collections
import math


__author__ = "Hamukichi (Nombiri)"
__copyright__ = "Copyright 2015, Hamukichi (Nombiri)"
__version__ = "0.1.0"
__date__ = "2015-11-29"
__licence__ = "MIT License"

eps = 10E-4

def is_equal(v1, v2):
    d = abs(v1 - v2)
    if d < eps:
        return True
    return False

class Vector2(collections.namedtuple("Vector2", "x y")):
    """Class for representing a two-dimensional vector.
    :param x: The x component of the vector.
    :type x: float
    :param y: The y component of the vector.
    :type y: float
    """

    __slots__ = ()

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # cross product
        return self.x * other.y - self.y * other.x

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __pos__(self):
        return Vector2(+self.x, +self.y)

    def __abs__(self):  # norm
        return math.sqrt(float(self.x * self.x + self.y * self.y))

    def dotproduct(self, other):
        """Returns the dot product of this vector and the given vector.
        :param other: The second vector.
        """

        return self.x * other.x + self.y * other.y

lines = stdin.readlines()
n = int(lines[0])
q = int(lines[n+1])

v_set = []
for i in range(1, n+1):
    v_set.append(Vector2(*list(map(int, lines[i].split()))))

def is_involed(p):

    counter = 0

    for i in range(n):
        g_i = v_set[i-1]
        g_in = v_set[i]
        if g_i.y <= g_in.y:
            a = g_i - p
            b = g_in - p
        else:
            b = g_i - p
            a = g_in - p

        if  a * b > 0:
            if a.y  <= 0 < b.y :
                counter += 1
        elif a * b == 0:
            if a.dotproduct(b) <= 0:
                return -1

    return counter

for k in range(q):
    p = Vector2(*list(map(int, lines[n+2+k].split())))
    t = is_involed(p)
    if t < 0:
        print(1)
    elif t % 2 == 0:
        print(0)
    else:
        print(2)










