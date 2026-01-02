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
    X=int(input())
    if X<4 :print(1);return
    ans=0
    for i in range(2,X):
        temp=i**2
        if temp<=X:
            while(1):
                if temp*i>X:
                    ans=max(ans,temp)
                    #print(ans,i)
                    break
                temp*=i
    print(ans)

#%%submit!
resolve()