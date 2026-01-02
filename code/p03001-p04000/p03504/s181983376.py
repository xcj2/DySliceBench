#!/usr/bin/env PyPy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
mod=10**9+7

def main():
    N,C=MI()
    T=10**5
    
    tc=[[0]*(T+1) for _ in range(C)]
    
    
    for i in range(N):
        s,t,c=MI()
        tc[c-1][s-1]+=1
        tc[c-1][t]-=1
        
    for c in range(C):
        for i in range(T):
            tc[c][i+1] +=tc[c][i]
            
    ans=0
    
    for i in range(T+1):
        temp=0
        for c in range(C):
            if tc[c][i]>0:
                temp+=1
        ans=max(ans,temp)
        
    print(ans)        
                    
        



main()
