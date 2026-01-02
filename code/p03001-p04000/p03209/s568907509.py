#!/usr/bin/env python3
import sys


def solve(N: int, X: int):
    # a_0 = 1
    # a_{n+1} = 2 * a_n + 3
    # b_0 = 1
    # b_{n+1} = 2 * b_n + 1

    # a_n = 2**(n+2) - 3
    # b_n = 2**(n+1) - 1
    def f(N: int, X: int):
        aN = 2 ** (N + 2) - 3
        bN = 2 ** (N + 1) - 1
        if X >= aN:
            return bN

        aN1 = 2 ** ((N - 1) + 2) - 3

        ans = 0

        X -= 1
        if X <= 0:
            return ans

        ans += f(N - 1, X)
        X -= aN1
        if X <= 0:
            return ans

        ans += 1
        X -= 1
        if X <= 0:
            return ans

        ans += f(N - 1, X)
        X -= aN1
        if X <= 0:
            return ans

        X -= 1
        if X <= 0:
            return ans

        assert False

    print(f(N, X))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(N, X)


if __name__ == '__main__':
    main()
