#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from collections import  Counter
def resolve():
    N,=pin()
    C=input()
    X=Counter(C)
    a=(min(X["R"],X["W"]))#すべての色を変えにしてしまったらいい時
    c=list(C)


    rightlimit_R=-1
    for i in range(1,N):
        if c[-i]=="R":
            rightlimit_R=N-i
            break
    cnt=0

    for i in range(N):

        if c[i]=="W":

            for j in range(rightlimit_R-1,0,-1):
                if c[j]=="R":

                    
                    rightlimit_R=j
                    break

            cnt+=1
        if rightlimit_R<=i:
            
            break


    print(min(a,cnt))
    
#%%submit!
resolve()