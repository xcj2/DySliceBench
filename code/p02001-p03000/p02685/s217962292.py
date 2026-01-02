#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect
import functools

MOD = 998244353


def factorial(n, mod=None, memo=False):
    if memo:
        factorial.memo = [1] * (n + 1)
        #print('factorial.memo') # debug
        #print(factorial.memo) # debug
        for i in range(1, n + 1):
            #print('i') # debug
            #print(i) # debug
            if mod is None:
                factorial.memo[i] = i * factorial.memo[i - 1]
            else:
                factorial.memo[i] = i * factorial.memo[i - 1] % mod
            #print('factorial.memo[i]') # debug
            #print(factorial.memo[i]) # debug
    return factorial.memo[n]

def choose(n, r, mod=None):
    a = factorial(n)
    b = factorial(r)
    c = factorial(n - r)
    if mod is None:
        res = a // b // c
    else:
        # fermat's little theorem
        res = a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod) % mod
    return res

def calc(n, m, k):
    res = choose(n - 1, k, MOD) * m * pow(m - 1, n - 1 - k, MOD) % MOD
    #print('res') # debug
    #print(res) # debug
    return res

# in the case k pair is same, pattern is (n-1)Choose(k) * m (m - 1) ** (n - 1 - k)
if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))
    ans = 0
    factorial(n, MOD, True)
    for kk in range(k + 1):
        ans += calc(n, m, kk)
    #print('ans') # debug
    print(ans % MOD)

    #print('\33[32m' + 'end' + '\033[0m') # debug

