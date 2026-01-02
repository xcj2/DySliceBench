from collections import Counter

mod = 1000000007

# nの素因数分解

def prime(n):
    d = Counter()
    i = 2
    while i*i <= n:
        while n%i == 0:
            n //= i
            d[i] += 1
        i += 1
    if n > 1:
        d[n] += 1
    return d

# xのn乗を計算する
def mod_pow(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_x = mod_pow(x, n // 2)
        return half_x * half_x % mod
    else:
        return x * mod_pow(x, n-1) % mod

fact = [1] * 100100
inv = [1] * 100100
for k in range(1, 100100):
    fact[k] = fact[k-1] * k % mod
    inv[k] = mod_pow(fact[k], mod-2)

def nCr(n, r):
    return fact[n] * inv[r] % mod * inv[n-r] % mod

def solve():
    N, M = map(int, input().split())
    p = prime(M)
    s = 1
    for i in p.values():
        s *= nCr(i + N - 1, N - 1)
        s %= mod
    print(s)

solve()
