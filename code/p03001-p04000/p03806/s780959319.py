import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,Ma,Mb=MI()
    a=[0]*N
    b=[0]*N
    c=[0]*N
    cab=[[0,0,0] for _ in range(N)]
    for i in range(N):
        cab[i][1],cab[i][2],cab[i][0]=MI()
    cab.sort()
    for i in range(N):
        a[i]=cab[i][1]
        b[i]=cab[i][2]
        c[i]=cab[i][0]
        
    
    inf=10**5
    #dp[i][j][k]はi番目の商品まででaがjg,bがkgをとるときの最低金額
    dp=[[[inf]*(N*10+1) for _ in range(N*10+1)] for i in range(N+1)]
    dp[0][0][0]=0
    
    ans=inf
    for i in range(N):
        for j in range(N*10+1-a[i]):
            for k in range(N*10+1-b[i]):
                if dp[i][j][k]!=inf:
                    dp[i+1][j][k]=dp[i][j][k]
                    dp[i+1][j+a[i]][k+b[i]]=min(dp[i+1][j+a[i]][k+b[i]],dp[i][j][k]+c[i])
                    if (j+a[i])*Mb==(k+b[i])*Ma:
                        ans=min(ans,dp[i+1][j+a[i]][k+b[i]])
                    
    if ans==inf:
        print(-1)
    else:
        print(ans)
    
    
    

main()
