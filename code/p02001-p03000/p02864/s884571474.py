import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    """
    メモ
    K=0なら，左から見て登った数を数える，grandGarden
    K>=1の時，塗る列は左右どちらかと同じ高さにする．同じ高さで何個か連なっていると面倒かも？
    左右どちらかと同じ高さにするというのは逐次的な話，1,1,1,5,4,5,1でK=3なら答えは1
    K個を無視できると考える．
    dp[x][y][k]で，x〜yまで，k個無視と考えれば遷移も含めて5乗くらいで行けそう
    =>0からスタートだけで良い，dp[x][k]で行けそう？．xのところは使っているものとする．
    =>「K回使える」よりも「使った数がいくつか」を記憶しておくほうが楽そう
    """
    N,K=MI()
    H=[0]+LI()
    N+=1
    inf=10**12
    dp=[[inf]*(N) for _ in range(N)]
    # dp[i][j]はi番目まで見て，j個の要素からなる
    dp[0][0]=0
    
    for i in range(1,N):
        for j in range(N):
            temp=inf
            for k in range(i):#どこからくるか
                temp=min(temp,dp[k][j-1]+max(0,H[i]-H[k]))
            dp[i][j]=temp
    
    ans=inf
    
    for i in range(N):
        ans=min(ans,dp[i][N-K-1])
    print(ans)

main()
