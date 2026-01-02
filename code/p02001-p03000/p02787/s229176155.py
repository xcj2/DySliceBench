import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,N=MI()
    A=[0]*N
    B=[0]*N
    
    for i in range(N):
        A[i],B[i]=MI()
        
    inf =10**20
    dp=[[inf]*(H+1)for _ in range(N+1)]
    # dp[i]はi番目の魔法まででhpをj減らす方法
    
    dp[0][0]=0
    
    for i in range(N):
        a=A[i]
        b=B[i]
        for j in range(H+1):
            if j-a>=0:
                dp[i+1][j]=min(dp[i+1][j],
                               dp[i][j],
                               dp[i+1][j-a]+b)
            else:
                dp[i+1][j]=min(dp[i+1][j],
                               dp[i][j],
                               dp[i+1][0]+b)
                
    print(dp[-1][-1])

main()
