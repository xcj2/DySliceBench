#!/usr/bin/env python3
import sys


def solve(A: int, B: int, K: int):
    for i in sorted(
            set(range(A, min(B + 1, A + K))) |
            set(range(max(A, B + 1 - K), B + 1))):
        print(i)


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
