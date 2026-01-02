from collections import Counter

mod = 1000000007

# nの素因数分解
def factor(n):
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
        half = int(n / 2)
        half_x = mod_pow(x, half)
        return half_x * half_x % mod
    else:
        return x * mod_pow(x, n - 1) % mod


def nCr(n, r):
    x = 1
    r = min(r, n - r)
    for i in range(r):
        x *= n - i
        x %= mod
        x *= mod_pow(i + 1, mod - 2)
        x %= mod
    return x


def solve():
    N, M = map(int, input().split())
    p = factor(M)
    s = 1
    for i in p.values():
        s *= nCr(i + N - 1, N - 1)
        s %= mod
    print(s)


solve()