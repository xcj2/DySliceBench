# coding: utf-8

import math
import fractions
import heapq
import collections
import re
import array
import bisect

from collections import Counter, defaultdict


class BIT(object):
    """Bibary Indexed Tree / Fenwick Tree"""
    # 1-indexed
    def __init__(self, size):
        self.size = size
        self.l = [0] * (size + 1)

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.l[i]
            i -= i & -i
        return r

    def add(self, i, x):
        while i <= self.size:
            self.l[i] += x
            i += i & -i


max_a = 1000000


def solve(a):
    bit = BIT(max_a)
    ans = 0
    for i, x in enumerate(a):
        ans += i - bit.sum(x)
        bit.add(x, 1)
    return ans


def main():
    while True:
        N = int(input())
        if N == 0:
            return
        a = []
        for i in range(N):
            a.append(int(input()))
        print(solve(a))


if __name__ == "__main__":
    main()