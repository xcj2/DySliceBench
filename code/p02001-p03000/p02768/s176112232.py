mod = 1000000007

def pw(x, n):
    if n == 0: return 1
    elif n == 1: return x
    elif n % 2 == 0:
        return pw(x, n // 2) ** 2 % mod
    else:
        return x * pw(x, n // 2) ** 2 % mod

def dv(x, y):
    return x * pow(y, mod - 2, mod) % mod

def comb(n, r):
    p, q = 1, 1
    if n < r or n < 0 or r < 0: return 0
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return dv(p, q)

n, a, b = map(int, input().split())
ans = pow(2, n, mod) - 1 + mod * 10
if a <= n: ans -= comb(n, a)
if b <= n: ans -= comb(n, b)
print(ans % mod)