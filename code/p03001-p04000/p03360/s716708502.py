#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(A: int, B: int, C: int, K: int):
    print(A + B + C + max(A, B, C) * (2 ** K - 1))


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
