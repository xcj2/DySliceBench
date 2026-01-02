import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right; sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0;  tmpli = []; candili = []
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

n = i()
#uvw
x = mi(n - 1)

routedi = {}
for i in range(n + 1):
    routedi[i] = []
for i in range(n - 1):
    routedi[x[i][0]].append([x[i][1], x[i][2]])
    routedi[x[i][1]].append([x[i][0], x[i][2]])

parli = [-1] * (n + 1)#親を保持
ansli = [-1]*(n + 1)
ansli[1] = 0
po = 1
que = deque()
que.append(1)
while que != deque():
    po = que.popleft()
    for i in routedi[po]:
        if parli[i[0]] == -1:  # 親が来るときは断る
            parli[i[0]] = po
            que.append(i[0])
            if i[1] % 2 == 0:
                ansli[i[0]] = ansli[po]
            else:
                if ansli[po] == 1:
                    ansli[i[0]] = 0
                else:
                    ansli[i[0]] = 1

for i in range(1, len(ansli)):
    print(ansli[i])