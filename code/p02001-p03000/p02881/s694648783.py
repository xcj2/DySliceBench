#!/usr/bin/env python3
import sys
INF = float("inf")

import math
import collections


def divisors_kai(n):
    ret = 1
    for i in range(1, int(n ** 0.5) + 1):
        d, m = divmod(n, i)
        if m == 0:
            ret = i
            # ret.add(d)
    return ret


def solve(N: int):
    a = divisors_kai(N)
    b = N/a
    print(int(a + b - 2))
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
