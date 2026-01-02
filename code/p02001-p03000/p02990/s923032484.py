N, K = map(int, input().split())
INF = 10**9 + 7
def powmod(a, n, mod):
    p = 1
    while n > 0:
        if n % 2 == 0:
            a = a**2 % mod
            n /= 2
        else:
            p *= a
            p %= mod
            n -= 1
    return p

def invmod(a, mod):
    return powmod(a, mod-2, mod)

fac = [1] * 2002
inv = [1] * 2002
for i in range(2002):
    if i == 0:
        fac[i] = 1
        inv[i] = 1
    else:
        fac[i] = fac[i-1] * i % INF
        inv[i] = inv[i-1] * invmod(i, INF) % INF


def combmod(n, k, mod):
    if n < k : return 0
    else:
        bunsi = fac[n]
        bunbo = inv[k] * inv[n-k]
        return bunsi * bunbo % mod

for i in range(1, K+1):
    print((combmod(K-1, i-1, INF) * combmod(N-K+1, i, INF))%INF)