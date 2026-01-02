MOD = 1000000007


def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


def modinv(a, mod=MOD):
    b = mod
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= mod
    if u < 0:
        u += mod
    return u


def LCM(a, b):
    return (a // GCD(a, b)) * b


n = int(input())
a = list(map(int, input().split()))

l = 1
for i in range(n):
    l = LCM(l, a[i])
ans = 0
l %= MOD
for i in range(n):
    ans += l * modinv(a[i]) % MOD
    ans %= MOD
print(ans)
