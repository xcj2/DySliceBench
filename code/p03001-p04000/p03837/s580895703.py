#!/usr/bin/env pypy3

import collections
import itertools


INF = 10 ** 8
UNDEF = -1


def floyd_warshall_undirected(num_vs, edges):
    n = num_vs
    dist = [[INF for _ in range(n)] for _ in range(n)]
    pred = [[UNDEF for _ in range(n)] for _ in range(n)]
    for u in range(n):
        dist[u][u] = 0
    for (u, v), c in edges.items():
        dist[u][v] = c
        dist[v][u] = c
        pred[u][v] = u
        pred[v][u] = v
    for t, u, v in itertools.product(range(n), repeat=3):
        nl = dist[u][t] + dist[t][v]
        if nl < dist[u][v]:
            dist[u][v] = nl
            pred[u][v] = pred[t][v]
    return dist, pred


def construct_shortest_path(s, t, pred):
    path = collections.deque()
    path.appendleft(t)
    while t != s:
        t = pred[s][t]
        path.appendleft(t)
    return list(path)


def main():
    n, m = (int(x) for x in input().split())
    edges = dict()
    used = dict()
    for _ in range(m):
        a, b, c = (int(x) for x in input().split())
        a -= 1
        b -= 1
        a, b = min(a, b), max(a, b)
        edges[(a, b)] = c
        used[(a, b)] = False
    _, pred = floyd_warshall_undirected(n, edges)
    for s in range(n):
        for t in range(s + 1, n):
            path = construct_shortest_path(s, t, pred)
            for u, v in zip(path[:-1], path[1:]):
                u, v = min(u, v), max(u, v)
                used[(u, v)] = True
    ans = m - sum(used.values())
    print(ans)


if __name__ == '__main__':
    main()
