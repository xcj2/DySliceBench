#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def solve(S: str):
    dp = [0]*13
    dp[0] = 1
    ep = [0]*13
    zero = [0]*13
    for c in S:
        ep[:] = zero
        for i in range(10):
            if c != "?" and int(c) != i:
                continue
            for j in range(13):
                ep[(10*j+i) % 13] += dp[j]
                ep[(10*j+i) % 13] %= MOD
        dp, ep = ep, dp

    print(dp[5])

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
