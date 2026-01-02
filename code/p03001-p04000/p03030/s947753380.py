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
MIT = lambda: tuple(MI())
MIS = lambda: input().split()


def main():
    N = II()
    sp = [None] * N
    for i in range(N):
        s, p = MIS()
        sp[i] = (s, -int(p))
    for k in sorted(range(N), key = lambda i: sp[i]):
        print(k + 1)


if __name__ == "__main__":
    main()
