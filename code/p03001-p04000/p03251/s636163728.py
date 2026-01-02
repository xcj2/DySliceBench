#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, X: int, Y: int, x: "List[int]", y: "List[int]"):
    xs = set(x)
    xs.add(X)
    ys = set(y)
    ys.add(Y)
    x1 = min(xs)
    x2 = max(xs)
    y1 = min(ys)
    y2 = max(ys)
    print("No War" if (x2 < y1 or y2 < x1) else "War")


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    y = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, X, Y, x, y)


if __name__ == '__main__':
    main()
