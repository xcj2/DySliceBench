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


def solve(N: int, P: int):
    counter = factorial(P)
    ans = 1
    for k in counter:
        if counter[k] >= N:
            ans *= k**(counter[k]//N)
    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve(N, P)


if __name__ == '__main__':
    main()
