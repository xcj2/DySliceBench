#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 998244353  # type: int

def solve(N: int, S: int, A: "List[int]"):
    dp = [[0] * 2 for _ in range(S + 1)]
    for i, v in enumerate(A):
        if v > S:
            continue
        for s in range(S + 1)[::-1]:
            if dp[s][0] > 0 and s + v <= S:
                dp[s + v][0] += dp[s][0]
                dp[s + v][1] += dp[s][0] * (N - i)
                dp[s + v][0] %= MOD
                dp[s + v][1] %= MOD
        dp[v][0] += i + 1
        dp[v][1] += (i + 1) * (N - i)
    print(dp[S][1] % MOD)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S, A)

if __name__ == '__main__':
    main()
