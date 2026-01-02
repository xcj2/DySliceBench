import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right; sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; ansli = []; tmpli = []; candili = []
eps = 1.0 / 10 ** 10; mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]; ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]; ddn9 = ddn + [(0, 0)]
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

n, c = wi()
xv = mi(n)
#下準備，時計回り
cwli = []; cal = 0
for i in range(n):
    cal += xv[i][1] - xv[i][0]
    if i > 0:
        cal += xv[i - 1][0]#戻す，復元
    cwli.append([cal, i])
#下準備，反時計回り
ccwli = []; cal = 0
for i in range(n - 1, -1, -1):
    cal += xv[i][1] - (c - xv[i][0])
    if i < n - 1:
        cal += (c - xv[i + 1][0])
    ccwli.append([cal, i])

cwli2 = sorted(cwli, reverse=True)
ccwli2 = sorted(ccwli, reverse=True)

#時計回りから
nowp = 0
#cwansli = [-INF] * n
for i in range(n):
    while nowp < n:
        if ccwli2[nowp][1] > i:
            ans = max(cwli[i][0] - xv[i][0] + ccwli2[nowp][0], ans)
            break
        else:
            nowp += 1
#反時計回りから
#ccwansli = [-INF] * n
nowp = 0
for i in range(n - 1, -1, -1):
    while nowp < n:
        if cwli2[nowp][1] < i:
            ans = max(ccwli[n - i - 1][0] - (c - xv[i][0]) + cwli2[nowp][0], ans)
            break
        else:
            nowp += 1

ans = max(cwli2[0][0], ccwli2[0][0], ans)

print(ans)