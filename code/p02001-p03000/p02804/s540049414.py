mod = 10**9+7
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
def make_fact(n):#0~nの階乗を求める
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1]*i%mod
    return fact
fact = make_fact(N) #＠
def make_fact_inv(n):#0~nの階乗のmodに関する逆元を求める
    fact_inv = [1]*(n+1)
    fact_inv[n] = pow(fact[n], mod-2, mod)#フェルマーの小定理
    for i in range(n, 0, -1):
        fact_inv[i-1] = fact_inv[i]*i%mod
    return fact_inv
fact_inv = make_fact_inv(N)#＠
def comb(n, k):#nCk
    return fact[n]*fact_inv[k]*fact_inv[n-k]%mod
ans = 0
for i in range(N):
    if i+1>=K:
        ans+=A[i]*comb(i, K-1)
        ans%=mod
    if N-i>=K:
        ans-=A[i]*comb(N-i-1, K-1)
        ans%=mod
print(ans)


