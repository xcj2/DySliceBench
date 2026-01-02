r1,c1,r2,c2 = map(int,input().split())
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
fact,rfact = factorial(r2+c2+1,mod)
def perm(n,k): #上のfactorialと併用
    return fact[n]*rfact[n-k]%mod
def comb(n,k): #上のfactorialと併用
    return fact[n]*rfact[k]*rfact[n-k]%mod
ans = comb(r1+c1,r1)
#print(ans)
for i in range(r1+1,r2+1):
    ans += comb(i+c1,c1)*comb(r2-c1+c2+1-i,r2-i+1)
    ans %= mod
    #print(ans)
#print(-1)
for i in range(c1+1,c2+1):
    ans += comb(i+r1,r1)*comb(c2-r1+r2+1-i,c2-i+1)
    ans %= mod
    #print(ans)

print(ans)