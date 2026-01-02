import sys
from itertools import starmap
readline = sys.stdin.readline
class Segment(object):
    __slots__ = ('fi', 'se')
    def __init__(self, fi, se):
        self.fi = fi
        self.se = se
def cross(a, b):
    return a.real * b.imag - a.imag * b.real
def dot(a, b):
    return a.real * b.real + a.imag * b.imag
def norm(base):
    return abs(base) ** 2
def project(s, p2):
    base = s.fi - s.se
    r = dot(p2 - s.fi, base) / norm(base)
    return s.fi + base * r
def reflect(s, p):
    return p + (project(s, p) - p) * 2.0
s = Segment(*starmap(complex, zip(*[map(float, readline().split())] * 2)))
n = int(readline())
for _ in [0] * n:
    p1 = reflect(s, complex(*map(float, readline().split())))
    print("{0:.10f} {1:.10f}".format(p1.real, p1.imag))