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
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def ws(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def s(): return input()
def hi(n): return [i() for _ in range(n)]
def hip(n): return [i() - 1 for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

n = i()
p = hip(n)

stillset = set()
flagli = [0] * n
for i in range(n):
    if p[i] - 1 in stillset:
        if p[i] != 0:
            flagli[p[i] - 1] = 1
    stillset.add(p[i])

sign = 1 if flagli[0] == 1 else 0
tmp = 1 if flagli[0] == 1 else 0
for i in range(1, n):
    if sign == 1:
        if flagli[i] == 1:
            tmp += 1
        else:
            sign = 0
            ans = max(ans, tmp)
            tmp = 0
    else:
        if flagli[i] == 1:
            tmp += 1
            sign = 1
        else:
            pass
ans = max(ans, tmp) + 1

print(n - ans)