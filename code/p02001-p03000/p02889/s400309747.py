# -*- coding: utf-8 -*-
import random
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

INF = 2**62-1

def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def warshall_floyd(g):
    N = len(g)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    return g


def slv(N, M, L, ABC, Q, ST):
    g = [[INF]*(N) for _ in range(N)]

    for a, b, c in ABC:
        if c > L:
            continue
        g[a-1][b-1] = c
        g[b-1][a-1] = c

    d = warshall_floyd(g)

    gg = [[INF]*(N) for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if d[u][v] <= L:
                gg[u][v] = 1

    d = warshall_floyd(gg)

    for s, t in ST:
        c = d[s-1][t-1]
        if c != INF:
            print(c-1)
        else:
            print(-1)


def main():
    N, M, L = read_int_n()
    ABC = [read_int_n() for _ in range(M)]
    Q = read_int()
    ST = [read_int_n() for _ in range(Q)]

    (slv(N, M, L, ABC, Q, ST))


if __name__ == '__main__':
    main()
