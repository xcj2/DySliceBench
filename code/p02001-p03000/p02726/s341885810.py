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

N, X, Y = LI()

ans = [0] * N

for i in range(1, N+1):
    for j in range(i, N+1):
        ans[min(j-i, abs(X-i)+1+abs(Y-j), abs(X-j)+1+abs(Y-i))] += 1

PL(ans[1:])
