#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N,=pin()
    #a>=b>=c (a,b,c)->(x,y,z) no junnretu kakeru
    ans=[0]*N
    for a in range(1,101):
        for b in range(1,a+1):
            for c in range(1,b+1):
                temp=((a+b)**2+(c+b)**2+(a+c)**2)//2
                if temp>N:break
                #print(a,b,c,temp)

                if a==b:
                    if b==c:
                        cnt=1
                    else:
                        cnt=3
                elif b==c:cnt=3
                else:cnt=6
                ans[temp-1]+=cnt
    print(*ans,sep="\n")
#%%submit!
resolve()