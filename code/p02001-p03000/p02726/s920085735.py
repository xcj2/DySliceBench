#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)

import heapq
from collections import defaultdict
INF = float("inf")


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, s, t, w=1):
        self.E[s].append((t, w))
        self.E[t].append((s, w))


def shortestPath(g: Graph, s: int):
    # 返り値 (dist, prev)
    # dist: 始点からの距離が格納されたリスト
    # prev: 始点から最短経路で移動する場合、各頂点に至る前の頂点のリスト
    dist = [INF]*g.N
    dist[s] = 0

    prev = [None]*g.N
    Q = []
    heapq.heappush(Q, (dist[s], s))

    while len(Q) > 0:
        _, u = heapq.heappop(Q)
        for v, w in g.E[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(Q, (dist[v], v))
    return dist, prev


def solve(N: int, X: int, Y: int):

    g = Graph(N)
    for i in range(1, N):
        g.add_edge(i-1, i)
    g.add_edge(X-1, Y-1)

    ans = [0]*N
    for i in range(N):
        dist, prev = shortestPath(g, i)
        for j, d in enumerate(dist):
            if i < j:
                ans[d] += 1
    print(*ans[1:], sep="\n")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, X, Y)


if __name__ == '__main__':
    main()
