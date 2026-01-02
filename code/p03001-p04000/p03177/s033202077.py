# dp[n][i][j]=(頂点iから頂点jへ行く長さnのパスの個数)
# dp[n][i][j]=sum(dp[n-1][i][k]*a[k][j])⇒DP[n]=DP[n-1]*A DP[0]=Eより DP[n]=A^n
import sys
input = sys.stdin.readline

def dot(A,B,MOD=1000000007):
    N,M,L = len(A),len(A[0]),len(B[0])
    res = [[0]*L for i in range(N)]
    for i in range(N):
        for j in range(L):
            s = 0
            for k in range(M):
                s = (s + A[i][k]*B[k][j]) % MOD
            res[i][j] = s
    return res

def matPow(A,x,MOD=1000000007):
    N = len(A)
    res = [[0]*N for i in range(N)]
    for i in range(N):
        res[i][i] = 1
    for i in range(x.bit_length()):
        if (x>>i) & 1:
            res = dot(res,A)
        A = dot(A,A)
    return res

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    a = [list(map(int,input().split())) for i in range(n)]
    dp = matPow(a,k)
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += dp[i][j]
    print(ans%mod)

main()