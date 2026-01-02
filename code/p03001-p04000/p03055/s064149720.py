from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left, bisect_right
import random
from itertools import permutations, accumulate, combinations
import sys
import string



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
mod = 10 ** 9 + 7



n = I()
graph = [[] for _ in range(n)]
for k in range(n - 1):
    a, b = LI()
    graph[a - 1] += [b - 1]
    graph[b - 1] += [a - 1]


def bfs(v):
    que = deque([v])
    dist = [INF] * n
    dist[v] = 0
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if dist[cur] + 1 < dist[nxt]:
                dist[nxt] = dist[cur] + 1
                que += [nxt]
    return dist



def double_sweep():
    dist = bfs(0)
    ret = -1
    for i in range(n):
        if dist[i] > ret:
            ret = dist[i]
            u = i
    return max(bfs(u))



if (double_sweep() + 1) % 3 == 2:
    print('Second')
else:
    print('First')