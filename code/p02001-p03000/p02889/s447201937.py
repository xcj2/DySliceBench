# -*- coding: utf-8 -*-
import random
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

INF = 10**11

def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def warshall_floyd(g):
    d = g
    N = len(g)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def slv(N, M, L, ABC, Q, ST):
    g = [[INF]*(N) for _ in range(N)]
    for i in range(N):
        g[i][i] = 0
    for a, b, c in ABC:
        if c > L:
            continue
        g[a-1][b-1] = c
        g[b-1][a-1] = c

    d = g
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    gg = [[INF]*(N) for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if d[u][v] <= L:
                gg[u][v] = 1

    d = gg
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

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
