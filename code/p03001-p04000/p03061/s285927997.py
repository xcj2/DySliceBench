#!/usr/bin/env python3

import itertools
try:
    from math import gcd
except ImportError:
    from fractions import gcd


class Cumulative(object):

    def __init__(self, seq, op):
        self.cumul_array = [0]
        self.cumul_array.extend(itertools.accumulate(seq, op))


def solve(n, xs):
    left_cumul = Cumulative(xs, gcd)
    right_cumul = Cumulative(reversed(xs), gcd)
    res = 1
    for i in range(n):
        left_gcd = left_cumul.cumul_array[i]
        right_gcd = right_cumul.cumul_array[n - i - 1]
        cand = gcd(left_gcd, right_gcd)
        if cand > res:
            res = cand
    return res


def main():
    n = int(input())
    xs = [int(x) for x in input().split()]
    res = solve(n, xs)
    print(res)


if __name__ == "__main__":
    main()
