#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from collections import Counter
def resolve():
    N,=pin()
    H=lispin()
    for i in range(1,N):
        if H[i]-H[i-1]>0:
            H[i]-=1
    cond=1
    for j in range(1,N):
        if H[j]-H[j-1]<0:cond=0;break
    print(["No","Yes"][cond])
    #print(B)
#%%submit!
resolve()