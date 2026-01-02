#!/usr/bin/env python3
import sys


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    total_value = sum(v)
    dp = [[float("inf")] * (total_value + 1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 0

    for i in range(N):
        for j in range(1, total_value+1):
            if j - v[i] >= 0:
                dp[i+1][j] = min(
                    dp[i][j],
                    dp[i][j-v[i]] + w[i]
                )
            else:
                dp[i+1][j] = dp[i][j]

    weight = 0
    res = 0
    for j in range(total_value+1):
        if dp[-1][j] <= W:
            weight = dp[-1][j]
            res = j
    print(res)


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
