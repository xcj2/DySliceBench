#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, X: int, m: "List[int]"):
    print(N + (X - sum(m)) // min(m))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    m = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, m)


if __name__ == '__main__':
    main()
