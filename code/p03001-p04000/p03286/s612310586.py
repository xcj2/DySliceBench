#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code

#なお、任意の整数 M に対して M の −2 進数表現が一意に定まることが証明できます。
#2桁ごとに見るとよかった（もう実験したよ）
def resolve():
    N,=pin()
    n=N
    ans=[]
    a=["00","01","10","11"]
    b=[0,1,-2,-1]
    t=0
    for t in range(30):
        #print(n)
        n4=n%4
        ans.append(a[n4])
        n-=b[n4]
        n//=4
        if abs(n)==0:break
        
    ans.reverse()
    if ans[0][0]=="0":ans[0]=ans[0][1]
    print(*ans,sep="")
        
#%%submit!
resolve()