import fractions
from functools import reduce
import math

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


# def pathes(x, y):
#     xf = None
#     yf = None
#     xyf = None
#     temp = 1
#     for i in range(1, x + y + 1):
#         temp *= i % MOD
#         if i == x:
#             xf = temp
#         if i == y:
#             yf = temp
#         if i == x + y:
#             xyf = temp
#     # xf = math.factorial(x) % MOD
#     # yf = math.factorial(y) % MOD
#     # xyf = math.factorial(x + y) % MOD

#     return xyf * modinv(xf * yf % MOD, MOD)


def pathes(rf, cf, rcf):
    return rcf * modinv((rf * cf) % MOD, MOD)


def main():
    r1, c1, r2, c2 = map(int, input().split())

    f = [1 for _ in range(r2 + c2 + 2 + 1 + 1)]

    for i in range(1, r2 + c2 + 2 + 1):
        f[i] = f[i - 1] * i % MOD

    a = (pathes(f[r1], f[c1], f[r1 + c1]) - 1) % MOD
    b = (pathes(f[r1], f[c2 + 1], f[r1 + c2 + 1]) - 1) % MOD
    c = (pathes(f[r2 + 1], f[c1], f[r2 + 1 + c1]) - 1) % MOD
    d = (pathes(f[r2 + 1], f[c2 + 1], f[r2 + c2 + 2]) - 1) % MOD

    print((d - c - b + a) % MOD)


main()
