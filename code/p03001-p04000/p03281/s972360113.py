#!/usr/bin/env python3
import sys
import itertools
import collections
import functools
import math
from queue import Queue
# import numpy as np
INF = float("inf")


def trial_division_sqrt(n):
    prime_count = collections.Counter()

    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[int(n)] += 1

    return prime_count


def num_divisors(prime_count):
    num = 1

    for prime, count in prime_count.items():
        num *= (count + 1)

    return num


def solve(N: int):

    count = 0
    for i in range(1, N+1, 2):
        prime_count = trial_division_sqrt(i)
        if num_divisors(prime_count) == 8:
            count += 1
    print(count)
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
