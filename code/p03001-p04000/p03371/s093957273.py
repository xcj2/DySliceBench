#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int, Y: int):
    print(min(
        A * X + B * Y + min(X, Y) * min(0, C * 2 - A - B),
        max(X, Y) * (C * 2),
    ))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(A, B, C, X, Y)


if __name__ == '__main__':
    main()
