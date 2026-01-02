n, a, b = map(int, input().split())

mod = 10 ** 9 + 7
def extGCD(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extGCD(b, a%b)
    y -= a//b * x
    return g, x, y

def moddiv(a, b):
    _, inv, _ = extGCD(b, mod)
    return (a * inv) % mod

N = 2 * 10 ** 5 + 10
fact = [0] * (N)
fact[0] = 1
for i in range(1, N):
    fact[i] = (fact[i-1] * i) % mod

def comb(n, b):
    bunbo = 1
    for i in range(n-b+1, n+1):
        bunbo *= i
        bunbo %= mod
    return moddiv(bunbo, fact[b])

pow2 = [1] * 64
pow2[1] = 2
for i in range(2, 64):
    pow2[i] = pow2[i-1] ** 2 % mod

def pow(b):
    ret = 1
    for i in range(1, 64):
        if b & 1:
            ret *= pow2[i]
            ret %= mod
        b //= 2
    return ret

ans = pow(n) - 1

ans -= comb(n, a)
ans -= comb(n, b)
ans %= mod
print(ans)