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


def warshall_floyd(graph):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
    return graph



n, m, l = LI()
graph = [[INF] * n for _ in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    a, b, c = LI()
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
for i in range(n):
    graph[i][i] = 0


supply_num_graph = [[INF] * n for _ in range(n)]
min_dist = warshall_floyd(graph)
for j in range(n):
    for k in range(j + 1, n):
        if min_dist[j][k] <= l:
            supply_num_graph[j][k] = 1
            supply_num_graph[k][j] = 1

supply_num_graph = warshall_floyd(supply_num_graph)
q = I()
for i in range(q):
    s, t = LI()
    if supply_num_graph[s - 1][t - 1] == INF:
        print(-1)
    else:
        print(supply_num_graph[s - 1][t - 1] - 1)


