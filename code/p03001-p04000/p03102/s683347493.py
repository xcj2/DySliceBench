#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, C: int, B: "List[int]", A: "List[List[int]]"):
    print(sum(
        1 for Ai in A
        if sum(Aij * Bj for Aij, Bj in zip(Ai, B)) + C > 0
    ))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    A = [[int(next(tokens)) for _ in range(M)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, M, C, B, A)


if __name__ == '__main__':
    main()
