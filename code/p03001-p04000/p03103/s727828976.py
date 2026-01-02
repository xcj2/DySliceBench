#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N,M=pin()
    A=sorted([lispin() for _ in range(N)])
    #print(A)
    ans=0
    for a in A:
        if a[1]>M:
            ans+=a[0]*M
            break
        else:
            ans+=a[0]*a[1]
            M-=a[1]
        #print(M)
    print(ans)
#%%submit!
resolve()
