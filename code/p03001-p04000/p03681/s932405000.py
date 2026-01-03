#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def fact(a):
    ans = 1
    while a > 0:
        ans *= a
        ans %= MOD
        a -= 1
    return ans


def solve(N: int, M: int):
    if abs(N-M) > 1:
        print(0)
        return
    if N == M:
        print(2*pow(fact(N), 2) % MOD)
    else:
        print(max(N, M)*pow(fact(min(N, M)), 2) % MOD)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)


if __name__ == '__main__':
    main()
