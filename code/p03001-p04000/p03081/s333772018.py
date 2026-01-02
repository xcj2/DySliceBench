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


N, Q = MI()
S = input()
queries = [(lambda t: (t[0], t[1] == "R"))(MIS()) for i in range(Q)]
search_result = [None] * N

def search(i):
    # is S[i] falls to (left, right)
    if i < 0:
        return (True, False)
    if i >= N:
        return (False, True)
    if search_result[i] is not None:
        return search_result[i]
    pos = i
    for t, d in queries:
        if t == S[pos]:
            pos += 1 if d else -1
            if pos < 0:
                return (True, False)
            if pos >= N:
                return (False, True)
    return (False, False)


def search_left():
    def isOK(i):
        return not search(i)[0]
    # lower_bound of search_result[i][0] == False or 0
    left, right = -1, N
    while (right - left > 1):
        mid = left + (right - left) // 2
        if (isOK(mid)):
            right = mid
        else:
            left = mid
    return right

def search_right():
    # lower_bound of search_result[i][1] == True or N
    def isOK(i):
        return search(i)[1]
    # lower_bound of search_result[i][0] == False or 0
    left, right = -1, N
    while (right - left > 1):
        mid = left + (right - left) // 2
        if (isOK(mid)):
            right = mid
        else:
            left = mid
    return right


def main():
    # left
    lb = search_left()
    rb = search_right()

    return rb - lb



if __name__ == "__main__":
    print(main())
