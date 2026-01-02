#!/usr/bin/env python3
import copy
import sys
import numpy as np

MOD = 1000000007  # type: int


def debug(s):
    print(s)


def solve(N: int, K: int, a):
    dp = np.zeros((N + 1, K + 1), dtype=np.int64)
    dp[0, 0] = 1
    for i in range(1, N + 1):
        ai = a[i - 1]
        ndp = np.cumsum(dp[i - 1, :])
        dp[i, :] = ndp
        dp[i, ai + 1 :] -= ndp[: -ai - 1]
        dp[i, :] %= MOD
    return dp[N, K]


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = np.array([int(next(tokens)) for _ in range(N)], dtype=np.int64)
    print(solve(N, K, a))


if __name__ == "__main__":
    main()
