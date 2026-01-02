#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, L: "List[int]", R: "List[int]"):
    ml = 1
    mr = N
    for Li, Ri in zip(L, R):
        ml = max(ml, Li)
        mr = min(mr, Ri)

    print(max(mr - ml + 1, 0))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, M, L, R)


if __name__ == '__main__':
    main()
