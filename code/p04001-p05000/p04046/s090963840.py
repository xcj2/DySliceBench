import math

MOD = 10**9+7


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def modinv(a):
    g, x, y = xgcd(a, MOD)
    return x % MOD


fact = [1] * 200100
for i in range(1, 200100):
    fact[i] = fact[i-1] * i % MOD


def calc(h, w):
    h -= 1
    w -= 1
    return (fact[h+w]*modinv(fact[h]) % MOD)*modinv(fact[w]) % MOD


h, w, a, b = map(int, input().split())
if a >= h // 2:
    ans = 0
    for i in range(1, h - a + 1):
        ans += calc(i, b) * calc(h + 1 - i, w - b) % MOD
        if ans >= MOD:
            ans -= MOD
    print(ans)

else:
    ans = calc(h, w)
    for i in range(h-a+1, h + 1):
        ans -= calc(i, b) * calc(h + 1 - i, w - b) % MOD
        if ans < 0:
            ans += MOD
    print(ans)
