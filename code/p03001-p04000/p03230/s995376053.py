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
def s_list(): return list(input())
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def num__grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]#NumberGrid
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def grid(n): return [s_list() for _ in range(n)]

n = i()
solve = (1 + (1 + 8 * n) ** 0.5) / 2
if int(solve) != solve:
    print("No")
else:
    print("Yes")
    k = int(solve)
    ansli = [[] for _ in range(k)]

    cnt = 1
    dec = 0
    i = 1
    while i <= n:
        if cnt <= k - 1 - dec:
            ansli[dec].append(i)
            cnt += 1
            i += 1
        else:
            cnt = 1
            dec += 1

    cnt = 1
    up = 1
    i = 1
    while i <= n:
        if cnt <= k - 1:
            ansli[cnt].append(i)
            cnt += 1
            i += 1
        else:
            up += 1
            cnt = up

    print(k)
    for i in range(k):
        print(len(ansli[i]), " ".join(map(str, ansli[i])))