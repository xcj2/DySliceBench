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
    N,D=pin()
    X=[lispin()for i in range(N)]
    cnt=0
    for i in range(N-1):
        for j in range(i+1,N):
            temp=0
            #print(i,j)
            for d in range(D):
                temp+=(X[i][d]-X[j][d])**2
            #print(temp)
            for k in range(100000):
                if k**2==temp:cnt+=1
                if k**2>temp:break
    print(cnt)
#%%submit!
resolve()