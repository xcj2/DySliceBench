# coding: utf-8
MOD = 10**9+7

# 二分累積法による a^n mod の計算
def modpow(a, n):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % MOD
        a = a * a % MOD
        n >>= 1
    return res

# nCr mod.p (n <= 10**6)
MAX = 1000010
fac = [0] * MAX 
finv = [0] * MAX
inv = [0] * MAX
def COMinit():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD//i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD
# より高速化が必要な場合
def COM(n, k):
    res = 1
    for i in range(k):
        res = res * (n-i) % MOD
    return res * finv[k] % MOD

COMinit()
n, a, b = map(int, input().split())
tot = modpow(2,n) - 1
ans = (tot - COM(n,a) - COM(n,b)) % MOD
print(ans)