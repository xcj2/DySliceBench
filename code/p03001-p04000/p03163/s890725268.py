#!/usr/bin/env python3
import sys


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    dp = [[0] * (N + 1) for _ in range(W+1)]

    for i in range(1, W+1):
        for j in range(N):
            if i - w[j] >= 0:
                dp[i][j+1] = max(dp[i][j], dp[i-1][j], dp[i-w[j]][j] + v[j])
            else:
                dp[i][j+1] = max(dp[i][j], dp[i-1][j])

    print(dp[-1][-1])


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
