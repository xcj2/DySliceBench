#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    W,H,N=pin()
    ans=[0,W,0,H]#ans[[xの範囲][yの範囲]]
    for n in range(N):
        x,y,a=pin()
        if a==1:
            ans[0]=max(ans[0],x)
        elif a==2:
            ans[1]=min(ans[1],x)
        elif a==3:
            ans[2]=max(ans[2],y)
        else:
            ans[3]=min(ans[3],y)
    t=((ans[1]-ans[0])*(ans[3]-ans[2]))
    if ans[1]-ans[0]<0 or ans[3]-ans[2]<0:t=0
    print(t)    
#%%submit!
resolve()