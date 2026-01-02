# coding: utf-8

import sys
import math

import array
import bisect
import collections
from collections import Counter, defaultdict
import fractions
import heapq
import re

sys.setrecursionlimit(1000000)


def array2d(dim1, dim2, init=None):
    return [[init for _ in range(dim2)] for _ in range(dim1)]

def argsort(l, reverse=False):
    return sorted(range(len(l)), key=lambda i: l[i], reverse=reverse)

def argmin(l):
    return l.index(min(l))

def YESNO(ans, yes="YES", no="NO"):
    print([no, yes][ans])

II = lambda: int(input())
MI = lambda: map(int, input().split())
MIL = lambda: list(MI())
MIS = lambda: input().split()


def main():
    N, M = MI()
    A = Counter(MI())
    for i in range(M):
        b, c = MI()
        A[c] += b
    ans = 0
    nc = N
    for c in sorted(A.keys(), reverse=True):
        if A[c] >= nc:
            return ans + c * nc
        ans += c * A[c]
        nc -= A[c]
    return ans


if __name__ == "__main__":
    print(main())
