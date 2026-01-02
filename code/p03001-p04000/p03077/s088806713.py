#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int, C: int, D: int, E: int):
    print(-(-N // min(A, B, C, D, E)) + 4)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    solve(N, A, B, C, D, E)


if __name__ == '__main__':
    main()
