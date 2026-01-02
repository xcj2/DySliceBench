#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N,=pin()
    if N%2==0: 
        print(-1)
        return #10の倍数も含まれる
    cnt=7%N
    if cnt==0:
        print(1)
        return
    for i in range(2,10**7):
        cnt=cnt*10+7
        cnt%=N
        if cnt==0:
            print(i)
            return
    print(-1)
#%%submit!
resolve()