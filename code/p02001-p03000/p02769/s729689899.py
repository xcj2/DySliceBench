n,k = map(int,input().split())
#逆元nCr
mod = 10**9+7
def cmb(n,r,mod):
    r = min(r, n-r)
    return (fact[n] * factinv[r] * factinv[n-r]) % mod
def h(n,r,mod):
    return cmb(n+r-1,r,mod)
def makefact(n,mod):
    fact = [1,1]
    factinv = [1,1]
    inv = [0,1]
    for i in range(2,n+1):
        fact.append((fact[-1]*i) % mod)
        inv.append(-inv[mod%i]*(mod//i)%mod)
        factinv.append((factinv[-1]*inv[-1])%mod)
    return fact,factinv
fact,factinv = makefact(n,mod)


ans = 0
for i in range(min(n,k+1)):
    ans = (ans+cmb(n,i,mod)*h(n-i,i,mod))%mod
print(ans)