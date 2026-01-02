n,k = map(int,input().split())
mod = 10**9 + 7
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
fact,rfact = factorial(2*n,mod)

def perm(n,k): #上のfactorialと併用
    return fact[n]*rfact[n-k]%mod
def comb(n,k): #上のfactorialと併用
    return fact[n]*rfact[k]*rfact[n-k]%mod
ans = 0

if k+1>=n:
    ans = comb(2*n-1,n)
    print(ans)
else:
    ans = 0
    for i in range(k+1):
        ans += comb(n,i)*comb(n-1,i)
        ans %= mod
    print(ans)