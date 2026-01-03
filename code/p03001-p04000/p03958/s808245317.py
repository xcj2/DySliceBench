#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    K,T=pin()
    A=tupin()
    B=[[A[i],i] for i in range(T)]
    #print(B)
    prev=None
    for k in range(K):
        B.sort(key=lambda x:x[0])
    #    print(B,"#")
        for i in reversed(range(T)):
            if B[i][0]>0 and B[i][1]!=prev:
                B[i][0]-=1
                
                prev=B[i][1]
                break
    print(sum([B[k][0] for k in range(T)]))
#%%submit!
resolve()