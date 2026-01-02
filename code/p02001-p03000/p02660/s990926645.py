#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug

import math
from collections import defaultdict
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect


# 50 まで
def survey():
    v = 1
    k = 2
    i = 0
    while not (v > 10 ** 12):
        v = k ** i
        print(i)
        i += 1

def survey2():
    v = 1
    s = 0
    while not (s > 50):
        #print('s', s) # debug
        s += v
        v += 1

def diff_selectable(v):
    l = [1, 3, 6, 10, 15, 21, 28, 36, 45, ]
    for i, t in enumerate(l):
        if v < t:
            return i
    raise ValueError

"""
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
"""

def prime_factorize(n):
    a = defaultdict(lambda: 0)
    while n % 2 == 0:
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n] += 1
    return a

if __name__ == '__main__':
    ans = 0
    data = int(input())
    primes = prime_factorize(data)
    for pc in primes.values():
        ans  += diff_selectable(pc)
    #print('ans') # debug
    print(ans)

    #print('\33[32m' + 'end' + '\033[0m') # debug
