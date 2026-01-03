#!/usr/bin/env python3
import sys
import heapq
from collections import defaultdict
INF = float("inf")


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, s, t, w):
        self.E[s].append([t, w])
        self.E[t].append([s, w])


def shortestPath(g: Graph, s: int):
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


def solve(N: int, M: int, a: "List[int]", b: "List[int]", c: "List[int]"):

    g = Graph(N)
    flag = {}
    for aa, bb, cc in zip(a, b, c):
        g.add_edge(aa-1, bb-1, cc)

        if aa > bb:
            aa, bb = bb, aa
        flag[(aa-1, bb-1)] = False

    for i in range(N-1):
        dist, prev = shortestPath(g, i)

        for j, p in enumerate(prev):
            if p == None:
                continue
            a, b = p, j
            if b < a:
                a, b = j, p
            flag[(a, b)] = True
    tot = 0
    for k in flag:
        if flag[k] == False:
            tot += 1
    print(tot)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, a, b, c)


if __name__ == '__main__':
    main()
