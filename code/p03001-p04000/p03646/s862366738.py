#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    K,=pin()
    if K==0:
        print(4)
        print(3,3,3,3)
    elif K==1:
        print(3)
        print(1,0,3)
    elif K<=50:
        print(K)
        t=[K]*K
        print(*t)
    else:
        print(50)
        s=K%50
        t=K//50
        t=[50+t-1]*50
        if s>0:
            for i in range(s):
                t=[tt-1 for tt in t]
                t[i]+=51
        print(*t)
#%%submit!
resolve()