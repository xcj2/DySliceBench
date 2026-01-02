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


MOD = 10**9+7
N, M = _li()

a_list = []
for _ in range(M):
    a_list.append(_i())
a_list.append(-1)

ans = [1, 1]
a_index = 0
if a_list[a_index] == 1:
    ans[1] = 0
    a_index += 1

for i in range(2, N+1):
    if i == a_list[a_index]:
        ans = [ans[1], 0]
        a_index += 1
    else:
        ans = [ans[1], ans[0] + ans[1] % MOD]
    if ans[0] + ans[1] == 0:
        break
print(ans[1] % MOD)

