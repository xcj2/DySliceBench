#!/usr/bin/env python3

MOD = int(1e9)+7

def extgcd(a, b):
    if b == 0:
        return [1, 0, a]
    x, y, g = extgcd(b, a%b)
    return [y, x - a//b * y, g]


def mod_inverse(a, m):
    x, y, _ = extgcd(a, m)
    return (m+x%m) % m


n, k = map(int, input().split())

maxf = 2*n + 10
f = [1 for _ in range(maxf)]
invf = [1 for _ in range(maxf)]

for i in range(1, maxf):
    f[i] = (i * f[i - 1]) % MOD
 
invf[maxf-1] = pow(f[maxf - 1], MOD-2, MOD)
for i in range(maxf-1, 0, -1):
    invf[i-1] = (i*invf[i]) % MOD
 
def comb(a, b):
    if b > a:
        return 0
    return (((f[a]*invf[b]) % MOD) * invf[a-b]) % MOD

a = [ int(x) for x in input().split() ]
a.sort(reverse=True)

ans = 0

for i, v in enumerate(a):
    ans += v*comb(n-i-1, k-1)
    ans %= MOD
    ans -= v*comb(i, k-1)
    ans %= MOD
    
print(ans)

