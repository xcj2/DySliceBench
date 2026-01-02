n, k = map(int, input().split())
mod = 10**9+7
def make_fact(n):#0~nの階乗を求める
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1]*i%mod
    return fact
fact = make_fact(n*2) #＠
def make_fact_inv(n):#0~nの階乗のmodに関する逆元を求める
    fact_inv = [1]*(n+1)
    fact_inv[n] = pow(fact[n], mod-2, mod)#フェルマーの小定理
    for i in range(n, 0, -1):
        fact_inv[i-1] = fact_inv[i]*i%mod
    return fact_inv
fact_inv = make_fact_inv(n*2)#＠
def comb(n, k):#nCk
    return fact[n]*fact_inv[k]*fact_inv[n-k]%mod
mod = 10**9+7
ans = 0
for i in range(n):
    m = n-i
    c = n-m
    if c+i>k*2:
        continue
    ans+=comb(n, i)*comb(m+c-1, m-1)%mod
    ans%=mod
print(ans)