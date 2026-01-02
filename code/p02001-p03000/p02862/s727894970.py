from functools import reduce

def modpow(a, m):
    ret = 1
    while m > 0:
        if m & 1:
            ret = ret * a % mod
        a = a * a % mod
        m = m >> 1
    return ret

def modinv(a):
    return modpow(a, mod - 2)

def cmb(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    over = reduce(lambda a, b: a * b % mod, range(n, n - r, -1))
    under = reduce(lambda a, b: a * b % mod, range(1, r + 1))
    return over * modinv(under) % mod

x, y = [int(i) for i in input().split()]
if (x + y) % 3 or x > 2 * y or y > 2 * x:
    print(0)
else:
    mod = 10**9 + 7
    print(cmb((x + y) // 3, (2 * x - y) // 3))
