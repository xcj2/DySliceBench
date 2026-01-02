#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, T: int, A: int, H: "List[int]"):
    print(1 + min(range(N), key=lambda i: abs(T - H[i] * 0.006 - A)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, A, H)


if __name__ == '__main__':
    main()
