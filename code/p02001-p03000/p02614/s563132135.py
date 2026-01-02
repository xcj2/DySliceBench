#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from copy import deepcopy
def resolve():
    H,W,K=pin()
    maze=[list(input()) for a in range(H)]
#    print(maze)

    #double bit full search
    ans=0
    for i in range(2**H):
        for j in range(2**W):
            #i,j is a set such that not colored red
            notred=[]
            numh=[0]*W
            #Height
            for ci in range(H):
                check=1<<ci
                if i & check:
                    #nukiidasi
                    for k in range(W):
                        if maze[ci][k]=="#":
                            numh[k]+=1

            cal=0
            for cj in range(W):
                check=1<<cj
                if j & check:
                    cal+=numh[cj]
            if cal==K:ans+=1
    print(ans)

#%%submit!
resolve()