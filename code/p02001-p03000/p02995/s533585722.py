#!/usr/bin/env python3
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


def solve(A: int, B: int, C: int, D: int):
    cdl = C // gcd(C, D) * D
    A -= 1
    print(
        (B - A)
        - (B // C - A // C) - (B // D - A // D)
        + (B // cdl - A // cdl)
    )


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)


if __name__ == '__main__':
    main()
