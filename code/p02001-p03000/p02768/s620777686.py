# coding: utf-8

import sys
import math
import collections
import itertools
from inspect import currentframe
INF = 10 ** 10
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return y if x % y == 0 else gcd(y, x % y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def MI() : return map(int, input().split())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def chkprint(*args) : names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}; print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

def ncr(n, r):
    a = 1
    b = 1
    for i in range(r):
        a = (a * (n - i) % MOD)
        b = (b * (r - i) % MOD)

        # a *= ((n - i) % MOD)
        # b *= ((r - i) % MOD)

    return a * pow(b, MOD - 2, MOD) % MOD

N, A, B = MI()

s = pow(2, N, MOD) - 1
ab = (ncr(N, A) + ncr(N, B)) % MOD

print((s - ab)  % MOD)
