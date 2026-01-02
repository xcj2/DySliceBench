#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
dxdy=[(1,0),(0,1),(-1,0),(0,-1)]
def resolve():
    H,W=pin()
    maze=[input() for h in range(H)]
    
    for i in range(H):
        for j in range(W):
            if maze[i][j]=="#":
                f=0
                for head in dxdy:
                    x,y=head
                    try:k=maze[i+x][j+y]
                    except IndexError:k=None
                    if k!=None and k=="#":
                        f=1
                if f==0:
                    print("No")
                    return
    print("Yes")
            
#%%submit!
resolve()