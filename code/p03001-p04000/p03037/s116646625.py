#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, M: int, L: "List[int]", R: "List[int]"):
    print(max(min(R)-max(L)+1, 0))
    return


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
