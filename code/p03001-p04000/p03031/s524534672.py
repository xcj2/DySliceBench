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

def check(N, S, P, state):
    sw = [0] * len(P)
    for i in range(N):
        if (state >> i) & 1:
            for m, s in enumerate(S):
                sw[m] += i + 1 in s
    return all((sw[i] % 2 == P[i] for i in range(len(P))))


def main():
    N, M = MI()
    S = []
    for _ in range(M):
        S.append(MIT()[1:])
    P = MIT()
    ans = 0
    for state in range(2**N):
        ans += check(N, S, P, state)
    return ans


if __name__ == "__main__":
    print(main())
