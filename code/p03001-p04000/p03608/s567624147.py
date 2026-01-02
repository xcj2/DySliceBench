#!/usr/bin/env python3
from itertools import permutations
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, R: int, r: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]"):
    inf = float("inf")
    md = [[inf] * N for _ in range(N)]
    for i in range(N):
        md[i][i] = 0
    for Ai, Bi, Ci in zip(A, B, C):
        Ai -= 1
        Bi -= 1
        md[Ai][Bi] = md[Bi][Ai] = Ci
    for k in range(N):
        for i in range(N):
            for j in range(N):
                md[i][j] = min(md[i][j], md[i][k] + md[k][j])

    def dist(path):
        return sum(md[p1 - 1][p2 - 1] for p1, p2 in zip(path, path[1:]))

    print(min(dist(path) for path in permutations(r)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    r = [int(next(tokens)) for _ in range(R)]  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, R, r, A, B, C)


if __name__ == '__main__':
    main()
