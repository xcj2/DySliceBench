#!/usr/bin/python3

import os
import sys


def main():
    N = read_int()
    E = []
    G = [dict() for _ in range(N)]

    for _ in range(N - 1):
        a, b = read_ints()
        a -= 1
        b -= 1
        E.append((a, b))
        G[a][b] = -1
        G[b][a] = -a

    K, C = solve(N, E, G)
    print(K)
    for c in C:
        print(c + 1)


def solve(N, E, G):
    K = max([len(d) for d in G])

    q = [(-1, 0)]
    while q:
        p, i = q.pop()

        used = -1
        if p != -1:
            used = G[p][i]

        c = 0
        for j in G[i]:
            if j == p:
                continue
            if c == used:
                c += 1
            G[i][j] = c
            G[j][i] = c
            q.append((i, j))
            c += 1

    C = [-1] * len(E)
    for i, (a, b) in enumerate(E):
        C[i] = G[a][b]
    return K, C


###############################################################################

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
