#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
mod=10**9+7

def main():
    H,W=MI()
    c=[[] for _ in range(10)]
    A=[[] for _ in range(H)]
    
    for i in range(10):
        c[i]=LI()
    for i in range(H):
        A[i]=LI()
        
    def warshall_floyd(d):
        #d[i][j]: iからjへの最短距離
        n=10
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j],d[i][k] + d[k][j])
        return d
    
    c=warshall_floyd(c)
    
    ans=0
    for i in range(H):
        for j in range(W):
            if A[i][j]==-1:
                continue
            else:
                ans+=c[A[i][j]][1]
                
    print(ans)
            
    
    

main()
