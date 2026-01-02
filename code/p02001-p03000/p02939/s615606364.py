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
    S=input()
    ans=0
    prev=""    
    temp=""
    cnt=0
    for i in range(len(S)):
        temp+=S[i]
        if temp!=prev:
            cnt+=1
            prev=temp
            temp=""
    print(cnt)

#%%submit!
resolve()