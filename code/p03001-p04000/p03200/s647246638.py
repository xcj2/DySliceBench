# coding: utf-8

import math
import fractions
import heapq
import collections
import re
import array
import bisect

from collections import Counter, defaultdict


def array2d(dim1, dim2, init=None):
    return [[init for _ in range(dim2)] for _ in range(dim1)]

II = lambda: int(input())
MI = lambda: map(int, input().split())




def mc(s):
    l = len(s)
    if l <= 1: return 0
    s1 = s[:l//2]
    s2 = s[l//2:]
    count = mc(s1) + mc(s2)
    count += sum(s1) * (len(s2) - sum(s2))
    return count


def main():
    s = list(input().strip())
    s = [(c == "B") for c in s]
    return mc(s)


if __name__ == "__main__":
    print(main())
