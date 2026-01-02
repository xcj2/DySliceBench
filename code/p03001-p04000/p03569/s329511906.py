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


def palindrome(s):
    for i in range(len(s)):
        if not s[i] == s[-i-1]:
            return False
    return True


def main():
    s = input().strip()
    i = 0
    sdx = ""
    x = defaultdict(int)
    for c in s:
        if c == "x":
            x[i] += 1
        else:
            sdx += c
            i += 1
    if not palindrome(sdx):
        return -1

    cnt = 0
    k = list(x.keys())
    for d in k:
        cnt += max(0, x[d] - x[i-d])
    return cnt


if __name__ == "__main__":
    print(main())
