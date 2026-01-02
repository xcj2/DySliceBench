# coding: utf-8
"""docstring"""


def arr2d(d1, d2, init=None):
    return [[init for i in range(d2)] for j in range(d1)]


def solve(N, W):
    v = [None] * N
    w = [None] * N
    for i in range(N):
        v[i], w[i] = map(int, input().split())

    # dp[i][j]: item 0..i ??????weight sum <= j ??¨????????????????????¶????????§????????§???value sum
    # (i: 0..N-1, j: 0..W)
    dp = arr2d(N, W + 1, 0)
    # i==0
    for j in range(0, W + 1):
        dp[0][j] = (j // w[0]) * v[0]
    for i in range(1, N):
        for j in range(0, W + 1):
            dp[i][j] = dp[i-1][j]
            if j >= w[i]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-w[i]] + v[i])
                dp[i][j] = max(dp[i][j], dp[i][j-w[i]] + v[i])
    return dp[-1][-1]


def main():
    n, w = map(int, input().split())
    print(solve(n, w))


if __name__ == "__main__":
    main()