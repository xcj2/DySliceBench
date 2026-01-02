#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


def solve(A: int, B: int, C: int, K: int):
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(A, B, C, K)


if __name__ == '__main__':
    main()
