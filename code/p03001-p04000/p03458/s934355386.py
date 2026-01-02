#!/usr/bin/env python3
from itertools import chain
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, K: int, x: "List[int]", y: "List[int]", c: "List[str]"):
    imos = [[0] * (2 * K) for _ in range(2 * K)]

    def sq(x1: int, y1: int, x2: int, y2: int):
        x1 %= 2 * K
        x2 %= 2 * K
        y1 %= 2 * K
        y2 %= 2 * K
        if x1 > x2:
            imos[y1][0] += 1
            imos[y2][0] -= 1
            if y1 > y2:
                imos[0][0] += 1
        if y1 > y2:
            imos[0][x1] += 1
            imos[0][x2] -= 1
        imos[y1][x1] += 1
        imos[y1][x2] -= 1
        imos[y2][x1] -= 1
        imos[y2][x2] += 1

    for xi, yi, ci in zip(x, y, c):
        if ci == "B":
            bx = xi + 1
            by = yi + 1
        else:
            bx = xi - K + 1
            by = yi + 1
        sq(bx, by, bx + K, by + K)
        sq(bx + K, by + K, bx, by)

    # print(imos, file=sys.stderr)

    for i in range(2 * K):
        for j in range(1, 2 * K):
            imos[i][j] += imos[i][j - 1]

    for j in range(2 * K):
        for i in range(1, 2 * K):
            imos[i][j] += imos[i - 1][j]

    # print(imos, file=sys.stderr)
    print(max(chain(*imos)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    c = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        c[i] = next(tokens)
    solve(N, K, x, y, c)


if __name__ == '__main__':
    main()
