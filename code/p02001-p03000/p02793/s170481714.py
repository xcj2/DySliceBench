import sys
from collections import Counter

read = sys.stdin.read


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sieve_of_eratosthenes(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N, *A = map(int, read().split())
mod = 10 ** 9 + 7

primes = sieve_of_eratosthenes(max(A) + 1)
dic = {i: 0 for i in primes}

n = len(primes)
p = [0] * n
for i in A:
    tmp = Counter(prime_factorize(i))
    for key, value in tmp.items():
        #print(key, value)
        if dic[key] < value:
            dic[key] = value

lcm = 1
for i, j in dic.items():
    if j == 0:
        continue
    lcm *= pow(i, j, mod)
    lcm %= mod

answer = 0
for i in A:
    answer += lcm * pow(i, mod - 2, mod)
    answer %= mod

print(answer)
