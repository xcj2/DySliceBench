#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
import sys


def d(i: int, j: int, X: int, Y: int):
    res = min(
        abs(i - j),
        abs(i - X) + 1 + abs(Y - j),
        abs(i - Y) + 1 + abs(X - j),
    )
    return res


def solve(N: int, X: int, Y: int):
    X -= 1
    Y -= 1
    ctr = Counter(
        d(i, j, X, Y)
        for i, j in combinations(range(N), 2)
    )
    for di in range(1, N):
        print(ctr[di])


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
