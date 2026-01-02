import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
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

n, k = wi()
v = wi()
v = deque(v)
pq = []
po = 0
cnt = 0
qwerty = min(n + 1, k + 1)
for i in range(qwerty):
    if i != 0:
        heappush(pq, v[i - 1])
    for j in range(qwerty - i):
        if j != 0:
            heappush(pq, v[-j])
        while k - i - j - cnt > 0:
            if pq != []:
                po = 0
                po = heappop(pq)
                if po < 0:
                    cnt += 1
                    tmpli.append(po)
                else:
                    heappush(pq, po)
                    cnt = 0
                    break
            else:
                break
        cnt = 0
        ans = max(ans, sum(pq))
        for bb in tmpli:
            heappush(pq, bb)
        tmpli = []
    pq = []
    for g in range(i + 1):
        if g != 0:
            heappush(pq, v[g - 1])

print(ans)