#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code

#なお、任意の整数 M に対して M の −2 進数表現が一意に定まることが証明できます。
#2桁ごとに見るとよかった（もう実験したよ）
def resolve():
    N,=pin()
    K,=pin()
    X=tupin()
    ans=0
    for x in X:
        ans+=min(abs(x),abs(K-x))*2
    print(ans) 
#%%submit!
resolve()