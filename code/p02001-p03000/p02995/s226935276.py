#!/usr/bin/env python3


def gcd(m, n):
    if m < n:
        return gcd(n, m)
    if m % n == 0:
        return n
    return gcd(n, m % n)


def lcm(m, n):
    return n // gcd(m, n) * m


def solv(a, b, c, d):
    if b <= a:
        return 0

    lcm_cd = lcm(c, d)
    if a == 0:
        c0 = 0
    else:
        a = a - 1
        c0 = a - (a // c) - (a // d) + (a // lcm_cd)
    c1 = b - (b // c) - (b // d) + (b // lcm_cd)
    return c1 - c0


if __name__ == '__main__':

    a, b, c, d = map(int, input().split())

    # print(gcd(c, d))
    # print(lcm(c, d))

    ans = solv(a, b, c, d)

    print(ans)
