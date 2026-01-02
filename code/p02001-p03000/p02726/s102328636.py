#!usr/bin/env pypy3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def LS(): return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


sys.setrecursionlimit(1000000)


def main():
    N, X, Y = LI()
    X -= 1
    Y -= 1
    dist = [[N] * N for _ in range(N)]

    q = deque()
    for i in range(N):
        q.append(i)
        dist[i][i] = 0
        while q:
            u = q.popleft()
            if u < N - 1:
                if dist[i][u + 1] > dist[i][u] + 1:
                    q.append(u + 1)
                    dist[i][u + 1] = dist[i][u] + 1
            if u >= 1:
                if dist[i][u - 1] > dist[i][u] + 1:
                    q.append(u - 1)
                    dist[i][u - 1] = dist[i][u] + 1
            if u == X:
                if dist[i][Y] > dist[i][u] + 1:
                    q.append(Y)
                    dist[i][Y] = dist[i][u] + 1
            if u == Y:
                if dist[i][X] > dist[i][u] + 1:
                    q.append(X)
                    dist[i][X] = dist[i][u] + 1

    cnt = [0] * N

    for i in range(N):
        for j in range(i + 1, N):
            cnt[dist[i][j]] += 1

    for i in cnt[1:]:
        print(i)


main()
