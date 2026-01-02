#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
import copy

def main():
    mod=10**9+7
    N,M=MI()
    inf=1000
    D=[[inf]*N for _ in range(N)]
    for _ in range(M):
        a,b=MI()
        a-=1
        b-=1
        D[a][b]=1
        D[b][a]=1
        
    for i in range(N):
        D[i][i]=0
        
    def warshall_floyd(d):
        #d[i][j]: iからjへの最短距離
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j],d[i][k] + d[k][j])
           
        for i in range(N):
            for j in range(N):
                if d[i][j]==inf:
                    return True
        return False
    cnt=0 
    for i in range(N):
        for j in range(i,N):
            if D[i][j]==1:
                d=copy.deepcopy(D)
                d[i][j]=inf
                d[j][i]=inf
                if warshall_floyd(d):
                    cnt+=1
                    
    print(cnt)
    
    



main()
