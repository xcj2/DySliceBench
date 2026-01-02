from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 18
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
mod = 1000000007


n, m, p = LI()
G = [[] for _ in range(n)]
for i in range(m):
    a, b, c = LI()
    G[a - 1] += [(b - 1, c - p)]


def bellman_ford(G, start=0):
    n = len(G)
    costs = [-INF] * n
    costs[0] = 0
    v_nows = set([start])
    for _ in range(n):
        v_changeds = set()
        for u in v_nows:
            for v, c in G[u]:
                if costs[u] + c > costs[v]:
                    costs[v] = costs[u] + c
                    v_changeds.add(v)
        v_nows = v_changeds
    if not v_changeds:
        return costs[n - 1]

    for i in v_nows:
        costs[i] = -INF
    que = deque(v_nows)
    while que:
        u = que.popleft()
        for v, cost in G[u]:
            if costs[v] != -INF:
                costs[v] = -INF
                que += [v]
    return costs[n - 1]


cost = bellman_ford(G, 0)
if cost == -INF:
    print(-1)
else:
    print(max(0, cost))