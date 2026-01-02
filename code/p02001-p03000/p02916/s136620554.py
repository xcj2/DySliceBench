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
a_list = _li()
b_list = _li()
c_list = _li()

ans = sum(b_list)
for i in range(N-1):
    if a_list[i] + 1 == a_list[i+1]:
        ans += c_list[a_list[i] - 1]
print(ans)
