# -*- coding: utf-8 -*-
from sys import stdin
# import numpy as np
# import sys
# sys.setrecursionlimit(10**4)
from collections import Counter

def _li(): return list(map(int, stdin.readline().split()))
def _li_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def _lf(): return list(map(float, stdin.readline().split()))
def _ls(): return stdin.readline().split()
def _i(): return int(stdin.readline())
def _f(): return float(stdin.readline())
def _s(): return stdin.readline()[:-1]


MOD = 10**9 + 7
N = _i()
S = list(_s())

s_count = Counter(S)
ans = 1
for _, i in s_count.items():
    ans *= (i+1)
    ans %= MOD
print((ans - 1) % MOD)
