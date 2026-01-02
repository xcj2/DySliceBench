import fractions
from functools import reduce

MOD = 10**9 + 7


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def pathes(x, y):
    xf = None
    yf = None
    xyf = None
    temp = 1
    for i in range(1, x + y + 1):
        temp = (temp*i) % MOD
        if i == x:
            xf = temp
        if i == y:
            yf = temp
        if i == x + y:
            xyf = temp

    return xyf * modinv(xf * yf % MOD, MOD)


def main():
    r1, c1, r2, c2 = map(int, input().split())

    a = (pathes(r1, c1) - 1) % MOD
    b = (pathes(r1, c2 + 1) - 1) % MOD
    c = (pathes(r2 + 1, c1) - 1) % MOD
    d = (pathes(r2 + 1, c2 + 1) - 1) % MOD

    print((d - c - b + a) % MOD)


main()
