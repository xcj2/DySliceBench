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


sys.setrecursionlimit(2147483647)
INF = 1 << 100
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


n, m = LI()
G = [[] for _ in range(n)]
for _ in range(m):
    l, r, c = LI()
    G[l - 1] += [(r - 1, c)]


for i in range(n - 1):
    G[i + 1] += [(i, 0)]


def dijkstra(G, s=0):
    hq = [(0, s)]
    dist = [INF] * n
    dist[s] = 0
    checked = [0] * n
    while hq:
        min_dist, u = heappop(hq)
        if checked[u]:
            continue
        checked[u] = 1
        for v, c in G[u]:
            if checked[v]:
                continue
            elif dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                heappush(hq, (dist[u] + c, v))
    return dist


ans = dijkstra(G)[-1]
if ans == INF:
    print(-1)
else:
    print(ans)
