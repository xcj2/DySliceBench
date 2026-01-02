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
    N,=pin()
    A1=lispin()
    A2=lispin()
    B1=list(accumulate(A1))
    B2=list(accumulate(A2))
    ans=B1[0]+B2[-1]
    for i in range(1,N):
        ans=max(ans,B1[i]+B2[-1]-B2[i-1])

    print(ans)
        
    
#%%submit!
resolve()