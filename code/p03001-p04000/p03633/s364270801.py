#!/usr/bin/env python3
from functools import reduce
import sys
try:
    from typing import List
except ImportError:
    pass


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int):
    g = gcd(a, b)
    return a // g * b


def solve(N: int, T: "List[int]"):
    print(reduce(lcm, T))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T)


if __name__ == '__main__':
    main()
