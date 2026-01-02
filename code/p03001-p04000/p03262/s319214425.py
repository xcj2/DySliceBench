#!/usr/bin/env python3
from functools import reduce
import sys
try:
    from typing import List
except ImportError:
    pass


def gcd(a: int, b: int):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def solve(N: int, X: int, x: "List[int]"):
    x2 = [abs(xi - X) for xi in x]
    print(reduce(gcd, x2))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, x)


if __name__ == '__main__':
    main()
