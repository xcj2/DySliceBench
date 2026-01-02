MOD = 10**9 + 7

n, k = map(int, input().split())

def getComb(n, k, MOD):
    if n < k:
        return 0
    if n-k < k:
        k = n-k
    comb = 1
    for x in range(n-k+1, n+1):
        comb = (comb * x) % MOD
    d = 1
    for x in range(1, k+1):
        d = (d * x) % MOD
    comb *= pow(d, MOD-2, MOD)
    return comb % MOD

def getCombNs(n, invs, MOD):
    combNs = [1] * (n//2+1)
    for x in range(1, n//2+1):
        combNs[x] = (combNs[x-1] * (n-x+1) * invs[x]) % MOD
    return combNs + combNs[:(n+1)//2][::-1]

def getInvs(n, MOD):
    invs = [1] * (n+1)
    for x in range(2, n+1):
        invs[x] = (-(MOD//x) * invs[MOD%x]) % MOD
    return invs


ans = getComb(2*n-1, n, MOD)

if k < n-1:
    m = n-1-k
    invs = getInvs(n+3, MOD)
    combNs = getCombNs(n, invs, MOD)
    combN1s = getCombNs(n-1, invs, MOD)

    for i in range(m):
        ans -= combN1s[i] * combNs[i+1] % MOD
        ans %= MOD

print(ans)
