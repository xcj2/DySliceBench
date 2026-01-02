#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from collections import defaultdict
def resolve():
    N,=pin()
    a=defaultdict(int)

    for i in range(N):
        temp=input()
        a[temp]+=1

    t=a["AC"]+a["WA"]+a["TLE"]+a["RE"]
    #print(a)
    assert t==N
    print("AC x",a["AC"])
    print("WA x",a["WA"])
    print("TLE x",a["TLE"])
    print("RE x",a["RE"])    
#%%submit!
resolve()
