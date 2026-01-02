#!/usr/bin/env python3
import sys
from collections import defaultdict
INF = float("inf")


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):

    L = 10**5+1
    DP = [[INF]*(L) for _ in range(N+1)]
    for i in range(N+1):
        DP[i][0] = 0

    for i in range(N):
        for j in range(L):
            DP[i+1][j] = DP[i][j]
            if 0 <= j-v[i] < L:
                DP[i+1][j] = min(DP[i+1][j], DP[i][j-v[i]]+w[i])

    for j in range(L-1, -1, -1):
        if DP[N][j] <= W:
            print(j)
            return

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, W, w, v)


if __name__ == '__main__':
    main()
