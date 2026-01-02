#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def main():
    def digsum(s):
        su = 0
        for c in s:
            su += int(c)
        return su

    def break_ith_dig(s, i1):
        assert 2 <= i1 <= dig
        if s[-i1] == "0":
            return s
        s = s[:-i1] + str(int(s[-i1]) - 1) + "9" * (i1 - 1)
        return s

    ns = input()
    dig = len(ns)
    ma = digsum(ns)
    for i in range(2, dig + 1):
        ns = break_ith_dig(ns, i)
        ma = max(ma, digsum(ns))

    print(ma)

main()

