#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(A: int, B: int, K: int):

    if A <= K:
        a = 0
        b = max(B-(K-A), 0)
    else:
        a = A-K
        b = B
    print(a, b, sep=" ")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(A, B, K)


if __name__ == '__main__':
    main()
