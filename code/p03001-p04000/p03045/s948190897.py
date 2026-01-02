#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


sys.setrecursionlimit(1000000)


def solve(N: int, M: int, X: "List[int]", Y: "List[int]", Z: "List[int]"):
    par = list(range(N))

    def getpar(n: int):
        if par[n] == n:
            return n
        par[n] = getpar(par[n])
        return par[n]

    def union(a: int, b: int):
        par[getpar(b)] = getpar(a)

    for Xi, Yi in zip(X, Y):
        Xi -= 1
        Yi -= 1
        union(Xi, Yi)

    print(len({getpar(i) for i in range(N)}))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    Z = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        Z[i] = int(next(tokens))
    solve(N, M, X, Y, Z)


if __name__ == '__main__':
    main()
