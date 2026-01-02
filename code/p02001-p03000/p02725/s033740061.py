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

K, N = LI()
A = LI()

tmp = A[0]
tmp += (K - A[-1])

ans = [tmp]
for i in range(N - 1):
    ans.append(A[i+1] - A[i])

ans.sort(reverse=True)

print(sum(ans[1:]))