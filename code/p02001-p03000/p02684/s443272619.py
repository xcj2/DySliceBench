#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    N,K=pin()
    A=list(pin())#henkan
    seen=set([0])
    junban=[0]
    #print(seen)
    
    
    point_1=0
    for n in range(N):
        #print(A[point_1])
        point_1=A[point_1]-1
        junban.append(point_1)
        if (point_1) in seen:
            #print(n)
            b=n
            break 
        seen.add(point_1)
        
        
    #print(n,junban,point_1)
    for m in range(len(junban)):
        if junban[m]==point_1:
            a=m
            break
    g=(len(junban)-1-a)
    #print(g)
    if K>a:
        k=(K-a)%g
        print(junban[a+k]+1)
    else:print(junban[K]+1)
#%%submit!
resolve()