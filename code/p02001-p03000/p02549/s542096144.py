import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=998244353
    N,K=MI()
    
    dp=[0]*N
    dp[0]=1
    
    L=[0]*K
    R=[0]*K
    for i in range(K):
        L[i],R[i]=MI()
    
    
    for i in range(N-1):
        for k in range(K):
            l= i + L[k]
            r= i + R[k] +1
            if l<N:
                dp[l]+=dp[i]
                dp[l]%=mod
            if r<N:
                dp[r]-=dp[i]
                dp[r]%=mod
        if i!=0:
            dp[i+1]+=dp[i]
        dp[i+1]%=mod
        
                
    print(dp[-1])
            
            

main()
