#!/usr/bin/env python3
import sys
import math
from collections import Counter
INF = float("inf")

MOD = 1000000007  # type: int


def factorial(n):
    # 試し割りによる素因数分解
    prime_count = Counter()

    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[int(n)] += 1

    return prime_count


def solve(N: int):

    primes = Counter()
    for i in range(1, N+1):
        primes += factorial(i)

    tot = 1
    for key in primes:
        tot *= primes[key]+1
        tot %= MOD

    print(tot)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
