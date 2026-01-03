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
    N,A,B=pin()
    S=input()
    a=0
    b=0
    for s in S:
        #print(s)
        if s=="c":
            print("No")
            continue
        elif s=="a":
            a+=1
        else:
            
            if b>=B:
                print("No")
                continue
            b+=1
        #print(s,a+b)
        if (a+b)<=(A+B):
            print("Yes")
        else:print("No")
    

#%%submit!
resolve()