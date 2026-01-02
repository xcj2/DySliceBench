#!/usr/bin/python3

import os
import sys


INF = 2 * 10 ** 9 + 1


def main():
    V, E = read_ints()
    G = [[INF] * V for _ in range(V)]
    for _ in range(E):
        s, t, d = read_ints()
        G[s][t] = d
    ans = solve(V, E, G)
    if not ans:
        print('NEGATIVE CYCLE')
    else:
        for a in ans:
            print(*a)


def solve(V, E, G):
    dists = [[INF] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i == j:
                dists[i][j] = 0
            elif G[i][j] != INF:
                dists[i][j] = G[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if (dists[i][k] != INF and dists[k][j] != INF and
                    dists[i][j] > dists[i][k] + dists[k][j]):
                    dists[i][j] = dists[i][k] + dists[k][j]

    for i in range(V):
        if dists[i][i] < 0:
            return None

    for i in range(V):
        for j in range(V):
            if dists[i][j] == INF:
                dists[i][j] = 'INF'
    return dists


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

