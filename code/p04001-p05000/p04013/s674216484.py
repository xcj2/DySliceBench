import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,A=MI()
    x=LI()
    M=max(x)
    
    #dp[i][j][k]はi番目まで，j枚で，和がkにできるか
    dp=[[[0]*(N*M+1) for j in range(N+1)] for _ in range(N+1)]
    dp[0][0][0]=1
    
    for i in range(N):
        for j in range(i+1):
            for k in range(N*M+1-x[i]):
                if dp[i][j][k]:
                    dp[i+1][j][k]+=dp[i][j][k]
                    dp[i+1][j+1][k+x[i]]+=dp[i][j][k]
                    

        
    ans=0
    for j in range(1,N+1):
        if j*A<=N*M:     
            ans+=dp[-1][j][j*A]
        
    print(ans)
 

                
    
        
            
            
    
            
        
        
            

main()
