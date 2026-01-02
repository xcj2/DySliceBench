from functools import lru_cache

N, K = [int(i) for i in input().split()]

P = 10**9 + 7


@lru_cache(None)
def modinv(x):
    return pow(x, P-2, P)


@lru_cache(None)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


for i in range(2000):
    factorial(i)


def ncr(n, r):
    if r > n:
        return 0
    if n == 0:
        return 1
    a = factorial(n) * modinv(factorial(r) * factorial(n-r))
    return a % P


def m():
    for i in range(1, K+1):
        blue = ncr(K-1, i-1)
        red = ncr(N-K+1, i)
        print((blue * red) % P)


m()
