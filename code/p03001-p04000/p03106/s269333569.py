#!/usr/bin/env python3
import sys


def gcd(a: int, b: int):
    if a < b:
        return gcd(b, a)
    while b != 0:
        a, b = b, a % b
    return a


def solve(A: int, B: int, K: int):
    g = gcd(A, B)
    c = [i for i in range(1, g + 1) if g % i == 0]
    print(c[-K])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(A, B, K)


if __name__ == '__main__':
    main()
