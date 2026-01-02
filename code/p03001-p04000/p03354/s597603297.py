#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, p: "List[int]", x: "List[int]", y: "List[int]"):
    pars = list(range(N))

    def getpar(n: int):
        if pars[n] == n:
            return n
        pars[n] = getpar(pars[n])
        return pars[n]

    def union(a: int, b: int):
        pars[getpar(a)] = getpar(b)

    for xi, yi in zip(x, y):
        union(xi - 1, yi - 1)
    print(sum(
        1
        for i in range(N)
        if getpar(p[i] - 1) == getpar(i)
    ))


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
