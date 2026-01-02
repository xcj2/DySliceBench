#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

MOD = 1000000007  # type: int


def solve(N: int, M: int, a: "List[int]"):
    sa = set(a)
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in sa:
            continue
        c = dp[i - 1]
        if i >= 2:
            c += dp[i - 2]
        dp[i] = c % MOD
    print(dp[N])


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
