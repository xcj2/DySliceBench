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
    lr = [0] * (N + 1)
    rr = [0] * (N + 1)
    for i in range(M):
        l, r = MI()
        lr[l] += 1
        rr[r] += 1
    c = 0
    ans = 0
    for i in range(N + 1):
        c += lr[i]
        if c == M: ans += 1
        c -= rr[i]
    return ans


if __name__ == "__main__":
    print(main())
