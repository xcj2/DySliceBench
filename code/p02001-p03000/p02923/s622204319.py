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
h_list = _li()

ans = 0
temp = 0
current = h_list[0]
for h in h_list[1:]:
    if h > current:
        ans = max(ans, temp)
        temp = 0
    else:
        temp += 1
    current = h

ans = max(ans, temp)
print(ans)
