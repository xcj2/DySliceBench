# -*- coding: utf-8 -*-
from sys import stdin
import numpy as np
# import sys
# sys.setrecursionlimit(10**4)

def _li(): return list(map(int, stdin.readline().split()))
def _li_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def _lf(): return list(map(float, stdin.readline().split()))
def _ls(): return stdin.readline().split()
def _i(): return int(stdin.readline())
def _f(): return float(stdin.readline())
def _s(): return stdin.readline()[:-1]


N = _i()
W_list = _li()

cum_W = np.cumsum(W_list)
ans = float('inf')
for i in range(N-1):
    ans = min(ans, abs(cum_W[i]*2 - cum_W[-1]))
print(ans)
