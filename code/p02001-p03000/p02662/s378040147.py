#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 998244353  # type: int
INV = pow(2, MOD - 2, MOD)

def calc_fraction_mod(numerator):
    '''
        returns numerator / denominator (mod MOD)
    '''
    #inv = pow(denominator, MOD - 2, MOD)
    return numerator * INV % MOD


def solve(N: int, S: int, A: "List[int]"):
    A.sort()
    dp = [0] * (S + 1)
    dp[0] = pow(2, N, MOD)
    for i, a in enumerate(A):
        for s in range(S + 1)[::-1]:
            if dp[s] == 0:
                continue
            if s + a <= S:
                dp[s + a] += calc_fraction_mod(dp[s])
                dp[s + a] %= MOD
    print(dp[S])

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
