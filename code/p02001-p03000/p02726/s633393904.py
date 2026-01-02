#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)

import heapq
from collections import defaultdict
INF = float("inf")


def solve(N: int, X: int, Y: int):
    if X > Y:
        X, Y = Y, X
    ans = [0]*N
    for i in range(N):
        for j in range(i+1, N):
            d = min(abs(j-i), abs(i-(X-1))+1+abs(j-(Y-1)))
            ans[d] += 1
    print(*ans[1:], sep="\n")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, X, Y)


if __name__ == '__main__':
    main()
