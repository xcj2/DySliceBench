# -*- coding: utf-8 -*-
import heapq
import sys
from collections import defaultdict

input = sys.stdin.buffer.readline
INF = 2**62-1


def read_int_n():
    return list(map(int, input().split()))


def read_str_n():
    return list(map(str, input().split()))


def Dijkstra(g, s):
    d = defaultdict(lambda: INF)
    d[s] = 0
    q = []
    heapq.heappush(q, (d[s], s))

    prev = {}
    done = set()
    while q:
        c, u = heapq.heappop(q)
        if u in done:
            continue
        done.add(u)
        for v in g[u]:
            alt = g[u][v] + d[u]
            if d[v] > alt:
                d[v] = alt
                prev[v] = u
                heapq.heappush(q, (d[v], v))
    return d

def slv(N, M, S, UVAB, CD):
    g = defaultdict(dict)
    V = {}
    for u, v, a, b in UVAB:
        g[u][v] = (a, b)
        g[v][u] = (a, b)

    for i, (c, d) in enumerate(CD, 1):
        V[i] = (c, d)

    MA = (N-1)*max(a for u, v, a, b in UVAB)
    S = min(S, MA)
    d = [[INF] * (MA+1) for _ in range(N+1)]
    d[1][S] = 0
    q = []
    heapq.heappush(q, (d[1][S], (1, S)))
    while q:
        c, (u, s) = heapq.heappop(q)
        if d[u][s] < c:
            continue
        c, dd = V[u]
        if s != MA:
            m = min(MA, s+c)
            alt = d[u][s] + dd
            if d[u][m] > alt:
                d[u][m] = alt
                heapq.heappush(q, (d[u][m], (u, m)))
        for v in g[u]:
            a, b = g[u][v]
            alt = b + d[u][s]
            m = s - a
            if m >= 0 and d[v][m] > alt:
                d[v][m] = alt
                heapq.heappush(q, (d[v][m], (v, m)))

    for i in range(2, N+1):
        print(min(d[i]))


def main():
    N, M, S = read_int_n()
    UVAB = [read_int_n() for _ in range(M)]
    CD = [read_int_n() for _ in range(N)]
    (slv(N, M, S, UVAB, CD))


if __name__ == '__main__':
    main()
