N,M,K = map(int, input().split())
mod = 998244353


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

bekizyo = [1] * N

for i in range(1, N):
    bekizyo[i] = bekizyo[i-1] * (M - 1) % mod



ans = 0

for i in range(K + 1):
    ans += comb(N-1, i) * M * bekizyo[N-i-1]
    ans %= mod

print(ans)