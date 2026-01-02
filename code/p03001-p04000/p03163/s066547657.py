#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    DP = [[0]*(W+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(W+1):
            DP[i+1][j] = DP[i][j]
            if j-w[i] >= 0:
                DP[i+1][j] = max(DP[i+1][j], DP[i][j-w[i]]+v[i])
    print(DP[N][W])
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
