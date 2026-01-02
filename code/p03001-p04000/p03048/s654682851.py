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
    R,G,B,N=pin()
    cnt=0
    for r in range(N+1):
        for g in range(N+1):
            t=(R*r+G*g)
            if N<t:continue
            if (N-t)%B==0:
                #print(r,g,t)
                cnt+=1
    print(cnt)
#%%submit!    
resolve()
