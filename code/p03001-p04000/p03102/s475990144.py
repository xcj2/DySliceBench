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


def check(B, C):
    def _check(A):
        return sum([A[i] * B[i] for i in range(len(B))]) + C > 0
    return _check


def main():
    N, M, C = MI()
    B = MIL()
    A = []
    for i in range(N):
        A.append(MIL())
    return sum(map(check(B, C), A))


if __name__ == "__main__":
    print(main())
