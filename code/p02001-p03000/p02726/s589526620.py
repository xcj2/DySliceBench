#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
import collections
def resolve():
    N,P,Q=pin()#
    P-=1
    Q-=1#0-index
    ans=[0]*N
    
    
    for i in range(N):
        seen=[0]*N #BFS so 
        d=collections.deque()
        d.append((i,0))
        for j in range(1,N*10):
            if len(d)==0:break
            a,b=d.popleft()
            if a<0 or a>=N or seen[a]:
                continue
            seen[a]=1
            ans[b]+=1
            d.append((a+1,b+1))
            d.append((a-1,b+1))
            if a==P:
                d.append((Q,b+1))
            if a==Q:
                d.append((P,b+1))
    for n,a in enumerate(ans):
        if n!=0:print(a//2)
        
                
            
#%%submit!
resolve()