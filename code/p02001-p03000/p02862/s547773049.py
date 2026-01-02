# -*- coding: utf-8 -*-

X, Y = map(int, input().split())
mod = 10 ** 9 + 7

times = (X + Y) // 3
if (X + Y) % 3:
    print('0')
    exit()

x = X - times
y = Y - times


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def combination(n, r, mod):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res


if y < 0 or x < 0:
    print('0')
    exit()


print(combination(times, y, mod))
