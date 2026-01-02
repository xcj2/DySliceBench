#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def solve(N: int, M: int, a: "List[int]"):

    # 0段目一通り
    dp = [None]*(N+1)
    dp[0] = 1
    for i in a:
        dp[i] = 0
    for i in range(1, N+1):
        # print(i, dp)
        if dp[i] == None:
            b = dp[i-1]
            if i-2 >= 0:
                b += dp[i-2]
                b %= MOD
            dp[i] = b
    print(dp[N])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, a)


if __name__ == '__main__':
    main()
