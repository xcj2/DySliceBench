#!/usr/bin/env python3
import sys


YES = "YES"  # type: str
NO = "NO"  # type: str


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def solve(A: int, B: int, C: int):
    print(YES if C % gcd(A, B) == 0 else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)


if __name__ == '__main__':
    main()
