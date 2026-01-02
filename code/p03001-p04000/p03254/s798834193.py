#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
import itertools
def resolve():
    N,X=pin()
    A=lispin()
    A.sort()
    S=list(itertools.accumulate(A))
    #print(S)
    for i in range(N):
        if S[i]>X:
            print(i)
            return
    if S[-1]<X:print(N-1)
    else:print(N)
        
        

#%%submit!    
resolve()