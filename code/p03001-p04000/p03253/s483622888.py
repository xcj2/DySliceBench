#!/usr/bin/env python3

from math import sqrt, floor

PRIME = 1000000007

def mul(a, b):
    return (a * b) % PRIME

def div(n, d):
    return int(n / d)

def multiDiv(n, d):
    count = 0

    while n % d == 0:
        count += 1
        n = div(n, d)

    return (n, count)

def factoring(n):
    m = floor(sqrt(n))

    (n, f) = multiDiv(n, 2)
    ret = [f]

    for d in range(3, m+1, 2):
        (n, f) = multiDiv(n, d)
        if (f != 0):
            ret.append(f)

    if n != 1:
        ret.append(1)

    return ret

def pow(base, n):

    if n == 0:
        return 1

    if n % 2 == 0:
        return pow(mul(base, base), div(n, 2))
    else:
        return mul(base, pow(base, n - 1))

def reciprocal(n):
    return pow(n, PRIME - 2)

def com(n, k):
    if k == 0:
        return 1

    if (n - k) < k:
        return com(n, n - k)

    ret = 1

    for i in range(1, k + 1):
        ret = mul(ret, reciprocal(i))

    for i in range(n - k + 1, n + 1):
        ret = mul(ret, i)

    return ret


if __name__ == '__main__':

    line = [int(w) for w in input().split()]
    n = line[0]
    m = line[1]

    fs = factoring(m)

    def fun(x):
        return com(n + x - 1, x)
    cs = [fun(i) for i in fs]

    a = 1
    for i in cs:
        a = mul(a, i)

    print(a)
