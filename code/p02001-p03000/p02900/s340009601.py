#!/usr/bin/env python3
import sys
INF = float("inf")
import math
import collections


def factorial(n):
    # 試し割りによる素因数分解
    prime_count = collections.Counter()

    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[int(n)] += 1

    return prime_count


def solve(A: int, B: int):
    As = factorial(A)
    Bs = factorial(B)
    counter = 1
    for key in As:
        if key in Bs:
            counter += 1
    print(counter)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == '__main__':
    main()
