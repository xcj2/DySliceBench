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

s_list = []
for _ in range(N):
    s = list(_s())
    s.sort()
    s_list.append(''.join(s))

s_list.sort()
s_list.append('')

ans = 0
pre = ''
cur = 0
for s in s_list:
    if s == pre:
        cur += 1
    else:
        ans += (cur + 1) * cur // 2
        cur = 0
        pre = s

print(ans)
