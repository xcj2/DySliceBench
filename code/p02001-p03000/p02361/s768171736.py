#!/usr/bin/python3

import heapq
import os
import sys


def main():
    V, E, R = read_ints()
    G = [dict() for _ in range(V)]
    for _ in range(E):
        s, t, d = read_ints()
        G[s][t] = d
    print(*solve(V, E, R, G), sep='\n')


def solve(V, E, R, G):
    dists = [-1] * V
    q = []
    heapq.heappush(q, (0, R))
    while q:
        d, i = heapq.heappop(q)
        if dists[i] != -1:
            continue
        dists[i] = d
        for j, e in G[i].items():
            if dists[j] == -1:
                heapq.heappush(q, (d + e, j))
    return ['INF' if d == -1 else d for d in dists]


###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


if __name__ == '__main__':
    main()

