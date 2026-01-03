#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def fact(i):
    res = 1
    for j in range(1, i + 1):
        res *= j
    return res

def combi(n, i):
    assert 0 <= i <= n
    return fact(n) // (fact(i) * fact(n - i))

def main():
    n, p = map(int, input().split())
    ai = list(map(int, input().split()))
    assert len(ai) == n

    evens = 0
    odds = 0
    for a in ai:
        if a % 2 == 0:
            evens += 1
        else:
            odds += 1
    way_evens = 2 ** evens
    way_odds = 0
    for no in range(p, odds + 1, 2):
        way_odds += combi(odds, no)

    print(way_evens * way_odds)

main()
