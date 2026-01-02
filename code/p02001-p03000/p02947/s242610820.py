#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from operator import mul
from functools import reduce

input = sys.stdin.readline

def cmb(n,r):
    r = min(n-r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

def comb(a, b):
    n = a
    for _ in range(b):
        n -= 1
        a *= n

    for i in range(1, b):
        b *= i
    return int(a / b)


def main():
    n = int(input())
    m = {}
    for l in sys.stdin:
        s = ''.join(sorted(l.strip()))
        if s in m:
            m[s] += 1
        else:
            m[s] = 1
    cnt = 0
    for k, v in m.items():
        if v == 1:
            continue
        if v == 2:
            cnt += 1
        else:
            cnt += cmb(v, 2)
    print(cnt)

main()
