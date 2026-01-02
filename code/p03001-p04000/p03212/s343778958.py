#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code

def resolve():
    N=input()
    n=len(N)
    N=int(N)
    ans=set()
    numans=0
    stack=[(3,1),(5,2),(7,4)]
    row=(3,5,7)
    while (stack!=[]):
        t,u=stack.pop()
        for n,l in enumerate(row):
            neu=(t*10+l,u|(2**n))
            if neu[0]<=N:
                stack.append(neu)
                if neu[1]==7:
                    ans.add(neu[0])
    print(len(ans))
#%%submit!
resolve()