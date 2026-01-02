def fact(k, mod):
    a = [0] * (k + 1)
    a[0] = 1
    for i in range(1, k + 1):
        a[i] = a[i - 1] * i      
        a[i] = a[i] % mod
    return a
def power(a, n, mod):    
    if n == 0:
        return 1
    if n == 1:
        return a % mod
    if n % 2 == 0:
        return power((a * a) % mod, n // 2, mod) % mod
    else:
        return ((a % mod) * power(a % mod, n - 1, mod)) % mod
def inv(a, mod):
    c = [0] * (len(a))
    for i in range(len(a)):
        c[i] = power(a[i], mod - 2, mod)
    return c
n, m, k = [int(i) for i in input().split()]
mod = 998244353
res = fact(n - 1, mod)
res2 = inv(res, mod)
total = 0
base = power(m - 1, n - 1 - k, mod)
dp = [0] * (k + 1)
dp[0] = base
for i in range(1, k + 1):
    dp[i] = dp[i - 1] * (m - 1)
    dp[i] = dp[i] % mod
for i in range(k + 1):
    fact = (res2[i] * res2[n - 1 - i] * m) % mod
    total += (res[n - 1] * fact * dp[k - i]) % mod
    total = total % mod
print(total)