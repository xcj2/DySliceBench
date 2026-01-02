#!/usr/bin/env python3
from functools import reduce
import sys
try:
    from typing import List
except ImportError:
    pass


def gcd(a: int, b: int):
    if a < b:
        return gcd(b, a)
    while b != 0:
        a, b = b, a % b
    return a


def solve(N: int, A: "List[int]"):
    print(reduce(gcd, A))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
