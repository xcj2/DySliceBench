#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def bit_sum(n):
    wa = 0
    while n > 0:
        wa += n & 1
        n >>= 1
    return wa


def bit(n, k):
    return (n >> k) & 1


def solve(N: int, a: "List[List[int]]"):
    dp = [0]*(1 << N)
    dp[0] = 1
    for S in range(1, 1 << N):
        i = bit_sum(S)
        for j in range(N):
            if bit(S, j) == 1 and a[i-1][j] == 1:
                dp[S] = (dp[S]+dp[S ^ (1 << j)]) % MOD
    print(dp[(1 << N)-1])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [[int(next(tokens)) for _ in range(N)]
         for _ in range(N)]  # type: "List[List[int]]"
    solve(N, a)


if __name__ == '__main__':
    main()
