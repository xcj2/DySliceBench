#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def gcd(x, y):
    if x < y:
        x, y = y, x  # x >= y
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

def gcd_all(a):
    g = a[0]
    for y in a:
        g = gcd(g, y)
    return g

def main():
    n, k = map(int, input().split())
    ai = list(map(int, input().split()))
    assert len(ai) == n
    g = gcd_all(ai)
    m = max(ai)
    if m - k >= 0 and (m - k) % g == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

main()
