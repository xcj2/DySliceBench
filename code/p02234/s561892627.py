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

Mat = collections.namedtuple("Mat", "r c")

def mat_mul(ms):
    return Mat(ms[0].r, ms[-1].c)

def cost(m1, m2):
    return m1.r * m1.c * m2.c

def solve(n, ms):
    if n == 1: return 0

    dp = {}
    for i in range(n):
        dp[(i,i)] = 0

    for l in range(2, n+1):
        for i in range(n-l+1):
            #cost_min = math.inf
            cost_min = float("inf")
            for j in range(l-1):
                dbg("l, i, j: %d %d %d", l, i, j)
                m_lhs = mat_mul(ms[i:i+j+1])
                m_rhs = mat_mul(ms[i+j+1:i+l])
                dbg("m_lhs, m_rhs: %r %r", m_lhs, m_rhs)
                cost_lhs = dp[(i,i+j)]
                cost_rhs = dp[(i+j+1,i+l-1)]
                dbg("cost_lhs, cost_rhs: %d %d", cost_lhs, cost_rhs)
                cost_mul = cost(m_lhs, m_rhs)
                dbg("cost_mul: %d", cost_mul)
                cost_now = cost_mul + cost_lhs + cost_rhs
                dbg("cost_now: %d", cost_now)
                if cost_min > cost_now:
                    cost_min = cost_now
            dp[(i,i+l-1)] = cost_min

    dbg(dp)
    return dp[(0,n-1)]

def main():
    n = int(input())

    ms = []
    for _ in range(n):
        r,c = map(int, input().split())
        ms.append(Mat(r,c))

    print(solve(n, ms))

if __name__ == "__main__": main()