#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    W="dream dreamer erase eraser".split(" ")
    #print(W)
    S=input()
    t=[S]
    while(t!=[]):
        temp=t.pop()
        for w in W:
            m=len(w)
            if(temp[-m:])==w:
                f=temp[:-m]
                if f=="":
                    print("YES")
                    return
                t.append(f)
    print("NO")
#%%submit!
resolve()