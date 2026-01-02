#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    N,HP=pin()
    weapon=[tupin() for _ in range(N)]
    weapon.sort(key=lambda x:x[0])
    a=weapon[-1][0]
    ans=0
    weapon.sort(key=lambda x:x[1],reverse=True)
    for w in weapon:
        if w[1]>a:
            HP-=w[1];ans+=1
            if HP<=0:break
    if HP>0:
        ans+=((HP-1)//a)+1
    print(ans)
#%%submit!
resolve()