#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N,M=pin()#NofKen,MofSi
    PY=[[]for i in range(N)]
    
    for m in range(M):
        p,y=pin()
        PY[p-1].append([y,m])
    #print(PY)
    ANS=[]
    for i in range(N):
        PY[i].sort(key=lambda x:x[0])
        for n,py in enumerate(PY[i]):
            py[0]=n+1
            ANS.append([i+1]+py)
    #print(ANS)
    ANS.sort(key=lambda x:x[2])
    
    
    #print(ANS)
    PY=ANS
    for k in range(M):
        x,y,z=PY[k]
        X,Y=str(x),str(y)
        t,s=6-len(X),6-len(Y)
        if t>0:
            X="0"*t+X
        if s>0:
            Y="0"*s+Y
        print(X+Y)

#%%submit!
resolve()