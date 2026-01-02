from collections import defaultdict
MOD = 10**9 + 7

def Mod_Power(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

def Mod_Inverse(a, mod):
    return Mod_Power(a, mod-2, mod)

def Mod_Combination(n, k, mod):
    p, q = 1, 1
    for i in range(n-k+1, n+1):
        p = (p * i) % mod
    for i in range(2, k+1):
        q = (q * i) % mod
    return int(p * Mod_Inverse(q, mod) % mod)

N, M = map(int, input().split())
prime_factors = defaultdict(int)
i, L = 2, M
while True:
    while L % i == 0:
        L /= i
        prime_factors[i] += 1
    if L == 1 or i * i > M:
        break
    i += 1
if L > 1:
    prime_factors[L] = 1
res = 1
for key in prime_factors:
    res = res * Mod_Combination(prime_factors[key] + N - 1, N - 1, MOD) % MOD
print(int(res))