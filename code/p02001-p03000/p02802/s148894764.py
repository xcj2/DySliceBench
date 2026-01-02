#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    N,M=pin()
    ps=[tupin(str) for _ in range(M)]

    WA=[0]*N
    AC=[0]*N
    for m in range(M):
        p,s=ps[m]
        p=int(p)-1#0-indxd
        if AC[p]==0:
            if s=="WA": 
                WA[p]+=1
            else:
                AC[p]=1
    wa=0
    for Wa in range(N):
        if AC[Wa]==1:wa+=WA[Wa]
    print(sum(AC),wa)
        
#%%submit!
resolve()