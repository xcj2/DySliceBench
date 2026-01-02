MOD = 10 ** 9 + 7
def init(n=5*10**5):
    fact = [1] * (n + 1)
    for i in range(2, n+1):
        fact[i] = i * fact[i-1] % MOD
    inv = [1] * (n + 1)
    inv[n] = pow(fact[n], MOD-2, MOD)
    for i in range(n, 0, -1):
        inv[i-1] = i * inv[i] % MOD
    return fact, inv

def nCr(n, r):
    r = min(r, n - r)
    return fact[n] * (inv[n-r] * inv[r] % MOD) % MOD

def nPr(n, r):
    return fact[n] * inv[n-r] % MOD

N, M = map(int, input().split())
fact, inv = init()
res = 0
sgn = 1
for i in range(N+1):
    res += sgn * nPr(M - i, N - i) * nCr(N, i)
    res %= MOD
    sgn *= -1
print(nPr(M, N) * res % MOD)