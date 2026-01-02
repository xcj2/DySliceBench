#!/usr/bin/env python3

import itertools
import sys


class CumulativeSum(object):

    def __init__(self, sequence):
        self.cumulative_sum = [0]
        self.cumulative_sum.extend(itertools.accumulate(sequence))

    def partial_sum(self, first, last):
        return self.cumulative_sum[last + 1] - self.cumulative_sum[first]


def div_ceil(a, b):
    return (a + b - 1) // b


def solve(n, xs):
    cs = CumulativeSum(xs)
    res = sys.maxsize // 10
    for p in range(n):
        left_sum = cs.partial_sum(0, p - 1)
        right_sum = cs.partial_sum(p, n - 1)
        res = min(res, abs(right_sum - left_sum))
    return res


def main():
    n = int(input())
    xs = [int(x) for x in input().split()]
    res = solve(n, xs)
    print(res)


if __name__ == "__main__":
    main()
