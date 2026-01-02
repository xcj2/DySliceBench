n,m,k = map(int, input().split())
mod = 998244353
def factorial(N,MOD,r=True):
    fact = [1]*(N+1)
    rfact = [1]*(N+1)
    r = 1
    for i in range(1,N+1):
        fact[i] = r = r * i % MOD
    rfact[N] = r = pow(fact[N],MOD-2,MOD)
    for i in range(N, 0, -1):
        rfact[i-1] = r = r * i % MOD
    if r:
        return fact,rfact
    else:
        return fact
fact,rfact = factorial(2*10**5,mod)

def perm(n,k): #上のfactorialと併用
    return fact[n]*rfact[n-k]%mod
def comb(n,k): #上のfactorialと併用
    return fact[n]*rfact[k]*rfact[n-k]%mod

ans = 0
now = pow(m-1,n-1-k)
for i in range(k,-1,-1):
    ans += comb(n-1,i)*now
    now *= (m-1)
    now %= mod
    ans %= mod

ans *= m
ans %= mod
print(ans)