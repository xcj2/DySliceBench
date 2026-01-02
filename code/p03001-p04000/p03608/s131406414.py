#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

import itertools

def main():
    mod=10**9+7
    N,M,R=MI()
    r=LI()
    inf=10**10
    d=[[inf]*N for _ in range(N)]
    for _ in range(M):
        a,b,c=MI()
        a-=1
        b-=1
        d[a][b]=c
        d[b][a]=c
    for i in range(N):
        d[i][i]=0
        
    def warshall_floyd(d):
        #d[i][j]: iからjへの最短距離
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j],d[i][k] + d[k][j])
        return d
        
    d=warshall_floyd(d)
    
    ans=inf
    for ite in itertools.permutations(range(R), R):
        temp=0
        for i in range(R-1):
            a=r[ite[i]]-1
            b=r[ite[i+1]]-1
            temp+=d[a][b]
        ans=min(ans,temp)
        
    print(ans)
            
        
        
    
    
    

main()
