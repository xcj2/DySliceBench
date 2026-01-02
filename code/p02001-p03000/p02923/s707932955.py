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
    A=lispin()
    temp=0
    cnt=0
    for i in range(1,N):
        if A[i]<=A[i-1]:
            #print(i)
            cnt+=1
        else:
            temp=max(temp,cnt)
            cnt=0
    print(max(temp,cnt))
    #print(A,B,C)


#%%submit!
resolve()
