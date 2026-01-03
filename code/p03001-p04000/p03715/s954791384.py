#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    H,W=pin()

    if H%3==0 or W%3==0:
        print(0)
        return
    #     
    ans=min(H,W)
    for i in range(1,H):
        yoko=W*i
        a=W//2*(H-i)
        b=W*H-yoko-a
        
        t=(max(yoko,a,b)-min(yoko,a,b))
        ans=min(t,ans)

    for j in range(1,W):
        yoko=H*j
        a=(H//2)*(W-j)
        b=W*H-yoko-a
        
        t=(max(yoko,a,b)-min(yoko,a,b))
        ans=min(t,ans)
    print(ans)
#%%submit!
resolve()