#!/usr/bin/env python3
import sys
from itertools import accumulate
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(N: int, a: "List[int]"):

    acc = [0]+list(accumulate(a))

    dp = [[-1]*N for _ in range(N)]

    def rec(l, r):
        if dp[l][r] > 0:
            return dp[l][r]
        if l == r:
            return 0

        wa = acc[r+1]-acc[l]
        ans = INF
        for k in range(l, r):
            ans = min(rec(l, k) + rec(k+1, r), ans)
        dp[l][r] = ans + wa
        return dp[l][r]

    print(rec(0, N-1))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
