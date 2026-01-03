import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque
from heapq import heappush, heappop
sys.setrecursionlimit(10 ** 7)
ans = 0
tmp = 0
inf = 10 ** 20
INF = float("INF")
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
ddn9 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (0, 0)]
"""for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def ws(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def s(): return input()
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

n, a = wi()
x = wi()
X = max(x)
dp = [[[0] * (n + 1) for j in range(X * n + 2)] for i in range(n)]
dp[0][0][0] = 1
dp[0][x[0]][1] = 1

for p in range(1, n):
    for k in range(X * n + 2):
        for usenum in range(p + 1):
            dp[p][k][usenum] += dp[p - 1][k][usenum]
            if k - x[p] >= 0:
                dp[p][k][usenum + 1] += dp[p - 1][k - x[p]][usenum]

for k in range(X * n + 2):
    for usenum in range(n + 1):
        if usenum != 0:
            if k / usenum == a:
                ans += dp[n - 1][k][usenum]
print(ans)