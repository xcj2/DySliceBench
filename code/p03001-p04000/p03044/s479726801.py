# -*- coding: utf-8 -*-
"""
D - Even Relation
https://atcoder.jp/contests/abc126/tasks/abc126_d

"""
import sys

from heapq import heappush, heappop


def dijkstra(adj, s):
    N = len(adj)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * N
    d = [float('inf')] * N
    d[s] = 0
    pq = []
    heappush(pq, (0, s))
    while pq:
        cost, u = heappop(pq)
        color[u] = BLACK
        if d[u] < cost:
            continue
        for v, cost in adj[u]:
            if color[v] == BLACK:
                continue
            if d[v] > d[u] + cost:
                d[v] = d[u] + cost
                heappush(pq, (d[v], v))
                color[v] = GRAY
    return d


def solve(N, path):
    adj = [[] for _ in range(N+1)]
    for f, t, w in path:
        adj[f].append([t, w])
        adj[t].append(([f, w]))
    dist = dijkstra(adj, 1)
    ans = []
    for d in dist[1:]:
        if d%2 == 0:
            ans.append(0)
        else:
            ans.append(1)
    return ans


def main(args):
    N = int(input())
    path = [[int(i) for i in input().split()] for _ in range(N-1)]
    ans = solve(N, path)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main(sys.argv[1:])

