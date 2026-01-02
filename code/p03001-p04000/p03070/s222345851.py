import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=998244353

    """
    aiが300以下なのが嬉しい，総和でなんかできる．
    dp[i][j]でi番目まで見て合計がj，j<=N*max(a)なので合計O(N^2 max(a))，これでRの通り数が求まるがGB用に何が残っているのかわからん-
    余事象，R>=sum(a)/2 ならダメなわけで
    
    """
    N=I()
    A=[0]*N
    for i in range(N):
        A[i]=I()
    
    S=sum(A)
    
    dp=[[0]*(S+1) for _ in range(N+1)]
    # i番目まで見て，Rの総和がjの通り数
    dp[0][0]=1
    
    for i in range(N):
        a=A[i]
        for j in range(S+1):
            dp[i+1][j]=(dp[i+1][j] + dp[i][j]*2)%mod#g,b
            if j+a<=S:
                dp[i+1][j+a]=(dp[i+1][j+a] + dp[i][j])%mod#r
    
    rem=0
    for j in range((S+1)//2,S+1):
        rem=(rem+dp[-1][j])%mod#RがS/2以上なら基本的に被りを考慮する必要はない
    ans=pow(3,N,mod)-rem*3#r,g,b3色分
    ans%=mod#負数防止
        
    if S%2==0:
        # 0,S/2,S/2は被って数えている，bを使わないバージョン
        dp2=[[0]*(S+1) for _ in range(N+1)]
        # i番目まで見て，Rの総和がjの通り数
        dp2[0][0]=1
        
        for i in range(N):
            a=A[i]
            for j in range(S+1):
                dp2[i+1][j]=(dp2[i+1][j] + dp2[i][j])%mod#g
                if j+a<=S:
                    dp2[i+1][j+a]=(dp2[i+1][j+a] + dp2[i][j])%mod#r
                    
        temp=dp2[-1][S//2]
        ans+=temp*3
        
    
    print(ans%mod)
    
    # for i in range(N+1):
    #     print(dp[i])
            

main()
