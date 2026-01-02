#!/usr/bin/env python3
from itertools import combinations
import sys


def solve(a: int, b: int, c: int, d: int, e: int, k: int):
    print(":(" if any(
        abs(x1 - x2) > k
        for x1, x2 in combinations([a, b, c, d, e], 2)
    ) else "Yay!")


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    e = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(a, b, c, d, e, k)


if __name__ == '__main__':
    main()
