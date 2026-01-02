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
    a=sys.stdin.readlines()
    #print(a)
    N,X=int(a[0].rstrip()),a[-1].rstrip()
    #print(N)
    slept=0
    ans=0
    for i in range(1,1+N):
        t,l=a[i].rstrip().split()
        #print(t,l)
        
        if slept:ans+=int(l)
        if t==X:slept=1
    print(ans)
#%%submit!
resolve()