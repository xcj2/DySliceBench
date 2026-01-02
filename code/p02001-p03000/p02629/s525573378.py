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
    ans=[]
    t=0
    
    max_digit=len("1000000000000001")
    ans=[]
    for i in range(max_digit):
        a=(N-1)%26+1
        if a==0:break
        ans.append(a)
        if a==N :
            break
        N=(N-a)//26

    ans.reverse()
#    print(ans)
    A=""
    for a in ans:
        A+=chr(ord("a")-1+a) 
    print(A)   
#%%submit!
resolve()
