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
    N,A,B=pin()
    cnt=0
    for i in range(1,N+1):
        temp=str(i)
        sum=0
        for s in str(i):
            sum+=int(s)
        
        if A<=sum and sum<=B:
            #print(sum)
            cnt+=i
    print(cnt)
#%%submit!
resolve()