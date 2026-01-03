#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, x: "List[int]", y: "List[int]"):
    par = [-1] * N

    def getroot(a: int):
        if par[a] != -1:
            par[a] = getroot(par[a])
            return par[a]
        else:
            return a

    def union(a: int, b: int):
        par[getroot(b)] = getroot(a)

    xpts = sorted((xi, i) for i, xi in enumerate(x))
    ypts = sorted((yi, i) for i, yi in enumerate(y))
    edges = [
        (xj - xi, i, j) for (xi, i), (xj, j) in zip(xpts, xpts[1:])
    ] + [
        (yj - yi, i, j) for (yi, i), (yj, j) in zip(ypts, ypts[1:])
    ]
    edges.sort()
    ans = 0
    for cost, i, j in edges:
        if getroot(i) == getroot(j):
            continue
        union(i, j)
        ans += cost
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)


if __name__ == '__main__':
    main()
