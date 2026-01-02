#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    inf=10*20
    N=I()
    A=[[]for _ in range(N)]
    A2=[[1]*N for _ in range(N)]
    ans=0
    for i in range(N):
        A[i]=LI()
        ans+=sum(A[i])
        
    


        
    def warshall_floyd(d):
        #d[i][j]: iからjへの最短距離
        for k in range(N):
            for i in range(N):
                if k==i:
                    continue
                for j in range(N):
                    if j==i or j==k:
                        continue
                    dd=d[i][k] + d[k][j]
                    #d[i][j] = min(d[i][j],d[i][k] + d[k][j])
                    
                    if dd==d[i][j]:
                        A2[i][j]=0
                    elif dd<d[i][j]:
                        return -1
        return 1
    
    if warshall_floyd(A)==-1:
        ans=-2
    else:
        ans=0
        for i in range(N):
            for j in range(N):
                ans+=A[i][j]*A2[i][j]
        
        
    print(ans//2)
        
    

main()