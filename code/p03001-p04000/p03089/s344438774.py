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

ans = []
for i in range(N, 0, -1):
    cand = []
    for j in range(i):
        if b_list[j] == (j+1):
            cand.append(j)
    if len(cand) == 0:
        print(-1)
        exit()
    else:
        a = b_list.pop(cand[-1])
        ans.append(a)

for a in ans[::-1]:
    print(a)
