from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
from re import split
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy
import re

sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


n, x, y = LI()
G = [[] for _ in range(n)]
ans = [0] * (n - 1)
for i in range(n - 1):
    G[i] += [i + 1]
    G[i + 1] += [i]

for j in range(n):
    q = [j]
    par = [-1] * n
    dist = [-1] * n
    dist[j] = 0
    while q:
        u = q.pop()
        for v in G[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q += [v]
    flag = [0] * n
    q2 = [x - 1, y - 1]
    dist[x - 1] = min(dist[x - 1], dist[y - 1] + 1)
    dist[y - 1] = min(dist[y - 1], dist[x - 1] + 1)
    while q2:
        a = q2.pop()
        for b in G[a]:
            if dist[a] + 1 < dist[b]:
                dist[b] = dist[a] + 1
                q2 += [b]

    for k in range(n):
        if k == j: 
            continue
        else:
            ans[dist[k] - 1] += 1


for l in ans:
    print(l // 2)



