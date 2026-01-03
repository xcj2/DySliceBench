#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
import random
def resolve():
    
    S=input()
    A="dream dreamer erase eraser".split()
    #print(A)
    que=[S]
    while(que!=[]):
        t=len(que)
        #print(t)
        vS=que.pop(random.randint(0,t-1))
        if vS=="":
            print("YES")
            return
        for w in A:
            r=len(w)
            if vS[:r]==w:
                que.append(vS[r:])
        #print(que,"k")    

    print("NO")
#%%submit!
resolve()