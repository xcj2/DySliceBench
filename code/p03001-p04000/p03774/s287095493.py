#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import math
import collections
import itertools
import functools

DEBUG = True
DEBUG = False

def dbg(*args):
    if DEBUG:
        print("DBG: ", file=sys.stderr, end="")
        print(*args, file=sys.stderr)

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append((a,b))
    B = []
    for _ in range(M):
        c, d = map(int, input().split())
        B.append((c,d))

    for i, a in enumerate(A):
        argmin = 0
        dmin = dist(a, B[0])
        for j, b in enumerate(B):
            d = dist(a, b)
            if d < dmin:
                argmin = j
                dmin   = d
        print(argmin+1)

if __name__ == "__main__": main()
