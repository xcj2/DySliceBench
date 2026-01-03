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


def possible(N, M, k):
    if N >= k:
        return M >= 2*k
    else:
        M -= 2*(k-N)
        return M >= 2*k

def main():
    N, M = map(int, input().split())

    # cc -> S はできるが S -> cc はできない

    # [lo, hi)
    # lo では必ず可能、hiでは必ず不可能
    hi = M // 2 + 1
    lo = M // 4
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if possible(N, M, mid):
            lo = mid
        else:
            hi = mid

    print(lo)

if __name__ == "__main__": main()
