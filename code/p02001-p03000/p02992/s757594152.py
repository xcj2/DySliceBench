import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    """
    末尾だけが重要，dp[i][j]でi枚目まで見て末尾がj，O(NK)
    Nが小さければ問題ない，jの部分は(N/j)の切り捨てでまとめられる．
    前半部分は1~sqrt(N)で，各組1こずつ．後半はN/i (i<=sqrt(N))
    
    """
    N,K=MI()
    M=int(N**0.5)
    cnt=[]
    
    i=1
    while i<=N:
        if i<=M:
            cnt.append(1)
            i+=1
        else:
            temp=int(N/i)
            cnt.append(int(N/temp-i+1))
            i=int(N/temp +1)
            
    N2=len(cnt)
            

    
    dp=[[0]*N2 for _ in range(K)]
    #dp[i][j]はi個見て，最後尾がグループL[j]に属す場合の数
    #j番目のグループはMーj番目までのグループと組める
    
    for j in range(N2):
        dp[0][j]=cnt[j]
        
    for i in range(K-1):
        S=[0]*(N2+1)
        for j in range(N2):
            S[j+1]=(S[j]+dp[i][j])%mod
        
        for j in range(N2):
            dp[i+1][j]=(S[N2-j]*cnt[j])%mod
            
    ans=0
    for j in range(N2):
        ans=(ans+dp[-1][j])%mod
        
    print(ans)


    
    

main()
