# import sys
from math import factorial
from functools import reduce


def mmul(a, b, mod):
    return (a % mod) * (b % mod) % mod


def mfact(a, mod):
    fact = 1
    for m in range(2, a + 1):
        fact *= m % mod
        fact %= mod
    return fact


def mpow(a, b, mod):
    if b == 0:
        return 1
    if b == 1:
        return a % mod
    if b % 2 == 0:
        return mpow(a, b / 2, mod) ** 2 % mod
    return mpow(a, b // 2, mod) ** 2 * a % mod


def mdiv(a, b, mod):
    return mmul(a, mpow(b, mod - 2, mod), mod)


# (n+a)Ca = (n+a)! / n!a! mod mod for n >> a
def mnpaca(n, a, mod):
    res = 1
    for num in range(n + 1, n + a + 1):
        res *= num % mod
        res %= mod
    return mdiv(res, factorial(a), mod)

mod = 1000000007
N, M = [int(s) for s in input().split()]

prime_counts = []
i = 2
while i * i <= M:
    count = 0
    while M % i == 0:
        M /= i
        count += 1
    if count:
        prime_counts.append(count)
    i += 1
if M > 1:
    prime_counts.append(1)

res = reduce(lambda x, y: x * y, [mnpaca(N - 1, c, mod) for c in prime_counts],
             1)

print(res % mod)
