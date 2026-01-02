def factorial(n, r, mod=10**9+7):
    a = 1
    for i in range(n, n-r, -1):
        a = a * i % mod
    return a


def power(n, r, mod=10**9+7):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod


def comb(n, k, mod=10**9+7):
    if n < k or k < 0:
        result = 0
    else:
        a = factorial(n, k, mod=mod)
        b = factorial(k, k, mod=mod)
        result = a * power(b, mod-2, mod=mod) % mod
    return result


n, a, b = map(int, input().split())
MOD = 10**9 + 7
ans = power(2, n) - comb(n, a) - comb(n, b) - 1
print(ans%MOD)