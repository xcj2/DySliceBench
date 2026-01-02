import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    
    #でかいやつから左右両端のどちらかに動かす
    B=sorted(zip(A,range(N)),reverse=True)
    
    #dp[i][j]は左からi個右からj個埋まっている時の最大値
    dp=[[0]*(N+1) for _ in range(N+1)]
    
    for k in range(N):
        a=B[k][0]
        x=B[k][1]
        
        for i in range(k+1):
            j=k-i
            #右詰
            y=N-j-1
            dp[i][j+1]=max(dp[i][j+1],dp[i][j]+a*abs(x-y))
            
            #左詰
            y=i
            dp[i+1][j]=max(dp[i+1][j], dp[i][j]+a*abs(x-y))
                
    ans=0
    for i in range(N+1):
        ans=max(ans,dp[i][N-i])
    print(ans)
        
    
    

        
        
        

main()
