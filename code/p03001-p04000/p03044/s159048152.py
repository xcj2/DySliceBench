from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor


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


n = I()
graph = [[] for _ in range(n)]
for a, b, cost in LIR(n-1):
    graph[a-1] += [(b-1, cost)]
    graph[b-1] += [(a-1, cost)]



color = [0] * n
color[0] = 0
dist = [-1] * n
dist[0] = 0
que = deque([0])
while que:
    cur = que.pop()
    for nxt, cost in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + cost
            color[nxt] = dist[nxt] % 2
            que += [nxt]


for i in range(n):
    print(color[i])