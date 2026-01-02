#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def max_cal(xn, vn, twoway):
    n = len(xn)
    factor = 2 if twoway else 1
    mc = []
    res = vn[0] - factor * xn[0]
    mc.append(max(0, res))
    for i in range(1, n):
        res += vn[i] - factor * (xn[i] - xn[i - 1])
        mc.append(max(mc[-1], res))
    assert len(mc) == len(xn)
    return mc

def read_input():
    n, c = map(int, input().split())
    xn = []
    vn = []
    for i in range(n):
        x, v = map(int, input().split())
        xn.append(x)
        vn.append(v)
    xnr = list(reversed([c - x for x in xn]))
    vnr = list(reversed(vn))
    return n, c, xn, vn, xnr, vnr

def merge(xn, xnr, c, max_one, max_two):
    def array_j(mt, j):
        if j < 0:
            return 0
        return mt[j]

    n = len(xn)
    j = -1
    ma = 0
    for i in reversed(range(n)):
        x = xn[i]
        while j + 1 < n and xnr[j + 1] * 2 <= c - x:
            j += 1
        res = max_one[i] + array_j(max_two, j)
        ma = max(ma, res)
    return ma

def main():
    n, c, xn, vn, xnr, vnr = read_input()
    max_one_cw = max_cal(xn, vn, False)
    max_two_cw = max_cal(xn, vn, True)
    max_one_ccw = max_cal(xnr, vnr, False)
    max_two_ccw = max_cal(xnr, vnr, True)
    res = merge(xn, xnr, c, max_one_cw, max_two_ccw)
    res = max(res, merge(xnr, xn, c, max_one_ccw, max_two_cw))
    print(res)

main()
