import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; cnt = 0; ansli = []; tmpli = []; candili = []; stillset = set()
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
def s_list(): return list(input())
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def num_grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]#NumberGrid
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def grid(n): return [s_list() for _ in range(n)]

n = i()
a = wi()

minus = 0
plus = 0

a.sort()
for i in range(n):
    if a[i] >= 0:
        plus += 1
    elif a[i] < 0:
        minus += 1

if plus == 0:
    minus -= 1
    plus += 1
elif plus == n:
    minus += 1
    plus -= 1


mli = []
pli = []
for i in range(1, n + 1):
    if i <= minus:
        ans += -a[i - 1]
        mli.append(a[i - 1])
    else:
        ans += a[i - 1]
        pli.append(a[i - 1])

print(ans)
for i in range(n - 1):
    if i == 0:
        if plus == 1:
            print(pli[0], mli[0])
            tmp = pli[0] - mli[0]
        else:
            print(mli[0], pli[0])
            tmp = mli[0] - pli[0]
    elif i < plus - 1:
        print(tmp, pli[i])
        tmp = tmp - pli[i]
    elif i == plus - 1:
        print(pli[i], tmp)
        tmp = pli[i] - tmp
    else:
        print(tmp, mli[i - plus + 1])
        tmp = tmp - mli[i - plus + 1]