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
from operator import mul
from functools import reduce


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n, m = LI()
graph = [[] for _ in range(n)]
for u, v in LIR(m):
    graph[u - 1] += [v - 1]


s, t = LI()
dist = [[INF for _ in range(3)] for _ in range(n)]
dist[s - 1][0] = 0
que = deque([(s - 1, 0)])
while que:
    cur, cost = que.popleft()
    for nxt in graph[cur]:
        if cost + 1 < dist[nxt][(cost + 1) % 3]:
            dist[nxt][(cost + 1) % 3] = cost + 1
            que += [(nxt, cost + 1)]



if dist[t - 1][0] == INF:
    print(-1)
else:
    print(dist[t - 1][0] // 3)