#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")

MOD = 1000000007  # type: int


def solve(N: int, K: int, a: "List[int]"):

    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        acc = [0] + list(accumulate(dp[i-1]))
        for j in range(K+1):
            dp[i][j] = acc[j+1] - acc[max(j-a[i-1], 0)]
            dp[i][j] %= MOD
    print(dp[N][K])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)


if __name__ == '__main__':
    main()
