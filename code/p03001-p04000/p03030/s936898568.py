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
    N=int(input())
    A=[]
    for i in range(N):
        S,P=pin(str)
        P=int(P)
        A.append((S,P,i+1))
    A.sort(key=lambda x:x[1],reverse=True)
    A.sort(key=lambda x:x[0])
    for a in A:
        print(a[2])

#%%submit!
resolve()