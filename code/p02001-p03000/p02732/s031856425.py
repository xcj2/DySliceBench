# coding: utf-8

import sys
import math
import collections
import itertools
INF = 10 ** 10
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return y if x % y == 0 else gcd(y, x % y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
from functools import lru_cache

N = I()
A = LI()

@lru_cache(maxsize=None)
def ncr(n, r):
    return int(n*(n-1)/2)

tmp = 0
AA = collections.Counter(A)
As = AA.items()
for n, t in As:
    tmp += ncr(t, 2)

for a in A:
    an = AA[a]
    print(tmp - ncr(an, 2) + ncr(an - 1, 2))
