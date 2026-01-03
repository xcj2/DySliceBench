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
    N,=pin()
    temp=0
    notsolve=0
    a=0
    for i in range(1,10**7):
        temp+=i
        if temp>N:
            notsolve=temp-N
            a=i
            break
    for j in range(1,a+1):
        if j!=notsolve:print(j)
    
        
#%%submit!    
resolve()


