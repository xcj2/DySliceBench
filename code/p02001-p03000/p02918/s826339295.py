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


N, K = _li()
S = _s()

lr = 0
rl = 0
for i in range(N-1):
    if S[i] == 'L' and S[i+1] == 'R':
        lr += 1
    elif S[i] == 'R' and S[i+1] == 'L':
        rl += 1

ans = N - (lr + rl + 1)
cand = min(lr, rl)
ans += 2 * min(cand, K)
if K > cand:
    if lr > rl and (S[0] == 'L' or S[-1] == 'R'):
        ans += 1
    elif lr < rl and (S[0] == 'R' or S[-1] == 'L'):
        ans += 1
print(ans)
