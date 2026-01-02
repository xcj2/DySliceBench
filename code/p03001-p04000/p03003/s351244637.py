
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    S=LI()
    T=LI()
    
    dp=[[0]*(M+1) for _ in range(N+1)]
    dp[0][0]=1
    #dp[i][j]はSのi文字目，Tのj文字目を使う時の通り数
    cumsum=[[0]*(M+2) for _ in range(N+2)]
    #2D累積和
    
    for i in range(1,N+2):
        cumsum[i][1]=1
    for j in range(1,M+2):
        cumsum[1][j]=1
    
    for i in range(N):
        for j in range(M):
            if S[i]==T[j]:
                dp[i+1][j+1]=(cumsum[i+1][j+1])%mod
                
            cumsum[i+2][j+2]=(cumsum[i+2][j+1]+cumsum[i+1][j+2]-cumsum[i+1][j+1]+dp[i+1][j+1])%mod
            
    print(cumsum[-1][-1])
    """
    for i in range(N+2):
        print(' '.join(map(str, cumsum[i])))
        
    for i in range(N+1):
        print(' '.join(map(str, dp[i])))"""

main()
