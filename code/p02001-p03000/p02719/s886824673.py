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
def PL(L) : print(*L, sep="\n")

N, K = LI()

if N == K:
    print(0)
elif N > K:
    a1 = N % K
    print(min(a1, abs(K-a1)))
else:
    print(min(N, abs(K-N)))
