import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=998244353
    N,S=MI()
    A=LI()
    
    dp=[[0]*(S+1)for _ in range(N+1)]
    #dp[i][j]はi番目まで見た時に和がjになる組み合わせを何通り作れるか．
    #ただし，iを増やすたびにj=0が1つ増える（Lがひとつずれたものと対応）
    
    for i in range(N):
        a=A[i]
        dp[i][0]+=1
        for j in range(S+1):
            dp[i+1][j]=(dp[i+1][j]+dp[i][j])%mod
            if j+a<=S:
                dp[i+1][j+a]=(dp[i+1][j+a]+dp[i][j])%mod
                
    ans=0
    for i in range(N+1):
        ans=(ans+dp[i][-1])%mod
        
    print(ans)
                
            
    
            
        

main()
