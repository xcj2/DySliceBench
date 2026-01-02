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
    A=[int(input()) for i in range(5)]
    A.sort(key=lambda x:(x-1)%10)
    #print(A)
    ans=A[0]
    for n in range(1,5):
        a=A[n]
        if a%10==0:
            ans+=a
        else:ans+=(1+a//10)*10
    print(ans)
        
#%%submit!    
resolve()