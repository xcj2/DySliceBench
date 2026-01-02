#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from collections import Counter
def resolve():
    S=input()
    N=len(S)
    s1="01"*(N//2)+"0"*(N%2)
    s2="10"*(N//2)+"1"*(N%2)
    #print(s1,s2)
    ans1,ans2=0,0
    for s in range(N):
        if S[s]!=s1[s]:ans1+=1
        if S[s]!=s2[s]:ans2+=1
    print(min(ans1,ans2))
#%%submit!    
resolve()