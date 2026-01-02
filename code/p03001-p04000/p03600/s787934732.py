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
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    return 1




n = I()
graph = [[INF] * n for _ in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(n):
    edges = LI()
    for j in range(n):
        graph[i][j] = edges[j]
        graph[j][i] = edges[j]



if warshall_floyd(graph):
    print(-1)
else:
    ret = 0
    for i in range(n):
        for j in range(i + 1, n):
            if i == j:
                continue
            for k in range(n):
                if k != i and k != j and graph[i][k] + graph[k][j] == graph[i][j]:
                        break
            else:
                ret += graph[i][j]
    print(ret)