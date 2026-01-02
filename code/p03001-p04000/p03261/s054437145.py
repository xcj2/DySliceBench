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
    s=set()
    prev=""
    for i in range(N):
        temp=input()
        if temp in s:
            print("No")
            return
        if i>0 and temp[0]!=prev[-1]:
            print("No")
            return
        s.add(temp)
        prev=temp
    print("Yes")
#%%submit!
resolve()