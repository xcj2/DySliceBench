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
    tmp=(S[0]=="A")
    f=0
    a=""
    for i in range(1,len(S)):
        if S[i]=="C":
            if i>=2 and i<len(S)-1:
                f=1
                tmp+=1
            else:break
        else:a+=S[i]        
    tmp+=(a.islower())
    print(["WA","AC"][tmp==3])
    
    #print()
#%%submit!
resolve()