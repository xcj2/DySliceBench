n, m, k = map(int, input().split())

def bin(a, b, p):
    res = 1
    while b > 0:
        if b & 1 > 0:
            res = res * a % p
        a = a * a % p
        b >>= 1

    return res

MOD = 998244353
N = 200000 + 50
f = [0 for i in range(N)]
invf = [0 for i in range(N)]

f[0] = invf[0] = 1
for i in range(1, N):
    f[i] = f[i-1] * i % MOD

invf[n] = bin(f[n], MOD-2, MOD)
for ri in range(1, N-1):
    i = n - ri
    invf[i] = invf[i+1] * (i+1) % MOD

def binom(n, m):
    if n < m or n < 0 or m < 0:
        return 0
    return f[n] * invf[m] % MOD * invf[n-m] % MOD

def g(n, m):
    return m * bin(m-1, n-1, MOD)

ans = 0
for i in range(0, k+1):
    # print(n-i, i, binom(n-1, i), bin(n-i, m, MOD), n-i, m)
    ans = (ans + binom(n-1, i) * g(n-i, m)) % MOD

print(ans)