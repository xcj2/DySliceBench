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
d = wi()

time = [[] for _ in range(13)]

for t in d:
    time[t].append(t)

for idx, kosu in enumerate(time):
    if len(kosu) >= 3:
        print(0)
        exit()

if n > 11:
    if len(time[0]) >= 1 or len(time[12]) > 1:
        print(0)
        exit()
    else:
        print(1)
        exit()

time = functools.reduce(lambda a, b: a + b, time)
ans = INF; A = 0

for ti in itertools.product([0, 1], repeat=len(time)):  # 11**2
    kyu = []
    for kk in range(len(ti)):
        if ti[kk] == 0:
            kyu.append(time[kk])
        else:
            kyu.append(24 - time[kk])
    kyu.append(0)

    for k in itertools.combinations(kyu, 2):  # nC2
        ans = min(ans, abs(k[0] - k[1]), 24 - abs(k[0] - k[1]))
    A = max(ans, A)
    ans = INF  # 初期化を忘れない
print(A)