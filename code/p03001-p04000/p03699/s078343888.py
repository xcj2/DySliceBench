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

def disp(x):
    return 0 if x%10==0 else x

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    A.sort()

    asum = sum(A)
    vmax = disp(asum)
    for a in A:
        v = disp(asum - a)
        vmax = max(vmax, v)

    print(vmax)

if __name__ == "__main__": main()
