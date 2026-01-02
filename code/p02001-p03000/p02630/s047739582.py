#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from collections import Counter
def resolve():
    N,=pin()
    An=lispin()
    count_An=dict(Counter(An))
    S=sum(An)
    Q,=pin()
    erachan=0
    for i in range(Q):
        a,b=pin()
        temp=0
        try:
            temp=count_An[a]
            count_An[a]=0
            count_An.setdefault(b,0)
            count_An[b]+=temp
        except KeyError:erachan+=1
        S=S+(b-a)*temp
        print(S)
        
#%%submit!
resolve()