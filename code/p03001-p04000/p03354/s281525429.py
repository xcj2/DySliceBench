#!/usr/bin/env python3
import sys
INF = float("inf")
from collections import defaultdict


def solve(N: int, M: int, p: "List[int]", x: "List[int]", y: "List[int]"):

    par = list(range(N+1))

    def root(i):
        if par[i] == i:
            return i
        else:
            par[i] = root(par[i])
            return par[i]

    def same(x, y):
        return root(x) == root(y)

    def unite(x, y):
        x = root(x)
        y = root(y)
        if x != y:
            par[x] = y

    for i in range(M):          # O(M)
        unite(x[i], y[i])

    counter = 0
    for i in range(N):
        if same(p[i], i+1):
            counter += 1
    print(counter)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, p, x, y)


if __name__ == '__main__':
    main()
