# -*- coding: utf-8 -*-
from sys import stdin
# import numpy as np
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
b_list = _li()

ans = b_list[0] + b_list[-1]
for i in range(N-2):
    ans += min(b_list[i], b_list[i+1])
print(ans)

