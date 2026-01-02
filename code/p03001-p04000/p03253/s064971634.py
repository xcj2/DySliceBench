def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

MOD = 10 ** 9 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, 11**5):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % MOD

def solve():
    N, M = map(int, input().split())
    l = factorize(M)
    
    ans = 1
    for _, c in l:
        ans = ans * cmb(c+N-1, c) % MOD
        
    return ans

print(solve())