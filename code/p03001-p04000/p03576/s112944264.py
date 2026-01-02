#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    xy=[[0,0] for _ in range(N)]
    y=[0]*N
    
    for i in range(N):
        xy[i][0],xy[i][1]=MI()
        y[i]=xy[i][1]
        
    xy.sort()
    y.sort()
    
    def count(l,r,d,u):
        cnt=0
        for i in range(N):
            if l<=xy[i][0]<=r:
                if d<=xy[i][1]<=u:
                    cnt+=1
        return cnt
    
    ans=10**20
    for i in range(N):
        for j in range(i+1,N):
            for ii in range(N):
                for jj in range(ii+1,N):
                    l=xy[i][0]
                    r=xy[j][0]
                    d=y[ii]
                    u=y[jj]
                    if count(l,r,d,u)==K:
                        ans=min(ans,(r-l)*(u-d))
    print(ans)

main()
