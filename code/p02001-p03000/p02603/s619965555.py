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
    A=[*pin()]

    mon=1000
    stocks=0
    final=0
    for i in range(N-1):

        if A[i]>A[i+1]:# sell
            if stocks>0:
                #print("yaa")
                mon+=stocks*A[i]
                stocks=0
            final=0
            
        elif A[i]<A[i+1]: #buy

            stocks+=mon//A[i]
            mon=mon%A[i]
            final=1
        #print(mon,stocks)
    print(mon+stocks*A[-1])
            
#%%submit!
resolve()
