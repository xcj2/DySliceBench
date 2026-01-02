#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N,=pin()
    A=lispin()
    temp=0
    sumA=[0]*N
    sumA[0]=A[0]
    for j in range(1,N):
        sumA[j]=sumA[j-1]+A[j]
    #print(sumA)
    ans=2**32-1
    t=sumA[-1]
    for i in range(N):
        ans=min(ans,abs(t-sumA[i]*2))
        
    print(ans)
#%%submit!
resolve()
