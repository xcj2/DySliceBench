import collections
import math


def gcd(a, b):
    while True:
        a, b = b, a % b
        if b == 0:
            break
    return a


def eratosthenes(n):
    sieve = [True for _ in range(n + 1)]
    sieve[0] = False
    sieve[1] = False

    def _update(p):
        if sieve[p]:
            for i in range(p * 2, n + 1, p):
                sieve[i] = False

    if n > 1:
        _update(2)
    p = 3
    while p * p <= n:
        _update(p)
        p += 2
    return sieve


a, b = map(int, input().split())
c = gcd(a, b)

sieve = eratosthenes(math.ceil(math.sqrt(c)))
counter = collections.Counter()
for i in range(1, c):
    if i**2 > c:
        break
    if sieve[i]:
        while c % i == 0:
            counter[i] += 1
            c //= i
if c > 1:
    counter[c] += 1
print(len(counter) + 1)