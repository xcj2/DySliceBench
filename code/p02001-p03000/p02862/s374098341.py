X, Y = map(int, input().split())
MOD = 10 ** 9 + 7

def modpow(a, n):
    ret = 1
    while n > 0:
        if n & 1:
            ret = ret * a % MOD
        a = a * a % MOD
        n >>= 1
    return ret

def modinv(a):
    return modpow(a, MOD - 2)

def modfac(x):
    ret = 1
    for i in range(2, x + 1):
        ret *= i
        ret %= MOD
    return ret

ans = 0
if (X + Y) % 3 == 0:
    a = (2 * X - Y) // 3
    b = (2 * Y - X) // 3
    if a >= 0 and b >= 0:
        n = a + b
        r = a
        ans = modfac(n)
        ans *= modinv(modfac(n - r) * modfac(r))
        ans %= MOD
print(ans)