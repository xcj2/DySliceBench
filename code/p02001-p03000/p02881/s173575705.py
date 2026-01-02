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
    ans=N+1
    for i in range(1,10**6+1):
        if N%i==0:
            j=N//i
            #print(i,j)
            if j>0:
                ans=min(ans,i+j)
    print(ans-2)
    #print(B)
#%%submit!
resolve()