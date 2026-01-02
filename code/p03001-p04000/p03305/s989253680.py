from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007

def dijkstra(G, s=0):
    n = len(G)
    que = [(0, s)]
    dist = [INF] * n
    dist[s] = 0
    while que:
        min_dist, u = heappop(que)
        if min_dist > dist[u]:
            continue
        for v, c in G[u]:
            if dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                heappush(que, (dist[u] + c, v))
    return dist

n, m, s, t = LI()
s-=1
t-=1
G1 = [[] for _ in range(n)]
G2 = [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = LI()
    G1[u-1] += [(v-1, a)]
    G1[v - 1] += [(u - 1, a)]
    G2[u-1] += [(v-1, b)]
    G2[v - 1] += [(u - 1, b)]

y_cost = dijkstra(G1, s)
s_cost = dijkstra(G2, t)
ans = [0] * n
ret = INF
for i in range(n - 1, -1, -1):
    ret = min(ret, s_cost[i] + y_cost[i])
    ans[i] = 10**15 - ret

print(*ans, sep="\n")

