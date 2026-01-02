
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    S=LI()
    T=LI()

    dp=[[0]*(M+1) for _ in range(N+1)]
    # dp[i][j]はSをi文字，Tをj文字見た時の通り数
    
    for i in range(N+1):
        dp[i][0]=1
        
    for j in range(M+1):
        dp[0][j]=1
    
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1]=dp[i+1][j]+dp[i][j+1]
            if S[i]!=T[j]:
                dp[i+1][j+1]-=dp[i][j]
            dp[i+1][j+1]%=mod
            
            
    print(dp[-1][-1])
            
                
            
    

    

main()
