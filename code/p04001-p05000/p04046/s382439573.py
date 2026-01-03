import sys

sys.setrecursionlimit(10 ** 9)


def extgcd(a, b):
    x, y = 0, 0

    def f(a, b):
        nonlocal x, y
        if b == 0:
            x = 1
            y = 0

            return a

        g = f(b, a % b)
        q = a // b
        next_x = y
        y = x - q * y
        x = next_x
        return g

    g = f(a, b)
    return x, y, g


fact = [0] * 200010
invfact = [0] * 200010
mod = 10 ** 9 + 7


def nCr(n, r):
    ret = fact[n]
    ret = (ret * invfact[n - r]) % mod
    ret = (ret * invfact[r]) % mod
    return ret


fact[0] = 1
for i in range(1, 200000 + 1):
    fact[i] = (fact[i - 1] * i) % mod
for i in range(200000 + 1):
    x, y, g = extgcd(fact[i], mod)
    while x < 0:
        x += mod
    invfact[i] = x % mod

H, W, A, B = [int(_) for _ in input().split()]

ans = 0
for i in range(B, W):
    tmp = nCr((H - A - 1) + i, H - A - 1)
    tmp = tmp * nCr((A - 1) + (W - i - 1), A - 1) % mod
    ans = (ans + tmp) % mod
print(ans)
