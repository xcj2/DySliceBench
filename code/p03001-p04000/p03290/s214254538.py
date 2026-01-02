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


def calc(bits, P, C, G):
    total = 0
    cnt = 0
    p = P[:]
    i = 0
    while bits > 0:
        if bits % 2:
            total += p[i] * (i + 1) * 100 + C[i]
            cnt += p[i]
            p[i] = 0
        bits >>= 1
        i += 1
    if total >= G:
        return cnt

    for i in range(len(p)-1, -1, -1):
        if p[i] != 0: break
    need = math.ceil((G - total) / ((i + 1) * 100))
    if need <= p[i]:
        return cnt + need
    return float("inf")



def main():
    D, G = MI()
    P = [None] * D
    C = [None] * D
    for i in range(D):
        P[i], C[i] = MI()

    ans = sum(P)
    for bits in range(2 << (D-1)):
        ans = min(ans, calc(bits, P, C, G))
    return ans



if __name__ == "__main__":
    print(main())
