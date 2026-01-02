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


def solve(X: int):

    for i in range(X, 2*(10**5)):
        c = factorial(i)
        if len(c) == 1 and list(c.values())[0] == 1:
            print(i)
            break
    else:
        raise Error

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)


if __name__ == '__main__':
    main()
