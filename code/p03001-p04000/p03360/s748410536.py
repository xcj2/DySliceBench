#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(A: int, B: int, C: int, K: int):
    a = sorted([A, B, C])
    print(a[0]+a[1]+a[2]*(2**K))

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
