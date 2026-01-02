#!/usr/bin/env python

from sys import stdin
from math import floor

N, M = (int(wd) for wd in stdin.readline().split())
a = [int(wd) for wd in stdin.readline().split()]

def kouyakusuu(g1, g2):
    if g1 < g2:
        return kouyakusuu(g2, g1)
    if g2 == 0:
        return g1
    return kouyakusuu(g2, g1 % g2)

def koubaisuu(g1, g2):
    return (g1 * g2) // kouyakusuu(g1, g2)




def solve2(N, M, a):
    ret = 1
    cnt2 = 1
    while a[0] % (2**cnt2) == 0: cnt2 += 1
    ng = 2 ** cnt2
    cnt2 -= 1
    ok = 2 ** cnt2
    for aa in a:
        if aa % ng == 0:
            return 0
        if aa % ok != 0:
            return 0
        ret = koubaisuu(ret, aa // 2)
    return int(floor((M - ret) / (ret * 2)) + 1)

print(solve2(N, M, a))
