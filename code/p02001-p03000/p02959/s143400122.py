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
    A=lispin()
    B=lispin()
    cnt=0
    for i in range(N):
        if A[i]>B[i]:
            cnt+=B[i]
        else:
            t=B[i]-A[i]
            x=A[i+1]-t
            if x<0:
                cnt+=A[i]+A[i+1]
                A[i+1]=0
            else:
                A[i+1]=x
                cnt+=B[i]
    print(cnt)
        
    
#%%submit!
resolve()