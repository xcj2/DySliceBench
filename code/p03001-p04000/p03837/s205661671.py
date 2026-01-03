import sys
input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import heapq
import bisect
import copy
import math
from collections import defaultdict

def warshall_floyd(d, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i * N +j] = min(d[i * N +j], d[i * N + k] + d[k * N + j])
    return d
MOD = 10**9 + 7
INF = 10**10

def dijkstra(n, graph, start):
    visited = [0 for i in range(n)]
    cost = [INF for i in range(n)]
    parents = [[] for i in range(n)]
    visited[start] = 1
    cost[start] = 0
    # cur = start
    pq = []
    for g in graph[start]:
        heapq.heappush(pq, g)
    while(pq):
        nxt = heapq.heappop(pq)
        # print(nxt)
        # print(cost)
        tcos, cur, tdist = nxt
        if cost[tdist] == cost[cur] + tcos:
            parents[tdist].append(cur)
        elif cost[tdist] > cost[cur] + tcos:
            cost[tdist] = cost[cur] + tcos
            parents[tdist] = [cur]
            for g in graph[tdist]:
                heapq.heappush(pq, g)

    res = []
    # print(parents)
    for i, par in enumerate(parents):
        for ppar in par:
            res.append((i, ppar))

    return res


def main():
    n, m = getlist()
    graph = [[] for i in range(n)]

    for i in range(m):
        a,b,c = getlist()
        graph[a-1].append((c, a-1, b-1))
        graph[b - 1].append((c, b-1, a-1))

    cands = []

    for start in range(n):
        res = dijkstra(n, graph, start)
        # print(res)
        for re in res:
            if re[0] < re[1]:
                cands.append(re)
            else:
                cands.append((re[1], re[0]))

    print(m - len(list(set(cands))))

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""