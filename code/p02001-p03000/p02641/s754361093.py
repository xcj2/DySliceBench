#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


def solve(X: int, N: int, p: "List[int]"):
    kouho = list((set(v + 1 for v in p) | set(v - 1 for v in p)) - set(p))
    kouho.sort()
    diff = INF
    ans = X
    for v in kouho:
        cdiff = abs(v - X)
        if diff > cdiff:
            diff = cdiff
            ans = v
    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(X, N, p)


if __name__ == '__main__':
    main()
