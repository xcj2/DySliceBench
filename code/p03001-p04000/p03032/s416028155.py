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


def get(V, n):
    if n >= len(V):
        yield V
    else:
        yield V[:n]
        for i in range(1, n):
            yield V[:n-i] + V[-i:]
        yield V[-n:]


def main():
    N, K = MI()
    V = MIL()
    ans = 0

    for i in range(max(K//2, 1), K + 1):
        # 左右からi個まで取る
        for vs in get(V, i):
            # K-i個まで、負を捨てる
            vs = sorted(vs)
            for j, v in enumerate(vs):
                if v >= 0: break
            ans = max(ans, sum(vs[min(K-i, j):]))
    return ans


if __name__ == "__main__":
    print(main())
