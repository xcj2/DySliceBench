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
    A=list(pin())
    ans=0
    for i in range(10**6):
        #print(A)
        B=[0]*3
        for a in range(3):
            if A[a]%2!=0:print(ans);return
        B[0]=(A[1]+A[2])//2
        B[1]=(A[0]+A[2])//2
        B[2]=(A[0]+A[1])//2
        A=B[:]
        ans+=1
    print(-1)
    
                
    
#%%submit!
resolve()