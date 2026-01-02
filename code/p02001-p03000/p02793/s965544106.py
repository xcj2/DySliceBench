from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

def llcm(l):
    return reduce(lcm, l)

def modinv(a, m):
    b, u, v = m, 1, 0
    while b:
        t = a // b
        a, b = b, a - t * b
        u, v = v, u - t * v
    u %= m
    if u < 0:
        u += m
    return u

def main():
    MOD = 10**9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    l = llcm(A) % MOD
    r = 0
    for i, a in enumerate(A):
        r = (r + l * modinv(a, MOD)) % MOD
    return r

print(main())
