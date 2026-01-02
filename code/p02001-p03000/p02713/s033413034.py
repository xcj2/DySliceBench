# coding: utf-8

import sys
import math
import collections
import itertools
INF = 10 ** 13
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def lcm(x, y) : return (x * y) // math.gcd(x, y)
def I() : return int(input())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def LS() : return input().split()
def RS(N) : return [input() for _ in range(N)]
def LRS(N) : return [input().split() for _ in range(N)]
def PL(L) : print(*L, sep="\n")

from functools import lru_cache

@lru_cache(maxsize=INF)
def ggcd(a, b):
    return math.gcd(a, b)

K = I()

h = [0] * 201
for a in range(1, K+1):
    for b in range(1, K+1):
        h[ggcd(min(a,b), max(a,b))] += 1

ans = 0
for c in range(1, K+1):
    for i, ab in enumerate(h):
        if ab != 0:
            ans += ggcd(min(c,i), max(c,i)) * ab

print(ans)
