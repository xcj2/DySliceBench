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
def num__grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]#NumberGrid
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def grid(n): return [s_list() for _ in range(n)]


s = input()
t = input()
ns = len(s)
nt = len(t)
alpha = "abcdefghijklmnopqrstuvwxyz"
aldi = {}
for i in alpha:
    aldi[i] = []

for i in range(ns):
    aldi[s[i]].append(i + 1)


num = []
if aldi[t[0]] == []:
    print("-1")
    exit()
mae = aldi[t[0]][0]
num.append(mae)
for i in range(1, nt):
    if aldi[t[i]] == []:
        print("-1")
        exit()
    else:
        kk = bisect_right(aldi[t[i]], mae)
        if kk == len(aldi[t[i]]):
            kk = aldi[t[i]][0]
        else:
            kk = aldi[t[i]][kk]
        mae = kk
        num.append(kk)

ans += num[0]
for i in range(1, len(num)):
    if num[i] <= num[i - 1]:
        ans += ns - num[i - 1] + num[i]
    else:
        ans += num[i] - num[i - 1]

if ans > 10 ** 100:
    print(-1)
else:
    print(ans)