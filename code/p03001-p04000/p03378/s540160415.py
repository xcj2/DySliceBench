#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code

def resolve():
    N,M,X=pin()
    A=lispin()
    ans=0
    x=X
    for i in range(N):
        
        if x==N:break
        if x in A:ans+=1
        x+=1
    bns=0
    x=X
    for i in range(N):
        
        if x==0:break
        if x in A:bns+=1
        x-=1
    print(min(bns,ans))    
            

#%%submit!    
resolve()