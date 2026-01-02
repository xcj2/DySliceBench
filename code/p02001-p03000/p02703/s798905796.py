# -*- coding: utf-8 -*-

import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

def dijkstra(nodes: list, src: int) -> list:
    from heapq import heappush, heappop

    N = len(nodes)
    MAX = 50**2
    res = list2d(N, MAX+1, INF)
    que = [(0, src, min(S, MAX))]
    res[src][min(S, MAX)] = 0
    while que:
        dist, u, coin  = heappop(que)
        if res[u][coin] < dist:
            continue
        if dist + D[u] < res[u][min(coin+C[u], MAX)]:
            res[u][min(coin+C[u], MAX)] = dist + D[u]
            heappush(que, (dist+D[u], u, min(coin+C[u], MAX)))
        for v, a, b in nodes[u]:
            if coin - a >= 0 and dist + b < res[v][coin-a]:
                res[v][coin-a] = dist + b
                heappush(que, (dist+b, v, coin-a))
    return res

N, M, S = MAP()
nodes = [[] for i in range(N)]
for _ in range(M):
    u, v, a, b = MAP()
    u -= 1; v -= 1
    nodes[u].append((v, a, b))
    nodes[v].append((u, a, b))
C = [0] * N
D = [0] * N
for i in range(N):
    c, d = MAP()
    C[i] = c
    D[i] = d

res = dijkstra(nodes, 0)
for i in range(1, N):
    print(min(res[i]))
