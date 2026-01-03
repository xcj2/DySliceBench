#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(N: int, M: int):
    def fact(n):
        ret = 1
        for i in range(2, n + 1):
            ret *= i
            ret %= MOD
        return ret
    if abs(N - M) > 1:
        ret = 0
    else:
        ret = fact(N) * fact(M)
        if N == M:
            ret *= 2
    print(ret % MOD)
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
