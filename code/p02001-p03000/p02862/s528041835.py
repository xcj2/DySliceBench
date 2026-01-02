#!/usr/bin/python

import sys
from pprint import pprint

import math

def nCr(n, r):
    v = 10**9 + 7
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def cmb_mod(n, r, mod):
    r = min(n - r, r)
    if r == 0:
        return 1
    else:
        denominator = 1
        for i in range(n, n - r, -1):
            denominator = (denominator * i) % mod
        numerator = 1
        for i in range(1, r + 1):
            numerator = (numerator * i) % mod
        return denominator * pow(numerator, mod - 2, mod) % mod 

x, y = map(int, sys.stdin.readline().strip().split(" "))

if (x + y) % 3 != 0:
    print(0)
    sys.exit()

n = (2*y - x) // 3
m = (2*x - y) // 3

if n < 0 or m < 0:
    print(0)
    sys.exit()

# print(n, m)
# print(nCr(n+m, n) % (10**9+7))
print(cmb_mod(n + m, n, 10**9 + 7))