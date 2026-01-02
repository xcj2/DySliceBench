#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from itertools import accumulate
def resolve():
    D,N=pin()
    if D==0:
        if N!=100:print(N)
        else:print(101)
    if D==1:
        if N!=100:print(N*100)
        else:print(10100)
    if D==2:
        if N!=100:print(N*10000)
        else:print(1010000)
#%%submit!
resolve()