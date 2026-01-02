n, m = map(int, input().split())
mod = 10**9 + 7
def setfact(l, mod):
    global fact
    global ifact
    fact = [1]
    for i in range(1, l+1):
        fact.append(fact[-1]*i%mod)
    ifact = [0] * (l+1)
    ifact[-1] = pow(fact[-1], mod-2, mod)
    for i in range(l, 0, -1):
        ifact[i-1] = ifact[i] * i %mod
def comb(n, m, mod):
    global fact
    global ifact
    return fact[n]*ifact[n-m]*ifact[m]%mod
def p(n, m, mod):
    global fact
    global ifact
    return fact[n]*ifact[n-m]%mod
ans = 0
setfact(m, mod)
for k in range(n+1):
    ans += p(m-k, n-k, mod)*comb(n, k, mod) * (-1)**k
    ans %= mod
    if ans < 0:
        ans += mod
ans *= p(m, n, mod)
ans %= mod
print(ans)