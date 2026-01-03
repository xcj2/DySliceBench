#!/usr/bin/env python3
from functools import reduce
import sys

MOD = 1000000007  # type: int


def solve(N: int, M: int):
    if M > N:
        M, N = N, M
    if M + 1 < N:
        print(0)
        return
    mf = reduce(lambda a, b: a * b % MOD, range(1, M + 1), 1)
    if M == N:
        ans = mf * mf % MOD * 2 % MOD
    else:
        ans = mf * mf % MOD * N % MOD
    print(ans)


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
