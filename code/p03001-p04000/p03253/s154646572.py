def factorize(n):
    factor = []
    if n % 2 == 0:
        f = [2, 1]
        n //= 2
        while n % 2 == 0:
            n //= 2
            f[1] += 1
        factor.append(f)
    k = 3
    while k * k <= n:
        if n % k == 0:
            f = [k, 1]
            n //= k
            while n % k == 0:
                n //= k
                f[1] += 1
            factor.append(f)
        k += 2
    if n != 1:
        factor.append([n, 1])
    return factor

def factorial(n, mod):
    fac = [0] * (n + 1)
    inv = [0] * (n + 1)
    fac[0], inv[0] = 1, 1
    for i in range(1, n + 1):
        fac[i] = fac[i-1] * i % mod
        inv[i] = inverse(fac[i], mod)
    return fac, inv

def inverse(a, mod):
    a %= mod # 除数が正なら正になる
    p = mod
    x, y = 0, 1
    while a > 0:
        n = p // a
        p, a = a, p % a, 
        x, y = y, x - n * y
    return x % mod # 除数が正なら正になる

n, m = map(int, input().split())
if m == 1:
    print(1)
    quit()
mod = 10 ** 9 + 7
f = factorize(m)
max_k = max(i for _, i in f)
fac, inv = factorial(n + max_k - 1, mod)
ans = 1
for _, k in f:
    ans = ans * fac[n + k - 1] % mod * inv[n - 1] % mod * inv[k] % mod
print(ans)

