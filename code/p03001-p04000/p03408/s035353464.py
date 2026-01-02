#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from collections import defaultdict
def resolve():
    N,=pin()
    a=defaultdict(lambda :0)
    for i in range(N):
        t=input()
        a[t]+=1
    M,=pin()
    for j in range(M):
        s=input()
        a[s]-=1
    t=(max(a.values()))          
    print(max(0,t))  
#%%submit!
resolve()