# -*- coding: utf-8 -*-

import sys
from collections import Counter

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

H,W=MAP()
S=''
for i in range(H):
    S+=input()

C=Counter(S)
if H%2==0 and W%2==0:
    for k, v in C.items():
        if v%4!=0:
            No()
            exit()
    Yes()
elif H%2==0:
    mod2=0
    for k, v in C.items():
        if v%4!=0:
            if v%2==0:
                mod2+=1
            else:
                No()
                exit()
    if mod2<=H//2:
        Yes()
    else:
        No()
elif W%2==0:
    mod2=0
    for k, v in C.items():
        if v%4!=0:
            if v%2==0:
                mod2+=1
            else:
                No()
                exit()
    if mod2<=W//2:
        Yes()
    else:
        No()
else:
    mod2=mod1=0
    for k, v in C.items():
        if v%4!=0:
            if v%2==0:
                mod2+=1
            elif v%3==0:
                mod2+=1
                mod1+=1
            else:
                mod1+=1
    if mod1==1 and mod2<=(H+W)//2-1:
        Yes()
    else:
        No()
