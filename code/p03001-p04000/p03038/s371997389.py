#!/usr/bin/env python3
from collections import defaultdict
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    d = defaultdict(int)
    for Bi, Ci in zip(B, C):
        d[Ci] += Bi

    k = [0] * N
    i = 0
    for key in sorted(d.keys(), reverse=True):
        newi = min(N, i + d[key])
        for j in range(i, newi):
            k[j] = key
        i = newi
        if newi > N:
            break
    print(sum(sorted(A + k, reverse=True)[:N]))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)


if __name__ == '__main__':
    main()
