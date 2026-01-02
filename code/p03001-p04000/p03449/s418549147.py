#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, A: "List[List[int]]"):
    print(max(
        sum(A[0][:i + 1]) + sum(A[1][i:])
        for i in range(N)
    ))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(2)]  # type: "List[List[int]]"
    solve(N, A)


if __name__ == '__main__':
    main()
